from flask import Blueprint, request
from api.services.application_service import ApplicationService
from api.common_helpers.http_response import HttpResponse
from api.common_helpers.common_constants import ApiVersions
from api.services.compute_service import ComputeEngineMapper

compute_handler = Blueprint(__name__, __name__)


@compute_handler.route(ApiVersions.API_VERSION_V1 + '/application/compute', methods=['POST'])
def compute_app():
    try:
        try:
            app_key = request.headers['app_key']
            app_secret = request.headers['app_secret']
            data_point = request.json['data_point']
        except Exception:
            return HttpResponse.bad_request('One or more parameters are missing')
        application = ApplicationService.get_applications({
            'app_key': app_key,
            'app_secret': app_secret
        })
        if len(application) == 0:
            return HttpResponse.bad_request('Invalid appKey or appSecret')
        compute_engine = ComputeEngineMapper.get_compute_engine(algorithm=application.algorithm)
        try:
            computed_output = compute_engine(application=application, data=data_point)
            return HttpResponse.success({
                'prediction': computed_output
            })
        except Exception as e:
            HttpResponse.bad_request('Unable to complete the computation : ' + e.message)
    except Exception as e:
        return HttpResponse.internal_server_error(e.message)