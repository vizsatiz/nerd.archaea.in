from functools import wraps
from flask import request, make_response, jsonify
from api.constants.http_constants import HTTP_STATUS
from api.constants.http_exceptions import HTTP_EXCEPTIONS


def __check_basic_auth(username, password):
    """This function is called to check if a username /
    password combination is valid.
    """
    return username == 'admin' and password == 'secret'


def __basic_auth_failure():
    """
    Sends a 401 response for basic auth

    :return:
    """
    auth_failure = {
        'message': HTTP_EXCEPTIONS['BASIC_AUTH_FAILURE']
    }
    return make_response(jsonify(auth_failure), HTTP_STATUS['UNAUTHORIZED'])


def basic_auth(f):
    """
    The decorator for basic auth

    :param f:
    :return:
    """

    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not __check_basic_auth(auth.username, auth.password):
            return __basic_auth_failure()
        return f(*args, **kwargs)

    return decorated
