from selenium import webdriver
from myPublic import userLogin, menu
import os

driver = webdriver.Chrome()
driver.maximize_window()
url = "http://localhost:8080/lite/"
downpath = "C:\\Users\\xqq\Downloads"
# 登录系统
userLogin.Login(driver, url)
#进入资产页面
menu.assetMenu(driver)
driver.find_element_by_xpath("//div[@class='widget-body']/div[1]/button[6]").click()
lists = os.listdir(downpath)
for list in lists:
    if '资产模板' in list :
        print(list)
        print("下载模板成功")



