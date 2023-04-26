from .base_page import BasePage
from .locators import RegLocators


class RegPage(BasePage):

    def __init__(self, driver, timeout=10):
        super().__init__(driver, timeout)
        self.firstname = driver.find_element(*RegLocators.REG_FIRSTNAME)
        self.lastname = driver.find_element(*RegLocators.REG_LASTNAME)
        self.region = driver.find_element(*RegLocators.REG_REGION)
        self.address = driver.find_element(*RegLocators.REG_ADDRESS)
        self.password = driver.find_element(*RegLocators.REG_PASSWORD)
        self.pass_confirm = driver.find_element(*RegLocators.REG_PASS_CONFIRM)
        self.btn = driver.find_element(*RegLocators.REG_REGISTER)

    def enter_firstname(self, value):
        self.firstname.send_keys(value)

    def enter_lastname(self, value):
        self.lastname.send_keys(value)

    def enter_region(self, value):
        self.region.send_keys(value)

    def enter_address(self, value):
        self.address.send_keys(value)

    def enter_password(self, value):
        self.password.send_keys(value)

    def enter_pass_conf(self, value):
        self.pass_confirm.send_keys(value)

    def btn_click_confirm(self):
        self.btn.click()
