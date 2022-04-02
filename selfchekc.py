
from xml.dom.minidom import Element
import pyautogui
from selenium import webdriver
from selenium.webdriver.support.ui import Select
driver = webdriver.Chrome('C:\chromedriver\chromedriver.exe')
driver.maximize_window()
driver.get("https://hcs.eduro.go.kr/#/loginHome")
click_start_1 = driver.find_element_by_id("btnConfirm2")
click_start_1.click()
click_start_2 = driver.find_element_by_class_name("searchBtn")
click_start_2.click()