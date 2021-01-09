from selenium import webdriver
import time
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)
    treasure = browser.find_element_by_id("treasure")
    x = treasure.get_attribute("valuex")


    y = calc(x)
    input = browser.find_element_by_id("answer")
    input.send_keys(y)
    time.sleep(0.5)
    option1 = browser.find_element_by_id("robotCheckbox")
    option1.click()
    time.sleep(0.5)
    option2 = browser.find_element_by_id("robotsRule")
    option2.click()
    time.sleep(0.5)
    button = browser.find_element_by_css_selector("[type='submit']")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
