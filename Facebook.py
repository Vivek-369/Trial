from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome()
driver.maximize_window()

driver.get("https://www.facebook.com/login/?privacy_mutation_token=eyJ0eXBlIjowLCJjcmVhdGlvbl90aW1lIjoxNjc5MjQzOTg0LCJjYWxsc2l0ZV9pZCI6MjY5NTQ4NDUzMDcyMDk1MX0%3D")
name=driver.find_element(By.NAME,'email').send_keys("vivek gondaliya")
password=driver.find_element(By.NAME,'pass').send_keys("vivek008")
btnLogin=driver.find_element(By.NAME,'login')
btnLogin.click()
time.sleep(10)


driver.close()