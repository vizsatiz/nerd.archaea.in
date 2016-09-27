from flask import Blueprint, request
from api.auth.basic_auth import basic_auth
from api.auth.header_validator import validate_headers
from api.constants.http_constants import API_VERSION_V1

lr_handler = Blueprint(__name__, __name__)


@lr_handler.route(API_VERSION_V1 + '/linear_regression', methods=['POST'])
@basic_auth
@validate_headers
def linear_regression_trainer():
    print request.json['name']
    return 'myName'
