from functools import wraps
from flask import request, make_response, jsonify
from api.constants.http_exceptions import HTTP_EXCEPTIONS
from api.constants.http_constants import HTTP_STATUS, ARCHAEA_REQUEST_ID


def __request_id_not_found():
    """
    The error thrown in case request Id not found

    :return:
    """
    request_id_failure = {
        'message': HTTP_EXCEPTIONS['REQUEST_ID_NOT_FOUND']
    }
    return make_response(jsonify(request_id_failure), HTTP_STATUS['PRE_CONDITION_FAILED'])


def __wrong_content_type():
    """
    The error thrown in case request Id not found

    :return:
    """
    content_type_failure = {
        'message': HTTP_EXCEPTIONS['CONTENT_TYPE_INVALID']
    }
    return make_response(jsonify(content_type_failure), HTTP_STATUS['PRE_CONDITION_FAILED'])


def header_validate(f):
    """
    The decorator for basic auth

    :param f:
    :return:
    """

    @wraps(f)
    def decorated(*args, **kwargs):
        request_id = request.headers.get(ARCHAEA_REQUEST_ID)
        content_type = request.headers.get('Content-Type')
        if not content_type or not (content_type == 'application/json'):
            return __wrong_content_type()
        if not request_id:
            return __request_id_not_found()
        return f(*args, **kwargs)

    return decorated
