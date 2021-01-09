from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input = browser.find_element_by_id("input_value")
    ans = calc(input.text)
    answer = browser.find_element_by_id("answer")
    answer.send_keys(ans)
    time.sleep(0.5)
    check = browser.find_element_by_id("robotCheckbox")
    check.click()
    time.sleep(0.5)
    radio = browser.find_element_by_id("robotsRule")
    browser.execute_script("arguments[0].scrollIntoView(true);", radio)
    radio.click()
    time.sleep(0.5)
    button = browser.find_element_by_css_selector("[type='submit']")
    browser.execute_script("arguments[0].scrollIntoView(true);", button)
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
