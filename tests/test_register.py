import pytest
from selenium.common import NoSuchElementException
from selenium import webdriver
from pages.register_page import RegisterPage
   
@pytest.fixture(scope="function", autouse=True)
def open_signup_page():
    driver=webdriver.Chrome()
    driver.get("https://www.hakini.net/signup")
    yield driver
    driver.quit()
   
def test_successful_register(driver, open_signup_page):
    register_page = RegisterPage(driver)
    register_page.enter_userName("gcfr")
    register_page.enter_email("w@gmail.com")
    register_page.enter_password("gftrebch")
    register_page.enter_poneNumber("599111000")
    register_page.handle_recaptcha_checkbox()
    register_page.click_register_button()

 
def test_failed_email(driver, open_signup_page):
        try:
            register_page = registerPage(driver)
            register_page.click_MyAcount_page()
            register_page.enter_email("qq@aseel")
            register_page.enter_password("aseelQ@@1359")
            register_page.click_register_button()
            assert "Please provide a valid email address." in register_page.get_the_text_error_message()
        except NoSuchElementException:
            return False
def test_existing_email(driver, open_signup_page):
    register_page = registerPage(driver)
    register_page.click_MyAcount_page()
    register_page.enter_email("aseelqtait@gmail.com")
    register_page.enter_password("aseelqtait1359")
    register_page.click_register_button()
    assert "An account is already registered with your email address. Please log in." in register_page.get_the_text_error_message()


def test_empty(driver, open_signup_page):
    register_page = registerPage(driver)
    register_page.click_MyAcount_page()
    register_page.enter_email("")
    register_page.enter_password("")
    register_page.click_register_button()
    assert "Please provide a valid email address" in register_page.get_the_text_error_message()


def test_weak_password(driver, open_signup_page):
    register_page = registerPage(driver)
    register_page.click_MyAcount_page()
    register_page.enter_email("yafaaaq92000@gmail.com")
    register_page.enter_password("13565")
    register_page.click_register_button()
    assert "weak - please enter a stronger password." == register_page.get_the_text_error_message()


def test_successful_registration(driver, open_signup_page):
    register_page = registerPage(driver)
    register_page.click_MyAcount_page()
    register_page.enter_email("rash05176092@gmail.com")
    actual_email=register_page.get_email()
    register_page.enter_password("rashtait766g@#")
    register_page.click_register_button()
    expected_username = register_page.get_the_username_locater()
    actual_username = actual_email.split('@')[0]
    assert expected_username == actual_username, "not matching"



