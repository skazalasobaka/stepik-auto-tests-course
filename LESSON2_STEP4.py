from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math

link = "http://suninjuly.github.io/explicit_wait2.html"
browser = webdriver.Chrome('C:\Python26\Chromedriver')
browser.get(link)

button1 = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.XPATH, '//*[@id="price"]'), "$100")
    )
button = browser.find_element_by_xpath('//*[@id="book"]').click()

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

x = browser.find_element_by_xpath('//*[@id="input_value"]').text
y = calc(x)

answer = browser.find_element_by_xpath('//*[@id="answer"]').send_keys(y)

submit2 = browser.find_element_by_xpath('/html/body/form/div/div/button').click()



