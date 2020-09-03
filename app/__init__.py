from flask import Flask
from flask_restful import Api
from config import Config

debug=True

import logging

app = Flask(__name__)
app.config.from_object(Config)
api = Api(app, catch_all_404s=True)

from modules.OnLoadActions import OnLoadActions

app.logger.debug('weird call I need to enable logging')

ola = OnLoadActions()
ola.logger = app.logger
ola.run() 

from app import routes


