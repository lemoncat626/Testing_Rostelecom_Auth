import pytest
from pages.auth_page import AuthPage
from selenium.webdriver.common.by import By
from settings import *


"""ATRT-001. Авторизация по валидному номеру телефону/паролю"""
@pytest.mark.positive
def test_auth_with_valid_number(browser):
    page = AuthPage(browser)
    page.enter_username(valid_number)
    page.enter_password(valid_password)
    page.btn_click_confirm()
    assert browser.find_element(By.ID, 'logout-btn')


"""ATRT-002. Авторизация по валидной почте/паролю"""
@pytest.mark.positive
def test_auth_with_valid_email(browser):
    page = AuthPage(browser)
    page.enter_username(valid_email)
    page.enter_password(valid_password)
    page.btn_click_confirm()
    assert browser.find_element(By.ID, 'logout-btn')


"""ATRT-003. Авторизация по валидному логину/паролю"""
@pytest.mark.positive
def test_auth_with_valid_login(browser):
    page = AuthPage(browser)
    page.enter_username(valid_login)
    page.enter_password(valid_password)
    page.btn_click_confirm()
    assert browser.find_element(By.ID, 'logout-btn')


"""ATRT-004. Авторизация по валидному лицевому счету/паролю"""
@pytest.mark.positive
def test_auth_with_valid_personal_account(browser):
    page = AuthPage(browser)
    page.enter_username(valid_personal_account)
    page.enter_password(valid_password)
    page.btn_click_confirm()
    assert browser.find_element(By.ID, 'logout-btn')


"""ATRT-005. Авторизация по невалидному значению username"""
@pytest.mark.negative
def test_auth_with_invalid_username(browser):
    page = AuthPage(browser)
    page.enter_username(invalid_email)
    page.enter_password(valid_password)
    page.btn_click_confirm()
    assert browser.find_element(By.ID, 'form-error-message')


"""ATRT-006. Авторизация по невалидному паролю"""
@pytest.mark.negative
def test_auth_with_invalid_password(browser):
    page = AuthPage(browser)
    page.enter_username(valid_email)
    page.enter_password(invalid_password)
    page.btn_click_confirm()
    assert browser.find_element(By.ID, 'form-error-message')


"""ATRT-007. Авторизация с пустым полем username"""
@pytest.mark.negative
def test_auth_without_username(browser):
    page = AuthPage(browser)
    page.enter_username('')
    page.enter_password(valid_password)
    page.btn_click_confirm()
    assert browser.find_element(By.XPATH, "//span[@class='rt-input-container__meta rt-input-container__meta--error']")


"""ATRT-008. Авторизация с пустым полем пароля"""
@pytest.mark.negative
def test_auth_without_password(browser):
    page = AuthPage(browser)
    page.enter_username(valid_email)
    page.enter_password('')
    page.btn_click_confirm()
    assert browser.find_element(By.XPATH, '//*[@id="page-right"]/div[1]/div[1]/h1[1]')


"""ATRT-009. Переход на страницу восстановления пароля"""
@pytest.mark.positive
def test_open_pass_recovery_page(browser):
    page = AuthPage(browser)
    page.forgot_pass_click()
    assert browser.find_element(By.XPATH, "//h1[text()]").text == 'Восстановление пароля'


"""ATRT-010. Авторизация через Вконтакте"""
@pytest.mark.positive
def test_auth_with_vk(browser):
    page = AuthPage(browser)
    page.auth_vk()
    assert 'vk' in browser.current_url


"""ATRT-011. Авторизация через Одноклассники"""
@pytest.mark.positive
def test_auth_with_vk(browser):
    page = AuthPage(browser)
    page.auth_ok()
    assert 'ok' in browser.current_url


"""ATRT-012. Авторизация через Мэйл Ру"""
@pytest.mark.positive
def test_auth_with_vk(browser):
    page = AuthPage(browser)
    page.auth_mail_ru()
    assert 'mail' in browser.current_url


"""ATRT-013. Авторизация через Гугл"""
@pytest.mark.positive
def test_auth_with_vk(browser):
    page = AuthPage(browser)
    page.auth_google()
    assert 'google' in browser.current_url


"""ATRT-014. Авторизация через Яндекс"""
@pytest.mark.positive
def test_auth_with_vk(browser):
    page = AuthPage(browser)
    page.auth_yandex()
    assert 'yandex' in browser.current_url