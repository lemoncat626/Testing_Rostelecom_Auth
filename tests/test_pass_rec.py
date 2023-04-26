import pytest
import time
from pages.pass_recovery_page import PassRecPage
from selenium.webdriver.common.by import By
from settings import *

"""ATRT-015. Восстановление пароля по невалидному номеру телефона"""
@pytest.mark.negative
def test_pass_rec_with_invalid_phone(browser):
    page = PassRecPage(browser)
    page.enter_username(invalid_phone)
    time.sleep(30) #для ввода капчи
    page.btn_click_reset()
    assert browser.find_element(By.ID, 'form-error-message')


"""ATRT-016. Восстановление пароля по невалидному email"""
@pytest.mark.negative
def test_pass_rec_with_invalid_email(browser):
    page = PassRecPage(browser)
    page.enter_username(invalid_email)
    time.sleep(30) #для ввода капчи
    page.btn_click_reset()
    assert browser.find_element(By.ID, 'form-error-message')


"""ATRT-017. Восстановление пароля по невалидному логину"""
@pytest.mark.negative
def test_pass_rec_with_invalid_login(browser):
    page = PassRecPage(browser)
    page.enter_username(invalid_login)
    time.sleep(30) #для ввода капчи
    page.btn_click_reset()
    assert browser.find_element(By.ID, 'form-error-message')


"""ATRT-018. Восстановление пароля по невалидному значению лицевого счета"""
@pytest.mark.negative
def test_pass_rec_with_invalid_personal_account(browser):
    page = PassRecPage(browser)
    page.enter_username(invalid_personal_account)
    time.sleep(30) #для ввода капчи
    page.btn_click_reset()
    assert browser.find_element(By.ID, 'form-error-message')


"""ATRT-019. Возвращение на страницу авторизации"""
@pytest.mark.positive
def test_back_to_auth_page(browser):
    page = PassRecPage(browser)
    page.btn_click_back()
    assert browser.find_element(By.XPATH, "//h1[text()]").text == 'Авторизация'