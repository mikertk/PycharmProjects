# coding=utf-8
from selenium import webdriver

import time

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
time.sleep(2)
title1 = driver.title
print title1
driver.find_element_by_xpath(".//*[@id='u1']/a[7]").click()
time.sleep(2)


# driver.quit()
