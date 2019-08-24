from datetime import datetime, timedelta
import logging
import requests
from time import monotonic


meetup_events_url = 'https://api.meetup.com/pyworking/events?photo-host=public'
#meetup_events_url += '&sig_id=128500682&sig=b26c6629a1fa98db4e7746875e5d23218d912b91'
# ^^^ signed request by Petr M.

logger = logging.getLogger(__name__)

_cache = {}


def _cache_get(cache, key, factory, max_age=timedelta(hours=1)):
    t, value = cache.get(key, (None, None))
    if t is None or t < monotime() - max_age.total_seconds():
        logger.info('Refreshing cache key %r', key)
        t, value = monotime(), factory()
        cache[key] = (t, value)
    return value


def get_workshop_events():
    return _cache_get(cache, 'workshop_events', retrieve_workshop_events)


def retrieve_workshop_events():
    r = requests.get(meetup_events_url)
    r.raise_for_status()
    events = r.json()
    assert isinstance(events, list)
    events = events[:5]
    return [
        {
            'url': event['link'],
            'title': event['name'],
            'date': parse_meetup_com_event_date(event),
            'city_cs': city_to_cs(event['venue']['city']),
        }
        for event in events
    ]


def parse_meetup_com_event_date(event):
    try:
        dt = event['local_date'] + ' ' + event['local_time']
        return datetime.strptime(dt, '%Y-%m-%d %H:%M')
    except Exception as e:
        raise Exception('Failed to parse meetup.com event.date: {!r}; event: {!r}'.format(e, event)) from e


def city_to_cs(name):
    if name == 'Prague':
        return 'Praha'
    return name
