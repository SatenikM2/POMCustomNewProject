import time

from selenium import webdriver
import unittest
from Sourse.SignInPage import SignInPage
from Sourse.Navigation import NavigationBar
from Sourse.SearchResultPage import SearchResultPage
from Sourse.ProductDetailPage import ProductDetailsPage


class MyTest(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.delete_all_cookies()
        self.driver.get("https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_custrec_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&")
        self.signInPageObject = SignInPage(self.driver)
        self.navigationBarObj = NavigationBar(self.driver)
        self.searchRusultObj = SearchResultPage(self.driver)
        self.productDetailsObj = ProductDetailsPage(self.driver)


    def test_signIn(self):
        self.signInPageObject.fill_Login_Field("SatMartirosyan0@gmail.com")
        self.signInPageObject.click_to_continue_button()
        time.sleep(5)
        self.signInPageObject.fill_password_field("Sat454649")
        self.signInPageObject.click_to_sign_in_button()
        time.sleep(3)
        self.navigationBarObj.fill_search_field("bags for women")
        time.sleep(3)
        self.navigationBarObj.click_to_search_button()
        self.searchRusultObj.click_to_first_product()
        self.productDetailsObj.add_to_cart()




    def tearDown(self) -> None:
        self.driver.close()