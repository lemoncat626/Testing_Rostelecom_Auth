import pytest
from pages.reg_page import RegPage
from pages.auth_page import AuthPage
from selenium.webdriver.common.by import By
from settings import *

"""ATRT-020. Регистрация по валидным данным"""
@pytest.mark.positive
def test_reg_with_valid_data(browser):
    page1 = AuthPage(browser)
    page1.reg_click()
    page2 = RegPage(browser)
    page2.enter_firstname(valid_firstname)
    page2.enter_lastname(valid_lastname)
    page2.enter_region(valid_region)
    page2.enter_address(valid_address)
    page2.enter_password(valid_password)
    page2.enter_pass_conf(valid_password)
    page2.btn_click_confirm()
    assert browser.find_element(By.XPATH, "//h1[text()]").text == 'Подтверждение email'
