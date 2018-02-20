from datetime import date, datetime
from flask import Blueprint, abort, redirect, render_template, url_for

from .model import load_events


bp = Blueprint('views', __name__)


@bp.route('/')
def index():
    events = load_events()
    today = datetime.now().date()
    return render_template('index.html',
        format_date_cs=format_date_cs,
        upcoming_events=[ev for ev in events if ev['date'] >= today],
        past_events=[ev for ev in events if ev['date'] < today])


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
