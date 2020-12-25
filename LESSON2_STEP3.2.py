from selenium import webdriver
import math
import time

link = "http://suninjuly.github.io/redirect_accept.html"
browser = webdriver.Chrome('C:\Python26\Chromedriver')
browser.get(link)

button = browser.find_element_by_xpath("/html/body/form/div/div/button").click()

new_window = browser.window_handles[1]
browser.switch_to.window(new_window)

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

x = browser.find_element_by_xpath('//*[@id="input_value"]').text
y = calc(x)

answer = browser.find_element_by_xpath('//*[@id="answer"]').send_keys(y)

submit2 = browser.find_element_by_xpath('/html/body/form/div/div/button').click()