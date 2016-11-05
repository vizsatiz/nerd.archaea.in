import datetime
from database import Base
from sqlalchemy import Column, Integer, String, DateTime


class Applications(Base):

    __tablename__ = 'applications'

    application_id = Column(Integer, primary_key=True, nullable=False)
    account_id = Column(String(64), nullable=False)
    application_name = Column(String(64), unique=True, nullable=False)
    application_guid = Column(String(64), unique=True, nullable=False)
    application_key = Column(String(64), nullable=False)
    application_secret = Column(String(255), nullable=False)
    application_algorithm = Column(String(64), nullable=False)
    created_user_id = Column(Integer, nullable=False)
    app_metadata = Column(String(1024), nullable=False)

    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow())

    def __init__(self,
                 account_id=None,
                 application_name=None,
                 application_guid=None,
                 application_key=None,
                 application_secret=None,
                 application_algorithm=None,
                 created_user_id=None,
                 app_metadata=None):
        """
        Apps published list

        :param account_guid:
        :param application_name:
        :param application_guid:
        :param application_key:
        :param application_secret:
        :param user_id:
        :param app_metadata:
        """
        self.account_id = account_id
        self.application_name = application_name
        self.application_guid = application_guid
        self.application_key = application_key
        self.application_secret = application_secret
        self.application_algorithm = application_algorithm
        self.created_user_id = created_user_id
        self.app_metadata = app_metadata

    def __repr__(self):
        return '<Applications %r>' % self.application_name

