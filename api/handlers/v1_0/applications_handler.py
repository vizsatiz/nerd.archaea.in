from json import dumps
from flask import Blueprint, request
from api.common_helpers.transformers import Transformers
from api.common_helpers.http_response import HttpResponse
from api.common_helpers.common_constants import ApiVersions
from api.services.application_service import ApplicationService

applications_handler = Blueprint(__name__, __name__)


@applications_handler.route(ApiVersions.API_VERSION_V1 + '/applications', methods=['POST'])
def app_publish():
    try:
        application_name = request.json['application_name']
        account_id = request.json['account_id']
        algorithm = request.json['algorithm']
        user_id = request.json['user_id']
        app_metadata = dumps(request.json['app_metadata'])
        applications = ApplicationService.get_applications({
            'application_name': application_name
        })
        if len(applications) > 0:
            return HttpResponse.bad_request(
                'This application with this name already exist.'
                ' Please rename the application that you are trying to create')
        if not application_name or not account_id or not algorithm or not user_id or not app_metadata:
            return HttpResponse.bad_request('One or more parameters are missing')
        application = ApplicationService.create_application(account_id=account_id,
                                                            application_name=application_name,
                                                            application_algorithm=algorithm,
                                                            created_user_id=user_id,
                                                            app_metadata=app_metadata)
        return HttpResponse.success(application)
    except Exception as e:
        return HttpResponse.internal_server_error(e.message)


@applications_handler.route(ApiVersions.API_VERSION_V1 + '/applications', methods=['GET'])
def get_all_apps():
    try:
        applications = ApplicationService.get_applications()
        return HttpResponse.success(Transformers.application_to_json_list(applications))
    except Exception as e:
        return HttpResponse.internal_server_error(e.message)


@applications_handler.route(ApiVersions.API_VERSION_V1 + '/applications/<application_guid>', methods=['GET'])
def get_app(application_guid):
    try:
        application = ApplicationService.get_applications({
            'application_guid': application_guid
        })
        if len(application) == 0:
            return HttpResponse.bad_request('The application is not published on this nerd')
        return HttpResponse.success(Transformers.application_to_json(application[0]))
    except Exception as e:
        return HttpResponse.internal_server_error(e.message)


@applications_handler.route(ApiVersions.API_VERSION_V1 + '/applications/<application_guid>', methods=['DELETE'])
def un_publish_apps(application_guid):
    try:
        ApplicationService.delete_application({
            'application_guid': application_guid
        })
        return HttpResponse.accepted('Your application has been successfully deleted')
    except Exception as e:
        HttpResponse.internal_server_error(e.message)