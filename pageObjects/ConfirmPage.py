from selenium.webdriver.common.by import By


class ConfirmPage:

    cou = (By.ID, "country")
    selcou = (By.LINK_TEXT, "United States of America")

    def __init__(self, driver):
        self.driver = driver

    def Coun(self):
        return self.driver.find_element(*ConfirmPage.cou)
        # self.driver.find_element_by_id("country")

    def selcoun(self):
        return self.driver.find_element(*ConfirmPage.selcou)
