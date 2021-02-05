import unittest
import pytest
from selenium import webdriver
import time

class Test():
    def send_form(link):
        browser = webdriver.Chrome()
        browser.get(link)
        input1 = browser.find_element_by_css_selector('div.first_block > div.form-group.first_class > input')
        input1.send_keys("Ivan")
        time.sleep(0.4)
        input1 = browser.find_element_by_css_selector('div.first_block > div.form-group.second_class > input')
        input1.send_keys("Ivanov")
        time.sleep(0.4)
        input1 = browser.find_element_by_css_selector('div.first_block > div.form-group.third_class > input')
        input1.send_keys("Ivanovsk")
        time.sleep(0.4)
        button = browser.find_element_by_css_selector("button.btn")
        button.click()
        time.sleep(1)

        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text
        browser.quit()
        return welcome_text


    def test_reg1():
        link = "http://suninjuly.github.io/registration1.html"
        welcome_text = send_form(link)
        assert welcome_text == "Congratulations! You have successfully registered!", "Error of registration"

    def test_reg2():
        link = "http://suninjuly.github.io/registration2.html"
        welcome_text = send_form(link)
        assert welcome_text == "Congratulations! You have successfully registered!", "Error of registration"
    def shutdown():
        time.sleep(3)
        browser.quit()

pytest.main()
