from time import sleep

def assetMenu(driver):
    driver.find_element_by_xpath("//img[@class='log-img']").click()
    # driver.find_element_by_xpath("//li[6][@class='sub_menu']").click()
    driver.find_element_by_link_text("系统").click()
    driver.find_element_by_link_text("资产管理").click()
    sleep(2)
    driver.switch_to.frame("showPage")
