from flask import Blueprint
from api.auth.basic_auth import basic_auth
from api.constants.http_constants import API_VERSION_V1

lr_handler = Blueprint(__name__, __name__)


@basic_auth
@lr_handler.route(API_VERSION_V1 + '/linear_regression', methods=['GET'])
def linear_regression_trainer():
    return 'myname'
