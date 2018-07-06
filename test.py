from selenium import webdriver
from time import sleep


def ifexistAsset(driver):
    # 通过定位父元素，操作子元素，操作兄弟元素
    # 定位到一组元素，非标题栏
    parents = driver.find_elements_by_xpath("//table[@id='editable-sample']/tbody/tr")

    for parent in parents:
        # `.`代表当前节点，`..`代表父节点
        sons = parent.find_elements_by_xpath("./td[2]/a")  # 串联查找 定位到一组资产名称的元素
        for son in sons:
            if 'test_selenium' in son.text:  # 判断test_selenium在不在数组中
                el = son
                break  # 拿到删除的资产，退出整个循环

    el.find_element_by_xpath("../../td[1]/input[@name='checkAssets']").click()  # 返回到复选框，并选中
    sleep(2)
    driver.find_element_by_xpath("//div[@class='span12']/div[1]/div[2]/button[2]").click()
    sleep(2)
    driver.switch_to.alert.accept()
    sleep(2)
    try:
        driver.switch_to.alert.accept()
    except UnexpectedAlertPresentException as e:
        driver.switch_to.alert.dismiss()
    sleep(2)

def addAsset(driver):
    # 获取新增按钮属性
    driver.find_element_by_xpath("//div[@class='span12']/div[1]/div[2]/button[1]").click()
    sleep(2)
    title = driver.find_element_by_xpath("//*[@id='editable-sample']/thead/tr/th").text
    try:
        assert title == '资产信息新增'
        print('成功进入资产新增页面')
    except Exception as e:
        print('未进入资产新增页面')
    # 填写资产信息
    driver.find_element_by_id("assetsInfo.assetsName").send_keys('test_selenium')
    driver.find_element_by_id("assetsInfo.assetsIp").send_keys('1.1.1.1')
    driver.find_element_by_id("assetsInfo.dataSrc").send_keys('test_selenium')
    js = "window.scrollTo(10000,10000);"
    driver.execute_script(js)
    # 单选框 是否使用flume
    radios = driver.find_elements_by_name("assetsInfo.useFlumeAgent")
    for radio in radios:

        if radio.get_attribute("value") == '01':
            radio.click()
            break

    driver.find_element_by_id("assetsInfo.assetsKey").send_keys("test_selenium")
    driver.find_element_by_xpath("//*[@id='editable-sample']/tbody/tr[10]/td/div/button[1]").click()
    sleep(2)
    driver.switch_to.alert.accept()

if __name__ == '__main__':

    driver = webdriver.Chrome()
    url = 'http://localhost:8080/lite'
    driver.get(url)
    driver.maximize_window()

    driver.find_element_by_id("userId").send_keys("root")
    driver.find_element_by_id("password").send_keys("root")
    driver.find_element_by_id("verifyCode").send_keys("1234")
    driver.find_element_by_class_name("icon-arrow-right").click()

    sleep(2)
    alert_login = driver.switch_to.alert
    if alert_login.text in "你的密码已过期，请及时修改！":
        alert_login.accept()

    #
    # '''
    # 新建资产流程
    # '''
    # driver.find_element_by_xpath("//img[@class='log-img']").click()
    # driver.find_element_by_link_text("系统").click()
    # driver.find_element_by_link_text("资产管理").click()
    # sleep(2)
    # driver.switch_to.frame("showPage")
    # checkboxs = driver.find_elements_by_xpath("//input[@class='checkboxes']")
    # if len(checkboxs) > 1:
    #     ifexistAsset(driver)
    # addAsset(driver)
    #
    '''
    进入到新建协议流程
    '''
    #退出到上一级页面
    driver.switch_to.default_content()
    #点击进入协议页面
    driver.find_element_by_xpath("//img[@class='log-img']").click()
    driver.find_element_by_link_text("采集").click()
    driver.find_element_by_link_text("协议").click()
    driver.switch_to.frame("showPage")
    #协议页面点击新增按钮
    driver.find_element_by_xpath("/html/body/div[3]/div/div/div/div[2]/button[1]").click()

    '''
    进入协议第一步
    '''
    sname_selects = driver.find_elements_by_xpath("//select[@id='dataSource.name']/option")  #获取数据源ID下拉框所有值
    for sname in sname_selects:
        if 'test_selenium' == sname.text:
            sname.click()    #选中test_selenium数据源ID
            break
    driver.find_element_by_xpath("//*[@id='dataSource_analysisRule']/option[2]").click()
    driver.find_element_by_xpath("//*[@id='dataSource.protocolType']/option[2]").click()
    driver.find_element_by_xpath("//*[@id='editable-sample']/tbody/tr[6]/td/div/button[2]").click()
    driver.find_element_by_xpath("//*[@id='editable-sample']/tbody/tr[1]/td[2]/p[1]/input").click()
    '''
    进入第二步
    '''
    #选择多行合并单行，并输入切片正则
    driver.find_element_by_xpath("//*[@id='editable-sample']/tbody/tr[1]/td[2]/p[1]/input").click()
    driver.find_element_by_id("ptb_regExp").send_keys("^\d{4}")
    driver.find_element_by_xpath("//*[@id='editable-sample']/tbody/tr[6]/td/div/button[2]").click()
    '''
    进入第三步
    输入一条常规时间的解析正则
    '''
    driver.find_element_by_xpath("//*[@id='add-del-btn']/button[1]").click()
    driver.find_element_by_xpath("//*[@id='regVal']").send_keys("(?<date>[\d\-]{10})")
    driver.find_element_by_xpath("/html/body/div[3]/div/div/div/div[3]/button[2]").click()
    '''
    进入第四步
    新建协议，并指定索引名为test_selenium,date类型为date
    '''
    driver.find_element_by_xpath("//*[@id='newMle']").click()
    driver.find_element_by_xpath("//*[@id='newSearch']").send_keys("test_selenium")
    driver.find_element_by_xpath("//*[@id='customStrategyTbody']/tr/td[3]/select/option[3]").click()
    js = "window.scrollTo(10000,10000);"
    driver.execute_script(js)
    driver.find_element_by_id("toggleBtn").click()   #修改字段类型
    #修改切片数
    js = "window.scrollTo(10000,10000);"
    driver.execute_script(js)
    driver.find_element_by_xpath("//*[@id='paramTable']/tbody/tr[1]/td[2]/input").clear()
    driver.find_element_by_xpath("//*[@id='paramTable']/tbody/tr[1]/td[2]/input").send_keys("2")
    driver.find_element_by_id("toggleBtn").click()
    driver.find_element_by_xpath("/html/body/div[3]/div/div/div/div[3]/button[2]").click()

    #启动协议
    driver.find_element_by_xpath("//*[@id='main']/tr/td[6]/span/b[1]").click()











