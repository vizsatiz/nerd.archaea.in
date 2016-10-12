from json import dumps
from flask import Blueprint, request
from api.common_helpers.transformers import Transformers
from api.common_helpers.http_response import HttpResponse
from api.common_helpers.common_constants import ApiVersions
from api.services.application_service import ApplicationService

publish_handler = Blueprint(__name__, __name__)


@publish_handler.route(ApiVersions.API_VERSION_V1 + '/application/publish', methods=['POST'])
def app_publish():
    try:
        name = request.json['name']
        application_guid = request.json['application_guid']
        account_guid = request.json['account_guid']
        algorithm = request.json['algorithm']
        user_id = request.json['user_id']
        app_metadata = dumps(request.json['app_metadata'])
        # TODO To check whether the application trying to be published aleady exists and if yes
        # TODO do the necessary
        if not name or not account_guid or not algorithm or not user_id or app_metadata:
            return HttpResponse.bad_request('Missing parameters to publish app')
        application = ApplicationService.create_application(account_guid=account_guid,
                                                            application_name=name,
                                                            application_guid=application_guid,
                                                            application_algorithm=algorithm,
                                                            user_id=user_id,
                                                            app_metadata=app_metadata)
        return HttpResponse.success(application)
    except Exception as e:
        return HttpResponse.internal_server_error(e.message)


@publish_handler.route(ApiVersions.API_VERSION_V1 + '/application', methods=['GET'])
def get_all_apps():
    try:
        applications = ApplicationService.get_applications()
        return HttpResponse.success(Transformers.application_to_json_list(applications))
    except Exception as e:
        return HttpResponse.internal_server_error(e.message)


@publish_handler.route(ApiVersions.API_VERSION_V1 + '/application/<application_guid>', methods=['GET'])
def get_app(application_guid):
    try:
        application = ApplicationService.get_applications({
            'application_guid': application_guid
        })
        return HttpResponse.success(Transformers.application_to_json(application))
    except Exception as e:
        return HttpResponse.internal_server_error(e.message)


@publish_handler.route(ApiVersions.API_VERSION_V1 + '/application/<application_guid>/publish', methods=['DELETE'])
def un_publish_apps(application_guid):
    try:
        ApplicationService.delete_application({
            'application_guid': application_guid
        })
        return HttpResponse.accepted('Your application has been successfully unpublished')
    except Exception as e:
        HttpResponse.internal_server_error(e.message)
