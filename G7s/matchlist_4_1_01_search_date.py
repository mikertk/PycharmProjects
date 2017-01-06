# coding=utf-8
import commen
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time
import datetime

# 进入匹配列表
dr = commen.login("admin_TK1", 'Admin@11', 'http://g7s.huoyunren.com/#map/matchlist/index.html')

dr = webdriver.firefox()



# dr.find_element_by_id("export").click().clear()
