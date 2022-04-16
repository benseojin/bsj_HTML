
#%%
from datetime import date
import time
from xml.dom.minidom import Element
import pyautogui
from selenium import webdriver
from selenium.webdriver.support.ui import Select
driver = webdriver.Chrome('C:\chromedriver\chromedriver.exe')
driver.maximize_window()
driver.get("https://hcs.eduro.go.kr/#/loginHome")

#%%
click_start_1 = driver.find_element_by_id("btnConfirm2")
click_start_1.click()
click_start_2 = driver.find_element_by_class_name("searchBtn")
click_start_2.click()
click_start_3 = driver.find_element_by_id("sidolabel")
click_start_3.click()

seojon_id = Select(driver.find_element_by_id('sidolabel'))
seojon_id.select_by_index(8)
time.sleep(1)
school_find = Select(driver.find_element_by_id('crseScCode'))
school_find.select_by_visible_text('중학교')
shool_name_ele = driver.find_element_by_id('orgname')
shool_name_ele.click()

#%%
shool_name_ele.send_keys('도담중학교')
Ser_ele = driver.find_elements_by_class_name('searchBtn')

#%%
lv_1_end = driver.find_element_by_class_name('layerFullBtn')
lv_1_end.click()


# %%

# %%

