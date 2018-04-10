import unittest
from selenium import webdriver
from time import sleep

class AssertAddWeb(unittest.TestCase):
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get("http://localhost:8080/lite/")
        cls.driver.find_element_by_id("userId").send_keys("root")
        cls.driver.find_element_by_id("password").send_keys("root")
        cls.driver.find_element_by_class_name("icon-arrow-right").click()
        sleep(2)
    def setUp(self):

    def tearDown(self):
        pass

    def test_add_new(self):
        self.driver