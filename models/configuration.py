import datetime
from database import Base
from sqlalchemy import Column, Integer, String, DateTime


class Configuration(Base):

    __tablename__ = 'configuration'

    configuration_id = Column(Integer, primary_key=True, nullable=False)
    configuration_guid = Column(String(64), unique=True, nullable=False)
    bot_name = Column(String(64), nullable=False)
    account_guid = Column(String(64), unique=True, nullable=False)
    plan_family = Column(String(32), nullable=False)
    plan_metadata = Column(String(64), nullable=False)

    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow())

    def __init__(self,
                 configuration_guid=None,
                 bot_name=None,
                 account_guid=None,
                 plan_family=None,
                 plan_metadata=None):

        self.configuration_guid = configuration_guid
        self.bot_name = bot_name
        self.account_guid = account_guid
        self.plan_family = plan_family
        self.plan_metadata = plan_metadata

    def __repr__(self):
        return '<Configuration %r>' % self.bot_name

