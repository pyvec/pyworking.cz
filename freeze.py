from flask_frozen import Freezer
from pyworking_cz.web import app
from pyworking_cz.model import load_events

freezer = Freezer(app)


@freezer.register_generator
def workshop_detail():
    events = load_events()
    return [("views.workshop_detail", {"slug": event["slug"]}) for event in events]

if __name__ == '__main__':
    freezer.freeze()
