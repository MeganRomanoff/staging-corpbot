# Test Script by Megan

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class CorpBotv1:
 
def __init__(self, email, password):
    self.email = email
    self.password = password
    self.driver = webdriver.Firefox()
 
def closeBrowser(self):
    self.driver.close()      

def invite():
    """ REST to DO """
