from selenium.webdriver.common.by import By
from Sourse.BasPage import BasePage

class SignInPageLocator():
    loginFieldElementLocator = (By.ID, "ap_email")
    continueButtonLocator = (By.ID, "continue")
    passwordFieldElementLocator = (By.ID, "ap_password")
    clickSignInButttonLocator = (By.ID, "signInSubmit")


class SignInPage(SignInPageLocator, BasePage):
    def __init__(self, driver):
        self.driver = driver


    def fill_Login_Field(self, username):
        loginFieldElement = self.driver.find_element(*(self.loginFieldElementLocator))
        loginFieldElement.clear()
        loginFieldElement.send_keys(username)

    def click_to_continue_button(self):
        continueButtonElement = self.driver.find_element(*(self.continueButtonLocator))
        continueButtonElement.click()

    def fill_password_field(self, password):
        passewdFieldElement = self.driver.find_element(*(self.passwordFieldElementLocator))
        passewdFieldElement.clear()
        passewdFieldElement.send_keys(password)

    def click_to_sign_in_button(self):
        signInButtonElement = self.driver.find_element(*(self.clickSignInButttonLocator))
        signInButtonElement.click()












