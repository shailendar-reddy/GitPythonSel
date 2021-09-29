import inspect
import logging
import pytest
# import inspect
# import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select


@pytest.mark.usefixtures("setup")
class BaseClass:

    def getLogger(self):
        logername = inspect.stack()[1][3]
        logger = logging.getLogger(logername)
        filehandler = logging.FileHandler("logfile.log")
        formatter = logging.Formatter("%(asctime)s: %(levelname)s: %(name)s: %(message)s")
        filehandler.setFormatter(formatter)
        if logger.hasHandlers():
            logger.handlers.clear()
        logger.addHandler(filehandler)  # filehandler object
        logger.setLevel(logging.DEBUG)
        return logger

    def verifyLinkPresence(self, text):
        wait = WebDriverWait(self.driver, 7)
        # wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//div[@class='suggestions']/ul/li/a")))
        # countries = driver.find_elements_by_xpath("//div[@class='suggestions']/ul/li/a")
        # for country in countries:
        #     print(country.text)
        #     if country.text == "United States of America":
        #         country.click()
        #         break
        wait.until(EC.presence_of_element_located((By.LINK_TEXT, text)))

    @staticmethod
    def selectDropdown(locator, text):
        sel = Select(locator)
        sel.select_by_visible_text(text)



