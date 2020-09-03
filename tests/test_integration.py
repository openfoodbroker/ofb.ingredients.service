import requests
import json
import pprint
import unittest
import time
import pytest

from modules.RESTClient import RESTClient


environments = [("http://localhost:5000"), ("http://localhost:8081")]


@pytest.mark.parametrize("base_url", environments)
def test_welcome(base_url):
    r = requests.get(base_url + "/")
    print(r.text)
    assert r.status_code == 200

    
