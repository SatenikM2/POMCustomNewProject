from selenium.webdriver.common.by import By
from Sourse.BasPage import BasePage


class NavigationBarLocator():
    SearchFieldELemenetLocator = (By.ID, "twotabsearchtextbox")
    searchButtonlOcator = (By.ID, "nav-search-submit-button")
    clickCartButtonLocator = (By.XPATH, "//span[@class='nav-cart-count nav-cart-1 nav-progressive-attribute nav-progressive-content']")
    delFistProductLocator = (By.XPATH, "//input[@name='submit.delete.C78646001-76f6-4ad0-a08c-fa15143839ec']")
    homePageLocator = (By.XPATH, "//a[@class='nav-logo-link nav-progressive-attribute']")
    productsCartsDelLocator = (By.ID, "deselect-all")


class NavigationBar(NavigationBarLocator):
    def __init__(self,driver):
        self.driver = driver

    def fill_search_field(self,text):
        searchFieldElement = self.driver.find_element(*(self.SearchFieldELemenetLocator))
        searchFieldElement.clear()
        searchFieldElement.send_keys(text)


    def click_to_search_button(self):
        searchButtonElement = self.driver.find_element(*(self.searchButtonlOcator))
        searchButtonElement.click()


    def click_to_cart_button(self):
        clickCartButton = self.driver.find_element(*(self.clickCartButtonLocator))
        clickCartButton.click()

    def delete_first_product(self):
        delFirstProduct = self.driver.find_element(*(self.delFistProductLocator))
        delFirstProduct.click()

    def delete_all_products(self):
        productsCartsDel = self.driver.find_element(*(self.productsCartsDelLocator))
        productsCartsDel.click()

    def go_to_home_page(self):
        homePage = self.driver.find_element(*(self.homePageLocator))
        homePage.click()