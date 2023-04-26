from .base_page import BasePage
from .locators import PassRecLocators


class PassRecPage(BasePage):

    def __init__(self, driver, timeout=10):
        super().__init__(driver, timeout)
        url = "https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/reset-credentials"
        driver.get(url)
        self.username = driver.find_element(*PassRecLocators.PASS_REC_USERNAME)
        self.btn_reset = driver.find_element(*PassRecLocators.PASS_REC_BTN_RESET)
        self.btn_back = driver.find_element(*PassRecLocators.PASS_REC_BTN_BACK)

    def enter_username(self, value):
        self.username.send_keys(value)

    def btn_click_reset(self):
        self.btn_reset.click()

    def btn_click_back(self):
        self.btn_back.click()
