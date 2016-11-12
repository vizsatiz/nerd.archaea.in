from dal.applications_adapter import ApplicationAdapter
from api.common_helpers.common_utils import CommonHelper


class ApplicationService:

    def __init__(self):
        pass

    @staticmethod
    def create_application(account_id=None,
                           application_name=None,
                           application_algorithm=None,
                           created_user_id=None,
                           app_metadata=None):
        application_key = CommonHelper.generate_guid()
        application_secret = CommonHelper.generate_guid()
        application_guid = CommonHelper.generate_guid()
        # TODO validate metadata for each algorithm
        ApplicationAdapter.create(account_id=account_id,
                                  application_name=application_name,
                                  application_guid=application_guid,
                                  application_key=application_key,
                                  application_secret=application_secret,
                                  application_algorithm=application_algorithm,
                                  created_user_id=created_user_id,
                                  app_metadata=app_metadata)
        return {
            'application_guid': application_guid,
            'application_key': application_key,
            'application_secret': application_secret
        }

    @staticmethod
    def get_applications(query=None):
        if not query:
            return ApplicationAdapter.get_all_apps()
        else:
            return ApplicationAdapter.read(query)

    @staticmethod
    def delete_application(query=None):
        ApplicationAdapter.delete(query)

    @staticmethod
    def update_application(query=None, update_value=None):
        ApplicationAdapter.update(query=query, updated_value=update_value)