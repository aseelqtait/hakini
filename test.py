from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
import time

# Initialize WebDriver
driver = webdriver.Chrome()

# Open the homepage
driver.get("https://www.hakini.net")

# Find the list item element by class name using CSS selector
list_item = driver.find_element(By.CSS_SELECTOR, "li.last.login.font-family-samim-m")

# Find the anchor element within the list item
anchor_element = list_item.find_element(By.TAG_NAME, "a")

# Get the URL of the anchor element
login_url = anchor_element.get_attribute("href")
print("Login URL:", login_url)

# Click on the anchor element to navigate to the login page
anchor_element.click()

# Introduce a pause to observe the navigation
time.sleep(2)

# Find the <p> element with class "haveAccount" on the login page
have_account_element = driver.find_element(By.CLASS_NAME, "haveAccount")

# Find the <a> element within the <p> element
register_link = have_account_element.find_element(By.TAG_NAME, "a")

# Get the URL of the register link
register_url = register_link.get_attribute("href")
print("Register URL:", register_url)

# Click on the register link
register_link.click()

# Introduce a pause to observe the navigation
time.sleep(2)

# Fill in the form fields
username_input = driver.find_element(By.CLASS_NAME, "username")
username_input.send_keys("qais4")

email_input = driver.find_element(By.ID, "email")
email_input.send_keys("a.qutait1@student.aaup.edu")

password_input = driver.find_element(By.ID, "password")
password_input.send_keys("92000atait@@")

mobile_input = driver.find_element(By.ID, "phoneField1")
mobile_input.send_keys("599111000")
 

# Wait for the reCAPTCHA checkbox container to be clickable
try:
    wait = WebDriverWait(driver, 20)
    # below line switches into the IFRAME
    wait.until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, "//iframe[@title='reCAPTCHA']")))
    # below line will click on the checkbox next to 'I'm not a robot'
    wait.until(EC.element_to_be_clickable((By.XPATH, "//span[@id='recaptcha-anchor']"))).click()

 
except TimeoutException:
    print("reCAPTCHA checkbox container not found. Proceeding without clicking.")
 
# Introduce a pause to observe the checkbox container click
 
# Switch back to default content
driver.switch_to.default_content()

# Wait for the registration button to be clickable
# time.sleep(20)
try:
    register_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "register_button"))
    )
    # Click on the registration button
    register_button.click()
    print("CLICK BUTTON ")
except NoSuchElementException:
    print("Registration button not found. Exiting.")
time.sleep(37)

# Close the WebDriver
driver.quit()

