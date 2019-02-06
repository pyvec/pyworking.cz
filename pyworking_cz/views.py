from datetime import date, datetime
from flask import Blueprint, Response, current_app, abort, redirect, render_template, url_for, request, send_from_directory
from pathlib import Path
import pytz

from .meetup_com import retrieve_workshop_events
from .model import load_events


bp = Blueprint('views', __name__)


@bp.route('/')
def index():
    events = load_events()
    today = pytz.utc.localize(datetime.utcnow())
    upcoming = [ev for ev in events if ev['date'] >= today]
    past = [ev for ev in events if ev['date'] < today]
    return render_template('index.html',
        format_date_cs=format_date_cs,
        upcoming_session_events=retrieve_workshop_events(),
        upcoming_workshop_events=sorted(upcoming, key=lambda ev: ev['date']),
        past_workshop_events=past)


@bp.route('/favicon.ico')
def favicon():
    return send_from_directory(
        Path(current_app.root_path) / 'static',
        'favicon/favicon.ico',
        mimetype='image/vnd.microsoft.icon')


@bp.route('/workshops/')
def workshops_index():
    return redirect('/')


@bp.route('/workshops/<slug>')
def workshop_detail(slug):
    events = load_events()
    event, exact = find_event_by_slug(events, slug)
    if not event:
        abort(404)
    if not exact:
        return redirect(url_for('.workshop_detail', slug=event['slug']))
    return render_template('workshop.html',
        event=event,
        format_date_cs=format_date_cs)


@bp.route('/workshops.ics')
def workshops_ical():
    import ics
    cal_events = []
    for event in load_events():
        try:
            if not event['date']:
                continue
            cal_event = ics.Event(
                name=event['title'],
                location=event['location'],
                begin=event['date'].isoformat(),
                uid='{}@pyworking.cz'.format(event['slug']),
                url='https://pyworking.cz' + event['url_path'],
            )
            #cal_event.geo = '{}:{}'.format(geo_obj.latitude, geo_obj.longitude)
            cal_events.append(cal_event)
        except Exception as e:
            raise Exception('Failed to export event: {!r}; event: {}'.format(e, event)) from e
    return Response(ics.Calendar(
        events=cal_events),
        mimetype='text/plain' if request.args.get('debug') else 'text/calendar')


def find_event_by_slug(events, slug):
    '''
    Try to find the event matching the slug.
    Returns tuple (event, exact_match).
    Where exact_match is True only if event slug == slug (from parameters).
    '''
    for e in events:
        if e['slug'] == slug:
            return e, True
    # ok, no event has the same slug, try again but case-insensitive
    for e in events:
        if e['slug'].lower() == slug.lower():
            return e, False
    # no event found
    return None, None


_cs_weekdays = 'pondělí úterý středa čtvrtek pátek sobota neděle'.split()

_cs_months_genitiv = '- ledna února března dubna května června července srpna září října listopadu prosince'.split()

def format_date_cs(dt):
    assert isinstance(dt, (date, datetime))
    return '{} {}. {} {}'.format(_cs_weekdays[dt.weekday()], dt.day, _cs_months_genitiv[dt.month], dt.year)
