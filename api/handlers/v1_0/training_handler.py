from flask import Blueprint, request
from api.services.application_service import ApplicationService
from api.common_helpers.http_response import HttpResponse
from api.common_helpers.common_constants import ApiVersions
from api.services.training_service import TrainingEngineMapper

training_handler = Blueprint(__name__, __name__)


@training_handler.route(ApiVersions.API_VERSION_V1 + '/application/train', methods=['POST'])
def train_app():
    try:
        try:
            app_key = request.headers['app_key']
            app_secret = request.headers['app_secret']
            training_data = request.json['training_data']
        except Exception:
            return HttpResponse.bad_request('One or more parameters are missing')
        application = ApplicationService.get_applications({
            'app_key': app_key,
            'app_secret': app_secret
        })
        if len(application) == 0:
            return HttpResponse.bad_request('Invalid appKey or appSecret')
        training_engine = TrainingEngineMapper.get_training_engine(algorithm=application.algorithm)
        training_status = training_engine(application=application, training_data=training_data)
        return HttpResponse.success(training_status)
    except Exception as e:
        return HttpResponse.internal_server_error(e.message)