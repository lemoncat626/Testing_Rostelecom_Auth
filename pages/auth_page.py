from .base_page import BasePage
from .locators import AuthLocators


class AuthPage(BasePage):

    def __init__(self, driver, timeout=10):
        super().__init__(driver, timeout)
        url = "https://b2c.passport.rt.ru/"
        driver.get(url)
        self.username = driver.find_element(*AuthLocators.AUTH_USERNAME)
        self.password = driver.find_element(*AuthLocators.AUTH_PASS)
        self.btn = driver.find_element(*AuthLocators.AUTH_BTN)
        self.forgot_pass = driver.find_element(*AuthLocators.AUTH_FORGOT_PASS)
        self.registration = driver.find_element(*AuthLocators.AUTH_REG_IN)
        self.vk = driver.find_element(*AuthLocators.AUTH_VK)
        self.ok = driver.find_element(*AuthLocators.AUTH_OK)
        self.mail_ru = driver.find_element(*AuthLocators.AUTH_MAIL_RU)
        self.google = driver.find_element(*AuthLocators.AUTH_GOOGLE)
        self.yandex = driver.find_element(*AuthLocators.AUTH_YANDEX)

    def enter_username(self, value):
        self.username.send_keys(value)

    def enter_password(self, value):
        self.password.send_keys(value)

    def btn_click_confirm(self):
        self.btn.click()

    def forgot_pass_click(self):
        self.forgot_pass.click()

    def reg_click(self):
        self.registration.click()

    def auth_vk(self):
        self.vk.click()

    def auth_ok(self):
        self.ok.click()

    def auth_mail_ru(self):
        self.mail_ru.click()

    def auth_google(self):
        self.google.click()

    def auth_yandex(self):
        self.yandex.click()