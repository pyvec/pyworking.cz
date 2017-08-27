from datetime import date, datetime
from flask import Blueprint, render_template

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


_cs_weekdays = 'pondělí úterý středa čtvrtek pátek sobota neděle'.split()


def format_date_cs(dt):
    assert isinstance(dt, (date, datetime))
    return '{} {}. {}. {}'.format(_cs_weekdays[dt.weekday()], dt.day, dt.month, dt.year)
