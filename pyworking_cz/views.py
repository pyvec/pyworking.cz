from datetime import date, datetime
from flask import Blueprint, abort, redirect, render_template

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
    try:
        event, = [e for e in events if e['slug'] == slug]
    except ValueError:
        abort(404)
    return render_template('workshop.html',
        event=event,
        format_date_cs=format_date_cs)



_cs_weekdays = 'pondělí úterý středa čtvrtek pátek sobota neděle'.split()

_cs_months_genitiv = '- ledna února března dubna května června července srpna září října listopadu prosince'.split()

def format_date_cs(dt):
    assert isinstance(dt, (date, datetime))
    return '{} {}. {} {}'.format(_cs_weekdays[dt.weekday()], dt.day, _cs_months_genitiv[dt.month], dt.year)
