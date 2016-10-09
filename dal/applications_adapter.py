from database import db
from dal.base_adapter import BaseAdapter
from models.applications import Applications


class ApplicationAdapter(BaseAdapter):

    def __init__(self):
        BaseAdapter.__init__(self)

    @staticmethod
    def create(account_guid=None,
               application_name=None,
               application_guid=None,
               application_key=None,
               application_secret=None,
               application_algorithm=None,
               user_id=None,
               app_metadata=None):
        application = Applications(account_guid=account_guid,
                                   application_name=application_name,
                                   application_guid=application_guid,
                                   application_key=application_key,
                                   application_secret=application_secret,
                                   application_algorithm=application_algorithm,
                                   user_id=user_id,
                                   app_metadata=app_metadata)
        db.add(application)
        db.commit()
        return application.application_id

    @staticmethod
    def update(query=None, updated_value=None):
        """
        This method update the account

        :param query:
        :param updated_value:
        :return:
        """
        db.query(Applications) \
            .filter_by(**query) \
            .update(updated_value)
        db.commit()

    @staticmethod
    def delete(query=None):
        """
        This methods deletes the record

        :param query:
        :return:
        """
        db.query(Applications) \
            .filter_by(**query) \
            .delete()
        db.commit()

    @staticmethod
    def read(query=None):
        """
        Reading the records from a table

        :param query:
        :return:
        """
        applications = db.query(Applications) \
            .filter_by(**query).all()
        assert isinstance(applications, list)
        return applications

    @staticmethod
    def get_all_apps():
        """
        Get all apps

        :return:
        """
        applications = db.query(Applications).all()
        assert isinstance(applications, list)
        return applications

