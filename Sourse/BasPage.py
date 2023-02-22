from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class BasePage():
    def __init__(self,driver):
        self.driver = driver

    def find_element(self,by: By, value: str):
        try:
            element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((by, value)))

        except:
            print(f"Error 1:Element({by}, {value}) not visible")

        return element

    def git_title(self):
        return self.driver.title

    def wait_until_element_will_be_visibility(self):
        pass

    def screenshot():
        pass




