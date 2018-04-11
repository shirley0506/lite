from time import sleep

def assetMenu(driver):
    driver.find_element_by_xpath("//img[@class='log-img']").click()
    driver.find_element_by_link_text("资产").click()
    sleep(2)
    driver.switch_to.frame("showPage")
