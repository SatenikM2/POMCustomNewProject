from selenium.webdriver.common.by import By
from Sourse.BasPage import BasePage


class SerachResultPageLocator():
    firstProductLocator = (By.XPATH, "((//img[@class='s-image'])[1])")


class SearchResultPage(SerachResultPageLocator, BasePage):
    def __init__(self, driver):
        self.driver = driver

    def click_to_first_product(self):
        firstProductElement = self.driver.find_element(*(self.firstProductLocator))
        firstProductElement.click()