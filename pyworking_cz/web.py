import flask

from .views import bp as views_bp


app = flask.Flask(__name__)
app.register_blueprint(views_bp)
