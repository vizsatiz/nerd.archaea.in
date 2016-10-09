from database import db
from dal.base_adapter import BaseAdapter
from models.configuration import Configuration


class ConfigurationAdapter(BaseAdapter):

    def __init__(self):
        BaseAdapter.__init__(self)

    @staticmethod
    def create(configuration_guid=None,
               bot_name=None,
               account_guid=None,
               plan_family=None,
               plan_metadata=None):
        configuration = Configuration(configuration_guid=None,
                                    bot_name=None,
                                    account_guid=None,
                                    plan_family=None,
                                    plan_metadata=None)
        db.add(configuration)
        db.commit()
        return configuration.application_id

    @staticmethod
    def update(query=None, updated_value=None):
        """
        This method update the account

        :param query:
        :param updated_value:
        :return:
        """
        db.query(Configuration) \
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
        db.query(Configuration) \
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
        configuration = db.query(Configuration) \
            .filter_by(**query).all()
        assert isinstance(configuration, list)
        return configuration
