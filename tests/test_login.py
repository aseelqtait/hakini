from selenium.common import NoSuchElementException
from pages.login_page import LoginPage

def test_empty_email_and_password(driver):
    login_page = LoginPage(driver)
    login_page.click_login_page()
    login_page.enter_email(" ")
    login_page.enter_password(" ")
    login_page.click_login_button()
    assert "الرجاء ادخال كلمة المرور أو اسم المستخدم" in login_page.get_the_text_error_message()
def test_empty_email(driver):
    login_page = LoginPage(driver)
    login_page.click_login_page() 
    login_page.enter_email("")
    login_page.enter_password("")
    login_page.click_login_button()
    assert "الرجاء ادخال كلمة المرور أو اسم المستخدم" in login_page.get_the_text_error_message()


def test_empty_password(driver):
    login_page = LoginPage(driver)
    login_page.click_login_page()
    login_page.enter_email("qais4")
    login_page.enter_password("")
    login_page.click_login_button()
    assert  ".كلمة المرور مطلوب" in login_page.get_the_text_error_message()


def test_failed_email(driver):
    try:
        login_page = LoginPage(driver)
        login_page.click_login_page()
        login_page.enter_email("qq@aseel")
        login_page.enter_password("aseelQ@@1359")
        login_page.click_login_button()
        assert "الرجاء التأكد من اسم المستخدم" in login_page.get_the_text_error_message()
    except NoSuchElementException:
        return False


def test_Not_existing_email_registration(driver):
    login_page = LoginPage(driver)
    login_page.click_login_page()
    login_page.enter_email("sojoud@gmail.com")
    login_page.enter_password("sojoud981359")
    login_page.click_login_button()

    assert "الرجاء التأكد من  البريد الالكتروني" in login_page.get_the_text_error_message()
def test_incorrect_password(driver):
    login_page=LoginPage(driver)
    login_page.click_login_page()
    login_page.enter_email("rasha051092@gmail.com")
    login_page.enter_password("cgfby89")
    login_page.click_login_button()
    assert "كلمة المرور يجب أن يكون 8 خانات على الأقل" in login_page.get_the_text_error_message()

def test_success_login(driver):
    login_page=LoginPage(driver)
    login_page.click_login_page()
    login_page.enter_email("rasha051092@gmail.com")
    login_page.enter_password("rashtait766g@#")
    login_page.click_login_button()


