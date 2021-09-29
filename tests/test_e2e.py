import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pageObjects.CheckoutPage import CheckoutPage
from pageObjects.ConfirmPage import ConfirmPage
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestOne(BaseClass):

    def test_e2e(self):
        log = self.getLogger()
        prodSelected = []
        cartItems = []
        self.driver.implicitly_wait(5)
        homepage = HomePage(self.driver, log)  #this object is used to send the driver object to the actual page object file
        checkoutpage = homepage.homeshop()
        log.info("All phone cards")
        products = checkoutpage.ShopItems()
        for product in products:
            productName = product.find_element_by_xpath("div/h4/a").text
            log.info(productName)
            if productName == "Nokia Edge":
                time.sleep(3)
                prodSelected.append(productName)
                product.find_element_by_xpath("div[2]/button").click()

        checkoutpage.checkoutbutton().click()

        cartItems.append(self.driver.find_element_by_css_selector("h4[class='media-heading'] a").text)
        assert prodSelected == cartItems

        confirmpage = checkoutpage.checkoutbutton2()
        confirmpage.Coun().send_keys("un")
        # self.driver.find_element_by_id("country").send_keys("un")
        self.verifyLinkPresence("United States of America")
        confirmpage.selcoun().click()
        # self.driver.find_element_by_link_text("United States of America").click()

        self.driver.find_element_by_css_selector(".btn-success").click()

        message = self.driver.find_element_by_xpath("//div[@class='alert alert-success alert-dismissible']").text
        assert "Successful!" in message

        self.driver.get_screenshot_as_file("success.png")