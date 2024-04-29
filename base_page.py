import time
import pytest
from selenium.common import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
    def click(self,locater):
        self.wait.until(EC.element_to_be_clickable(locater)).click()

    def is_element_present(self, locator):
        try:
            self.wait.until(EC.presence_of_element_located(locator))
            return True
        except NoSuchElementException:
            return False
    def input_text(self, locator, text):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(text)
    def find_locater_error_message(self,locator):
        error_message = self.wait.until(EC.presence_of_element_located(locator))
        return error_message

    #to finde the locater from email, username(strong field)
    def find_the_locater(self,locater):
        username=self.wait.until((EC.presence_of_element_located(locater)))
        return username
     