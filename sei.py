#%%
#from xml.dom.minidom import Element
from selenium import webdriver
from selenium.webdriver.support.ui import Select


#%%
driver = webdriver.Chrome('C:\chromedriver\chromedriver.exe')
driver.maximize_window()
driver.get("http://sbasu.pythonanywhere.com/tastyFoodApp")

element  = driver.find_element_by_link_text("Create New Profile")
element.click()
button = driver.find_element_by_id('js_button')
button.click()
alert = driver.switch_to_alert()
alert.accept()

firstName = driver.find_element_by_id('id firstName')
firstName.send_keys("Kia")
val1 = firstName.get_attribute('value')
print("The first name is",val1)
print("The url is",driver.current_url)
expected_val = ""














