from datetime import date
import os
from pathlib import Path
import re
import yaml

from .util import markdown_to_html


here = Path(__file__).resolve().parent
project_dir = here.parent


def get_data_dir():
    '''
    Get path to data dir - from DATA_DIR env variable (used in production) or simply
    from project path (in development mode, works for pip install -e).
    '''
    env_name = 'DATA_DIR'
    if os.environ.get(env_name):
        data_dir = Path(os.environ[env_name])
    else:
        data_dir = project_dir / 'data'
    if not data_dir.is_dir():
        raise Exception('Data directory is not a directory: {}'.format(data_dir))
    return data_dir


def load_events():
    '''
    Load all events from data/events/*.yaml
    '''
    event_dir = get_data_dir() / 'events'
    is_event_file_name = lambda name: not name.startswith('.') and name.endswith('.yaml')
    events = [_load_event(p) for p in event_dir.iterdir() if is_event_file_name(p.name)]
    return sorted(events, key=lambda ev: ev['date'], reverse=True)


def _load_event(event_path):
    '''
    Load event data from YAML file
    '''
    try:
        data = yaml.load(event_path.read_text())['event']
        return {
            'title': data['title'],
            'location': data.get('location'),
            'date': _to_date(data['date']) if data.get('date') else None,
            'description_html': markdown_to_html(data['description']) if data.get('description') else None,
            'authors': data.get('authors'),
        }
    except Exception as e:
        raise Exception('Failed to load event from {}: {}'.format(event_path, e)) from e


def _to_date(value):
    if isinstance(value, date):
        return value
    else:
        # pravděpodobně bude stačit sem jen něco přidat
        # YAML jinak umí date interpretovat sám
        raise Exception('Not a date: {!r}'.format(value))
