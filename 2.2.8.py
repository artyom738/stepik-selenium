from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import os

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_name("firstname")
    input1.send_keys("Ivan")
    time.sleep(0.5)
    input2 = browser.find_element_by_name("lastname")
    input2.send_keys("Petrov")
    time.sleep(0.5)
    input3 = browser.find_element_by_name("email")
    input3.send_keys("email")
    time.sleep(0.5)
    input4 = browser.find_element_by_id("file")
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'input.txt')
    input4.send_keys(file_path)
    time.sleep(0.5)
    button = browser.find_element_by_css_selector("[type='submit']")
    button.click()



finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
