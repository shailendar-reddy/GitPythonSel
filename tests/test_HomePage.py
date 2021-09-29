import time
import pytest
from selenium import webdriver
from selenium.webdriver.support.select import Select
from TestData.HomePageData import HomePageData
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):
    def test_formSubmission(self, getData):
        log = self.getLogger()
        homepage = HomePage(self.driver, log)
        # self.driver.find_element_by_css_selector("input[name='name']").send_keys("krithi")
        # Self.driver.find_element_by_xpath("").send_keys("krithi_shetty23@gmail.com")
        #  regular expressions for Xpath: [contains(@attribute,'value')]
        # driver.find_element_by_xpath("//*[contains(@id,'exampleInput')]").send_keys("password")
        # driver.find_element_by_id("exampleCheck1").click()
        # select class provide the methods to handle the options in dropdown
        # dropdown = Select(driver.find_element_by_id("exampleFormControlSelect1"))
        # dropdown.select_by_index(1)
        # time.sleep(2)
        # dropdown.select_by_visible_text("Male")
        # driver.find_element_by_class_name("btn-success").click()
        message = homepage.getName(getData)
        time.sleep(3)
        assert "Success" in message
        self.driver.refresh()

    @pytest.fixture(params=HomePageData.getTestData("Testcase2"))
    def getData(self, request):
        return request.param

#  full relative css "div[class='alert alert-success alert-dismissible']"
# Using regular expression css syntax: [attribute*='value'] Tagname is optional