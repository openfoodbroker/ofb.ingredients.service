import requests
import json
import pprint
import unittest
import random
import yaml

class TestConfig(unittest.TestCase):

    @classmethod
    def setUpClass(self):

        self.config_yml = "config.yml"

    @classmethod
    def tearDownClass(self):
        pass

    def test_config_yml(self):
        
        with open(self.config_yml) as f:
            data = yaml.load(f, Loader=yaml.FullLoader)
            print(data["stages"]["dev"])