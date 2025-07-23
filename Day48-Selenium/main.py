from  selenium import webdriver
from selenium.webdriver.common.by import  By

##keep browser open after program finishes
chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach",True)

driver =webdriver.Chrome(options=chrome_option)
# driver.get("https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1")
driver.get("https://www.python.org")

event_times =driver.find_elements(By.CSS_SELECTOR, value=".event-widget time")
event_names =driver.find_elements(By.CSS_SELECTOR, value=".event-widget li a")
# get_all_events =[(index, item.text) for (index, item) in  get_all_events_arr]

events={}

for n in range(len(event_times)):
    events[n]={
        "time": event_times[n].text,
        "name": event_names[n].text
    }

print(events)

# bug_link= driver.find_element(By.XPATH, value='//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
# print(bug_link.text)




driver.close()  #this will close the chrome browser. Closes one tab
driver.quit() # closes entrire browser