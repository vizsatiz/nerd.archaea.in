from flask import Blueprint, Flask
from handlers.v1_0.training_handler import training_handler
from handlers.v1_0.compute_handler import compute_handler
from handlers.v1_0.applications_handler import applications_handler

bp = Blueprint(__name__, __name__)
app = Flask(__name__)

if __name__ == '__main__':
    app.register_blueprint(bp)
    app.register_blueprint(applications_handler)
    app.register_blueprint(training_handler)
    app.register_blueprint(compute_handler)
    app.run(debug=True, port=9081)
