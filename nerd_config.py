import os
import json


PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
with open(PROJECT_ROOT + '/nerd.config.json') as config_file:
    config = json.load(config_file)

# Database Setup
MY_SQL_HOST_URL = config['DATABASE_URL']
