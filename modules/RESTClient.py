import requests
import logging
import http.client as http_client
import json
import pprint

LOGGING = True
LOGLEVEL = logging.DEBUG

if LOGGING:

  http_client.HTTPConnection.debuglevel = 2
  logging.basicConfig()
  logging.getLogger().setLevel(LOGLEVEL)
  requests_log = logging.getLogger("requests.packages.urllib3")
  requests_log.setLevel(LOGLEVEL)
  requests_log.propagate = True


class RESTClient:
  def __init__(self):
    self.default_headers = {"Content-Type": "application/json"}

  def get(self, endpoint, headers=None):
    """ GET """
    if headers == None:
      r = requests.get(endpoint)
    else:
      r = requests.get(endpoint, headers=headers)


    if r.status_code < 300:
      return r
    else:
      # print("status code: %s" % r.status_code)
      # print (r.headers)
      raise Exception(r.text)

  def post(self, endpoint, payload=None, headers=None):
    """ POST """
    if headers == None:
      r = requests.post(endpoint, headers=self.default_headers, data=json.dumps(payload))
    else:
      headers = headers.update(self.default_headers)
      r = requests.post(endpoint, headers=headers, data=json.dumps(payload))


    if r.status_code < 300:
      return r
    else:
      # print("status code: %s" % r.status_code)
      # print (r.headers)
      raise Exception(r.text)




