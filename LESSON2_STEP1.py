from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/get_attribute.html"
browser = webdriver.Chrome('C:\Python26\Chromedriver')
browser.get(link)

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

x_element = browser.find_element_by_id("treasure")
x = x_element.get_attribute("valuex")
y = calc(x)

field = browser.find_element_by_id("answer").send_keys(y)
check = browser.find_element_by_id("robotCheckbox").click()
radio_button = browser.find_element_by_id("robotsRule").click()
submit = browser.find_element_by_css_selector(".btn.btn-default").click()

