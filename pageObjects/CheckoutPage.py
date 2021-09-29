from selenium.webdriver.common.by import By

from pageObjects.ConfirmPage import ConfirmPage


class CheckoutPage:

    items = (By.XPATH, "//div[@class='card h-100']")
    checkoutbut = (By.CSS_SELECTOR, ".btn-primary")
    checkoutbut2 = (By.XPATH, "//button[@class='btn btn-success']")

    def __init__(self, driver):
        self.driver = driver

    def ShopItems(self):
        return self.driver.find_elements(*CheckoutPage.items)

    def checkoutbutton(self):
        return self.driver.find_element(*CheckoutPage.checkoutbut)

        # self.driver.find_element_by_css_selector(".btn-primary")

    def checkoutbutton2(self):
        self.driver.find_element(*CheckoutPage.checkoutbut2).click()
        confirmpage = ConfirmPage(self.driver)
        return confirmpage
