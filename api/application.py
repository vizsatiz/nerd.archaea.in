from flask import Blueprint, Flask
from api.handlers.v1_0.app_publish_handler import publish_handler

bp = Blueprint(__name__, __name__)
app = Flask(__name__)


@bp.route('/')
def index():
    return "Hello, World!"

if __name__ == '__main__':
    app.register_blueprint(bp)
    app.register_blueprint(publish_handler)
    app.run(debug=True, port=9080)