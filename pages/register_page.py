from selenium.webdriver.common.by import By
from base_page import BasePage
class RegisterPage(BasePage):
    MyAcount_link = (By.CSS_SELECTOR, "p.haveAccount a")
    username_FIELD=(By.CLASS_NAME, "username")  
    EMAIL_FIELD=(By.ID, "email")
    PASSWORD_FIELD=(By.ID, "password")
    phoneNumber_FIELD = (By.ID, "phoneField1")

    register_BUTTON=(By.ID, "register_button")
     
    error_message_locater=(By.CLASS_NAME,'invalid-feedback error_txts')

    def enter_userName(self,userName):
        self.input_text(self.username_FIELD,userName)
    def enter_email(self,email):
         self.input_text(self.EMAIL_FIELD,email)
    def enter_password(self,password):
        self.input_text(self.PASSWORD_FIELD,password)
    def enter_poneNumber(self,phoneNumber):
        self.input_text(self.phoneNumber_FIELD,phoneNumber)
    def handle_recaptcha_checkbox(self):
        try:
            wait = WebDriverWait(self.driver, 20)
            # Switch to the reCAPTCHA iframe
            wait.until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, "//iframe[@title='reCAPTCHA']")))
            # Click on the reCAPTCHA checkbox
            wait.until(EC.element_to_be_clickable((By.XPATH, "//span[@id='recaptcha-anchor']"))).click()
        except TimeoutException:
            print("reCAPTCHA checkbox container not found. Proceeding without clicking.")
             
    def click_register_button(self):
        self.click(self.register_BUTTON)

    def get_the_text_error_message(self):
       element= self.find_locater_error_message(self.error_message_locater)
       return element.text
   