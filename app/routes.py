from app import app, api
from flask import request
from flask_restful import Resource
import json
import pprint
import os
import subprocess
import traceback


import logging

class WelcomeController(Resource):
    def get(self):

        return {'welcome': "welcome, stranger!"}

api.add_resource(WelcomeController, '/')