from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import os
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element_by_css_selector("[type='submit']")
    button.click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    input = browser.find_element_by_id("input_value")
    ans = calc(input.text)
    answer = browser.find_element_by_id("answer")
    answer.send_keys(ans)
    button = browser.find_element_by_css_selector("[type='submit']")
    button.click()



finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
