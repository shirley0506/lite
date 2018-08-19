import unittest, os, time
from selenium import webdriver
from time import sleep
from myPublic import userLogin, menu

class datasearch(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.url = "http://172.31.18.33"
        userLogin.Login(cls.driver, cls.url)
        menu.searchMenu(cls.driver)
        sleep(2)
