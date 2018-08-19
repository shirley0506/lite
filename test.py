from selenium import webdriver
from time import sleep
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# t = time.time()

driver = webdriver.Chrome()
driver.get("http://172.31.18.33")
driver.maximize_window()
driver.find_element_by_id("userId").send_keys("root")
driver.find_element_by_id("password").send_keys("root")
driver.find_element_by_id("verifyCode").send_keys("1234")
driver.find_element_by_class_name("icon-arrow-right").click()
sleep(2)
alert_login = driver.switch_to.alert
if alert_login.text in "你的密码已过期，请及时修改！":
    alert_login.accept()


driver.find_element_by_xpath("//img[@class='log-img']").click()
driver.find_element_by_css_selector(".icon-search").click()

#切换iframe
driver.switch_to.frame("showPage")

#定位到索引下拉框
indexN = driver.find_element_by_css_selector("#indexName0")

#遍历索引下拉框，选中tomcatlog01索引
indexOpts = indexN.find_elements_by_tag_name("option")

for indexOpt in indexOpts:
    # if indexOpt.text == "tomcatlog01":
    if indexOpt.text == "fivemillion":
        indexOpt.click()

#等待一秒，时间维度值出来
sleep(1)

#遍历时间维度下拉框，选中@timestap

tFld = driver.find_element_by_css_selector("#timeField0")
tOpts = tFld.find_elements_by_tag_name("option")

for topt in tOpts:
    # print(topt.text)
    if topt.text == "@timestamp":
        topt.click()

#遍历时间窗口，选中所有时间
#隐藏元素，调用js修改属性
js = "document.getElementById('Time0').style.display='block';"
driver.execute_script(js)
sleep(1)
fullTime = driver.find_element_by_css_selector("#Time0 > li:last-child")
# print(fullTime.find_element_by_tag_name("i").text)
fullTime.find_element_by_tag_name("i").click()
print("开始查询：%d" %(round(time.time()*1000)))

# driver.find_element_by_css_selector("#page0")

try:
    WebDriverWait(driver,10,0.05).until(
        EC.presence_of_element_located((By.CSS_SELECTOR,"#tbody0 > tr:nth-child(100)"))
    )
finally:
    print("查询结束：%d" %(round(time.time()*1000)))


