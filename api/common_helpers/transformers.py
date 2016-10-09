from json import loads


class Transformers:
    
    def __init__(self):
        pass

    @staticmethod
    def application_to_json(application):
        return {
            'application_id': application.application_id,
            'application_guid': application.application_guid,
            'application_name': application.application_name,
            'application_key': application.application_key,
            'application_secret': application.application_key,
            'account_guid': application.account_guid,
            'algorithm': application.application_algorithm,
            'user_id': application.user_id,
            'app_metadata': loads(application.app_metadata),
            'created_at': str(application.created_at),
            'updated_at': str(application.updated_at)
        }

    @staticmethod
    def application_to_json_list(applications):
        applications_list = []
        for application in applications:
            applications_list.append(Transformers.application_to_json_list(application))
        return applications_list
