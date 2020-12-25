from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math

link = "http://suninjuly.github.io/selects2.html"
browser = webdriver.Chrome('C:\Python26\Chromedriver')
browser.get(link)

a = int(browser.find_element_by_id("num1").text)
b = int(browser.find_element_by_id("num2").text)

x = a + b

select = Select(browser.find_element_by_tag_name("select"))
select.select_by_value(str(x))

submit = browser.find_element_by_css_selector(".btn.btn-default").click()
