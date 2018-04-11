from time import sleep

def Login(driver, url):
    driver.get(url)
    driver.find_element_by_id("userId").send_keys("root")
    driver.find_element_by_id("password").send_keys("root")
    driver.find_element_by_class_name("icon-arrow-right").click()
    sleep(2)
    alert_login = driver.switch_to.alert
    if alert_login.text in "你的密码已过期，请及时修改！":
        alert_login.accept()


