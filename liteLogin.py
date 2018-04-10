from selenium import webdriver
from time import sleep
from selenium.common.exceptions import UnexpectedAlertPresentException

#登录
driver = webdriver.Chrome()
driver.maximize_window()
# driver.implicitly_wait(10)
driver.get("http://localhost:8080/lite/")
driver.find_element_by_id("userId").send_keys("root")
driver.find_element_by_id("password").send_keys("root")

driver.find_element_by_class_name("icon-arrow-right").click()
sleep(2)
#处理告警框
alert_login = driver.switch_to.alert
if alert_login.text in "你的密码已过期，请及时修改！":
    alert_login.accept()
#进入资产管理页面
driver.find_element_by_xpath("//img[@class='log-img']").click()
driver.find_element_by_link_text("资产").click()

#切换表单
sleep(2)
driver.switch_to.frame("showPage")

#新增之前处理--删除已存在的资产
father_css_selector = "#editable-sample>tbody>tr"
father_elements = driver.find_elements_by_css_selector(father_css_selector)
print(father_elements)
# for element in father_elements:
#     if element.text == 'test_selenium':
#         print(1)
# checkboxes = driver.find_elements_by_xpath("//input[@name='checkAssets' and @class='checkboxes']")
# print(checkboxes)
# for checkbox in checkboxes:
#     assets = driver.find_elements_by_css_selector("#editable-sample>tbody>tr>td>a")
#     for asset in assets:
#         if asset.text == 'test_selenium':
#             checkbox.click()

# driver.find_element_by_link_text("删除").click()
'''
driver.find_element_by_xpath("//div/div[1]/button[2]").click()
sleep(2)
driver.switch_to.alert.accept()

sleep(2)

try:
    driver.switch_to.alert.accept()
except UnexpectedAlertPresentException as e:
    driver.switch_to.alert.dismiss()

#新增资产

#获取新增按钮属性
sleep(2)
driver.find_element_by_xpath("//div[@class='widget-body']/div[1]/button[1]").click()
sleep(2)
title = driver.find_element_by_xpath("//table[@id='editable-sample']/thead/tr/th").text
try:
    assert title == '资产信息新增'
    print('成功进入资产新增页面')
except Exception as e:
    print('未进入资产新增页面')

#填写资产信息
driver.find_element_by_id("assetsInfo.assetsName").send_keys('test_selenium')
driver.find_element_by_id("assetsInfo.assetsIp").send_keys('1.1.1.1')
driver.find_element_by_id("assetsInfo.dataSrc").send_keys('test_selenium')
radios = driver.find_elements_by_name("assetsInfo.useFlumeAgent")
for radio in radios:
    if radio.get_attribute("value")=='01':
        radio.click()
driver.find_element_by_id("assetsInfo.assetsKey").send_keys("test_selenium")
js = "window.scrollTo(10000,10000);"
driver.execute_script(js)
driver.find_element_by_xpath("//div[@class='btn-group']/button[1]").click()
sleep(2)
driver.switch_to.alert.accept()
sleep(2)
assets = driver.find_elements_by_css_selector("#editable-sample>tbody>tr>td>a")

for asset in assets:
    if asset.text == 'test_selenium':
        print("新增资产成功")

'''















