from selenium import webdriver
from secrets import username,password
import time
driver=webdriver.Safari()
driver.get("https://ipgw.neu.edu.cn")
time.sleep(1)
driver.find_element_by_xpath('/html/body/div/div[1]/div[2]/div[1]/div[2]/div/div/a[1]').click()
time.sleep(1)
driver.find_element_by_xpath('//*[@id="un"]').send_keys(username)
driver.find_element_by_xpath('//*[@id="pd"]').send_keys(password)
driver.find_element_by_xpath('//*[@id="index_login_btn"]').click()
time.sleep(1)
driver.quit()
#python3 ./ipgw_auto_login/main.py