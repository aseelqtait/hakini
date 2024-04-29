from base_page import BasePage
from selenium.webdriver.common.by import By
class LoginPage(BasePage):
    Mylogin_link=(By.LINK_TEXT,"تسجيل الدخول")
    Email_FIELD=(By.XPATH, '/html/body/div[2]/div/div/div/div/div/form/div[1]/div[1]/div[1]/input')
     
    PASSWORD_FIELD=(By.CLASS_NAME,"password")
    CLICK_BUTTON=(By.XPATH,"/html/body/div[2]/div/div/div/div/div/form/div[1]/div[2]/button")
    error_message_locater=(By.XPATH,'/html/body/div[2]/div/div/div/div/div/form/div[1]/div[1]/div[1]/span')
    
    def enter_email(self,text):
        self.input_text(self.Email_FIELD,text)
    def enter_password(self,text):
        self.input_text(self.PASSWORD_FIELD,text)
    def click_login_button(self):
        self.click(self.CLICK_BUTTON)
    def get_the_text_error_message(self):
        message=self.find_locater_error_message(self.error_message_locater)
        return message.text
    def click_login_page(self):
        self.click(self.Mylogin_link)
 
 
