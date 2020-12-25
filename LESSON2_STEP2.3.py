from selenium import webdriver
import os

link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome('C:\Python26\Chromedriver')
browser.get(link)

current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'file.txt')

first_name = browser.find_element_by_xpath('/html/body/div/form/div/input[1]').send_keys('xyu')
last_name = browser.find_element_by_xpath('/html/body/div/form/div/input[2]').send_keys('xyu')
email = browser.find_element_by_xpath("/html/body/div/form/div/input[3]").send_keys('xyu')

chose_file = browser.find_element_by_xpath('//*[@id="file"]').send_keys(file_path)

submit = browser.find_element_by_xpath("/html/body/div/form/button").click()