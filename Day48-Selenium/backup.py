from  selenium import webdriver
from selenium.webdriver.common.by import  By

##keep browser open after program finishes
chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach",True)

driver =webdriver.Chrome(options=chrome_option)
# driver.get("https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1")
driver.get("https://www.python.org")

# # price_doller = driver.find_element(By.CLASS_NAME, value="a-price-whole")
# # price_cents = driver.find_element(By.CLASS_NAME,value="a-price-fraction")
# # print(f"{price_doller.text}.{price_cents.text}")
#
# search_bar = driver.find_element(By.NAME, value="q")
# print(search_bar.tag_name)
# print(search_bar.get_attribute("placeholder"))
#
# button= driver.find_element(By.ID, value="submit")
# print(button.text)
#
# documentation_link = driver.find_element(By.CSS_SELECTOR,value=".documentation-widget a") #a link under documentation-widget class
# print(documentation_link.text)

#Using XPath we can find an element

# bug_link= driver.find_element(By.XPATH, value='//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
# print(bug_link.text)
