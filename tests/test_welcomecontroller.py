
import requests
from modules.WelcomeController import WelcomeController

def test_welcome_get():
  wc = WelcomeController()
  assert wc.get() == {'welcome': "welcome, stranger!"}
  