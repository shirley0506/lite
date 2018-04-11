import unittest, os, time
from selenium import webdriver
from time import sleep
from myPublic import userLogin, menu
from selenium.common.exceptions import UnexpectedAlertPresentException
from selenium.webdriver.common.keys import Keys
import HTMLTestRunner


def ifexistAsset(self):
    # 通过定位父元素，操作子元素，操作兄弟元素
    parents = self.driver.find_elements_by_xpath("//table[@id='editable-sample']/tbody/tr")
    for parent in parents:
        sons = parent.find_elements_by_xpath("./td[2]")
        for son in sons:
            if 'test_selenium' in son.text:
                son.find_element_by_xpath("../td[1]/input[@name='checkAssets']").click()
                sleep(2)
                self.driver.find_element_by_xpath("//div[@class='widget-body']/div[1]/button[2]").click()
                sleep(2)
                self.driver.switch_to.alert.accept()
                sleep(2)
                try:
                    self.driver.switch_to.alert.accept()
                except UnexpectedAlertPresentException as e:
                    self.driver.switch_to.alert.dismiss()
    sleep(2)


def addAsset(self):
    # 获取新增按钮属性
    self.driver.find_element_by_xpath("//div[@class='widget-body']/div[1]/button[1]").click()
    sleep(2)
    title = self.driver.find_element_by_xpath("//table[@id='editable-sample']/thead/tr/th").text
    try:
        assert title == '资产信息新增'
        print('成功进入资产新增页面')
    except Exception as e:
        print('未进入资产新增页面')
    # 填写资产信息
    self.driver.find_element_by_id("assetsInfo.assetsName").send_keys('test_selenium')
    self.driver.find_element_by_id("assetsInfo.assetsIp").send_keys('1.1.1.1')
    self.driver.find_element_by_id("assetsInfo.dataSrc").send_keys('test_selenium')
    radios = self.driver.find_elements_by_name("assetsInfo.useFlumeAgent")
    for radio in radios:
        if radio.get_attribute("value") == '01':
            radio.click()
    self.driver.find_element_by_id("assetsInfo.assetsKey").send_keys("test_selenium")
    js = "window.scrollTo(10000,10000);"
    self.driver.execute_script(js)
    self.driver.find_element_by_xpath("//div[@class='btn-group']/button[1]").click()
    sleep(2)
    self.driver.switch_to.alert.accept()


# @unittest.skip("直接跳过测试")
class assetAddtests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.url = "http://localhost:8080/lite/"
        userLogin.Login(cls.driver, cls.url)
        menu.assetMenu(cls.driver)
        sleep(2)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def setUp(self):
        checkboxs = self.driver.find_elements_by_xpath("//input[@class='checkboxes']")
        if len(checkboxs) > 1:
            ifexistAsset(self)


    def test_asset_web(self):
        """测试页面新增资产功能是否正常"""
        addAsset(self)
        assetnames = self.driver.find_elements_by_css_selector("#editable-sample>tbody>tr>a")
        for assetname in assetnames:
            self.assertIn('test_selenium', assetname.text)
            break
    '''       
    def test_asset_web_assetname_AA(self):
        self.driver.find_element_by_xpath("//div[@class='widget-body']/div[1]/button[1]").click()
        sleep(2)
        title = self.driver.find_element_by_xpath("//table[@id='editable-sample']/thead/tr/th").text
        try:
            assert title == '资产信息新增'
            print('成功进入资产新增页面')
        except Exception as e:
            print('未进入资产新增页面')
        # 填写资产信息
        self.driver.find_element_by_id("assetsInfo.assetsName").send_keys('AA')
        js = "window.scrollTo(10000,10000);"
        self.driver.execute_script(js)
        self.driver.find_element_by_xpath("//div[@class='btn-group']/button[1]").click()
     '''

# @unittest.skip("直接跳过测试")
class downTemplate(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.url = "http://localhost:8080/lite/"
        userLogin.Login(cls.driver, cls.url)
        menu.assetMenu(cls.driver)
        sleep(2)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

    def test_downTemplate(self):
        """测试下载模板功能是否正常"""
        self.driver.find_element_by_xpath("//div[@class='widget-body']/div[1]/button[6]").click()
        downpath = "C:\\Users\\xqq\Downloads"
        lists = os.listdir(downpath)
        self.assertIn('资产模板.xlsx', lists)

# @unittest.skip("直接跳过测试")
class assetImport(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.url = "http://localhost:8080/lite/"
        userLogin.Login(cls.driver, cls.url)
        menu.assetMenu(cls.driver)
        sleep(2)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

    def test_asset_import(self):
        """ 测试资产导入功能是否正常"""
        self.driver.find_element_by_xpath("//div[@class='widget-body']/div[1]/button[4]").click()
        filepath = "C:\\Users\\xqq\Downloads\资产模板.xlsx"
        self.driver.find_element_by_css_selector("input#dataFile.file").send_keys(filepath)
        self.driver.find_element_by_xpath("//*[@id='scriptDiv']/table/tbody/tr[2]/td/div/button[1]").click()
        sleep(1)
        self.driver.switch_to.alert.accept()
        # alert_title = self.driver.switch_to.alert.text
        sleep(2)
        try:
            self.driver.switch_to.alert.accept()
        except UnexpectedAlertPresentException as e:
            self.driver.switch_to.alert.dismiss()

class assetEdit(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.url = "http://localhost:8080/lite/"
        userLogin.Login(cls.driver, cls.url)
        menu.assetMenu(cls.driver)
        sleep(2)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

    def test_asset_Edit(self):
        """测试资产页面编辑功能是否正常"""
        checkboxs = self.driver.find_elements_by_xpath("//input[@class='checkboxes']")
        if len(checkboxs) > 1:
            parents = self.driver.find_elements_by_xpath("//table[@id='editable-sample']/tbody/tr")
            for parent in parents:
                sons = parent.find_elements_by_xpath("./td[2]")
                for son in sons:
                    if 'test_selenium' in son.text:
                        son.click()
                        # break
                        # break

        sleep(2)
        self.driver.find_element_by_id("assetsInfo.assetsName").send_keys('_edit')
        js = "window.scrollTo(10000,10000);"
        self.driver.execute_script(js)
        self.driver.find_element_by_xpath("//div[@class='btn-group']/button[1]").click()
        sleep(2)
        self.driver.switch_to.alert.accept()


        assetnames = self.driver.find_elements_by_css_selector("#editable-sample>tbody>tr>a")
        for assetname in assetnames:
            self.assertIn('edit', assetname.text)
            break


if __name__ == '__main__':
    # unittest.main()
    now_time = time.strftime("%Y-%m-%d %H_%M_%S")
    fp = open('../report/' + now_time + '.html', 'wb')
    testunit = unittest.TestSuite()
    testunit.addTest(assetAddtests("test_asset_web"))
    testunit.addTest(downTemplate("test_downTemplate"))
    testunit.addTest(assetImport("test_asset_import"))
    testunit.addTest(assetEdit("test_asset_Edit"))
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title="测试资产模块",
    )
    runner.run(testunit)
    fp.close()

