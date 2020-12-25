from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/execute_script.html"
browser = webdriver.Chrome('C:\Python26\Chromedriver')
browser.get(link)


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


x_element = browser.find_element_by_id("input_value")
x = x_element.text
y = calc(x)

field = browser.find_element_by_id("answer").send_keys(y)
check = browser.find_element_by_id("robotCheckbox").click()
radio_button = browser.find_element_by_id("robotsRule")
browser.execute_script("return arguments[0].scrollIntoView(true);", radio_button)
radio_button.click()
submit = browser.find_element_by_css_selector(".btn.btn-primary").click()
