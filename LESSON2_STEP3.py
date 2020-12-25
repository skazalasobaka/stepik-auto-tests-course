from selenium import webdriver
import math
import time

link = "http://suninjuly.github.io/alert_accept.html"
browser = webdriver.Chrome('C:\Python26\Chromedriver')
browser.get(link)

button = browser.find_element_by_xpath("/html/body/form/div/div/button").click()

confirm = browser.switch_to.alert
confirm.accept()

time.sleep(1)

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

x = browser.find_element_by_xpath('//*[@id="input_value"]').text
y = calc(x)

answer = browser.find_element_by_xpath('//*[@id="answer"]').send_keys(y)

submit2 = browser.find_element_by_xpath('/html/body/form/div/div/button').click()
