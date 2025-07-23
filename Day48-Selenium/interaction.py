from  selenium import webdriver
from selenium.webdriver.common.by import  By
from selenium.webdriver.common.keys import  Keys
url="https://secure-retreat-92358.herokuapp.com/"
# url="https://www.google.com/"
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(chrome_options)
driver.get(url)
# article_count = driver.find_element(By.CSS_SELECTOR, value="#articlecount ul li a")

####Click a controls
####-----------------
# print(article_count.text)
# article_count.click()

# content_portal = driver.find_element(By.LINK_TEXT, value="Content portals")
# content_portal.click()

####Typeing text
####------------
fname = driver.find_element(By.NAME, value='fName')
# search.send_keys("Python")
# search.send_keys(Keys.ENTER)
fname.send_keys("Newman")

lname=driver.find_element(By.NAME, value='lName')
lname.send_keys("Croos")
email=driver.find_element(By.NAME, value='email')
email.send_keys("newmancroos@gmail.com")

signup= driver.find_element(By.CLASS_NAME, value="btn-primary")
signup.send_keys(Keys.ENTER)
# driver.close()  #this will close the chrome browser. Closes one tab
# driver.quit() # closes entrire browser