from flask import Blueprint, Flask
from api.auth.basic_auth import basic_auth

bp = Blueprint(__name__, __name__)
app = Flask(__name__)


@bp.route('/')
@basic_auth
def index():
    return "Hello, World!"

if __name__ == '__main__':
    app.register_blueprint(bp)
    app.run(debug=True)