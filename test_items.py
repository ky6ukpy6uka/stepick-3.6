import pytest
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec


link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

#check exist button
def test_guest_should_see_button(browser):
    browser.get(link)
    time.sleep(5)
    button = browser.find_element_by_css_selector(".btn-add-to-basket")
    ec.presence_of_element_located(browser.find_element_by_css_selector(".btn-add-to-basket"))
