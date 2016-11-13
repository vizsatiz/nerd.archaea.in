import datetime
from database import Base
from sqlalchemy import Column, Integer, String, DateTime, Text


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
    training_status = Column(String(64), nullable=True)
    app_metadata = Column(Text, nullable=False)

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
                 app_metadata=None,
                 training_status=None):
        self.account_id = account_id
        self.application_name = application_name
        self.application_guid = application_guid
        self.application_key = application_key
        self.application_secret = application_secret
        self.application_algorithm = application_algorithm
        self.created_user_id = created_user_id
        self.app_metadata = app_metadata
        self.training_status = training_status

    def __repr__(self):
        return '<Applications %r>' % self.application_name
