from selenium.webdriver.common.by import By

from pageObjects.CheckoutPage import CheckoutPage
from utilities.BaseClass import BaseClass


class HomePage(BaseClass):

    def __init__(self, driver, log):  # Constructor created to get the driver object from the object created in the test case
        self.driver = driver
        self.log = log

    shop = (By.XPATH, "//a[text()='Shop']")
    name = (By.CSS_SELECTOR, "input[name='name']")
    email = (By.XPATH, "//input[@name='email']")
    password = (By.XPATH, "//*[contains(@id,'exampleInput')]")
    checkbox = (By.ID, "exampleCheck1")
    gender = (By.ID, "exampleFormControlSelect1")
    submit = (By.CLASS_NAME, "btn-success")
    msg = (By.CSS_SELECTOR, "[class*='alert']")

    def homeshop(self):
        self.driver.find_element(*HomePage.shop).click()
        checkoutpage = CheckoutPage(self.driver)
        return checkoutpage
        # driver.find_element_by_xpath("//a[text()='Shop']")

    def getName(self, getData):

        self.log.info("first name is:"+getData["firstname"])
        self.driver.find_element(*HomePage.name).send_keys(getData["firstname"])
        self.driver.find_element(*HomePage.email).send_keys(getData["lastname"])
        self.driver.find_element(*HomePage.password).send_keys("password")
        self.driver.find_element(*HomePage.checkbox).click()
        dropdown = self.driver.find_element(*HomePage.gender)
        self.selectDropdown(dropdown, getData["Gender"])
        self.driver.find_element(*HomePage.submit).click()
        return self.driver.find_element(*HomePage.msg).text
