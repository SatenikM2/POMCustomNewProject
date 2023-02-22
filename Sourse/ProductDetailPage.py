from selenium.webdriver.common.by import By
from Sourse.BasPage import BasePage



class ProductDetailsLocator():
    addToCartLocator = (By.XPATH, "//input[@id='add-to-cart-button']")


class ProductDetailsPage(ProductDetailsLocator, BasePage):
    def __init__(self, driver):
        self.driver = driver

    def add_to_cart(self):
        productadd = self.driver.find_element(*(self.addToCartLocator))
        productadd.click()