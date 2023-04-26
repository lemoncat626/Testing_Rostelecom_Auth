from selenium.webdriver.common.by import By


class AuthLocators:
    AUTH_USERNAME = (By.ID, "username")
    AUTH_PASS = (By.ID, "password")
    AUTH_BTN = (By.ID, "kc-login")
    AUTH_FORGOT_PASS = (By.ID, 'forgot_password')
    AUTH_REG_IN = (By.ID, "kc-register")
    AUTH_VK = (By.ID, 'oidc_vk')
    AUTH_OK = (By.ID, 'oidc_ok')
    AUTH_MAIL_RU = (By.ID, 'oidc_mail')
    AUTH_GOOGLE = (By.ID, 'oidc_google')
    AUTH_YANDEX = (By.ID, 'oidc_ya')


class PassRecLocators:
    PASS_REC_USERNAME = (By.ID, "username")
    PASS_REC_BTN_RESET = (By.ID, "reset")
    PASS_REC_BTN_BACK = (By.ID, "reset-back")


class RegLocators:
    REG_FIRSTNAME = (By.XPATH, "//input[@name='firstName']")
    REG_LASTNAME = (By.XPATH, "//input[@name='lastName']")
    REG_REGION = (By.XPATH, "//input[@autocomplete='new-password']"[0])
    REG_ADDRESS = (By.ID, 'address')
    REG_PASSWORD = (By.ID, 'password')
    REG_PASS_CONFIRM = (By.XPATH, "//input[@id='password-confirm']")
    REG_REGISTER = (By.XPATH, "//button[@name='register']")
