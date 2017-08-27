from datetime import date
from functools import lru_cache
from markdown2 import markdown
import os
from pathlib import Path
import re
import yaml


here = Path(__file__).resolve().parent
project_dir = here.parent


def get_data_dir():
    env_name = 'DATA_DIR'
    if os.environ.get(env_name):
        data_dir = Path(os.environ[env_name])
    else:
        data_dir = project_dir / 'data'
    if not data_dir.is_dir():
        raise Exception('Data directory is not a directory: {}'.format(data_dir))
    return data_dir


def load_events():
    global _cached_events
    event_dir = get_data_dir() / 'events'
    events = []
    for event_path in event_dir.iterdir():
        if event_path.name.startswith('.') or not event_path.name.endswith('.yaml'):
            continue
        try:
            events.append(_load_event(event_path))
        except Exception as e:
            raise Exception('Failed to load event from {}: {}'.format(event_path, e)) from e
    return sorted(events, key=lambda ev: ev['date'], reverse=True)


def _load_event(event_path):
    data = yaml.load(event_path.read_text())['event']
    return {
        'title': data['title'],
        'location': data.get('location'),
        'date': _to_date(data['date']) if data.get('date') else None,
        'description_html': markdown_to_html(data['description']) if data.get('description') else None,
    }


@lru_cache()
def markdown_to_html(text):
    return markdown(
        text,
        extras=[
            "link-patterns",
        ],
        link_patterns=[
            (re.compile(r'(https?:\/\/[^ \t\n]+)'), r'\1'),
        ])


def _to_date(value):
    if isinstance(value, date):
        return value
    else:
        # pravděpodobně bude stačit sem jen něco přidat
        # YAML jinak umí date interpretovat sám
        raise Exception('Not a date: {!r}'.format(value))
