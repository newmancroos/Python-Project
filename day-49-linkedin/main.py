from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
url="https://www.linkedin.com/jobs/search/?currentJobId=4261882909&f_AL=true&keywords=python%20developer&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true"

chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach", True)

driver = webdriver.Chrome(chrome_option)
driver.get(url)

# # Click Reject Cookies Button
# time.sleep(2)
# reject_button = driver.find_element(by=By.CSS_SELECTOR, value='button[action-type="DENY"]')
# reject_button.click()

# Click Sign in Button
# time.sleep(2)

singin_button = driver.find_element(By.CLASS_NAME, value="sign-in-modal__outlet-btn")
singin_button.send_keys(Keys.ENTER)

# sign_in_button = driver.find_element(by=By.LINK_TEXT, value="Sign in")
# sign_in_button.click()

# # Click Sign in Button
# time.sleep(2)

emailtextbox=driver.find_element(By.ID,value="base-sign-in-modal_session_key")
emailtextbox.send_keys("croosnewman@gmail.com")

passwordtextbox=driver.find_element(By.ID,value="base-sign-in-modal_session_password")
passwordtextbox.send_keys("Selvasri_0812")

loginbutton=driver.find_element(By.CLASS_NAME,value="sign-in-form__submit-btn--full-width")
# loginbutton.send_keys(Keys.ENTER)
loginbutton.click()

easy_apply = driver.find_element(By.ID, value="jobs-apply-button-id")
easy_apply.click()

mobile_number = driver.find_element(By.ID, value="single-line-text-form-component-formElement-urn-li-jobs-applyformcommon-easyApplyFormElement-4261882909-21473488908-phoneNumber-nationalNumber")

next_button= driver.find_element(By.ID, value="ember312")
next_button.click()
time.sleep(1)
next_button1= driver.find_element(By.ID, value="ember312")
next_button1.click()
# driver.close()  #this will close the chrome browser. Closes one tab
# driver.quit() # closes entrire browser