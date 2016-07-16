from flask import Blueprint, Flask
from api.auth.basic_auth import basic_auth
from api.handlers.v1_0.lin_reg_handler import lr_handler

bp = Blueprint(__name__, __name__)
app = Flask(__name__)


@bp.route('/')
@basic_auth
def index():
    return "Hello, World!"

if __name__ == '__main__':
    app.register_blueprint(lr_handler)
    app.register_blueprint(bp)
    app.run(debug=True)