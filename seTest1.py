from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

browser = webdriver.Chrome(executable_path=r"C:\chromedriver\chromedriver.exe") # error:  chrome ver was incompaitble

browser.get("https://www.instagram.com/accounts/login/")  # get gets url
print(browser.title)  # title of the page

emailBox = browser.find_element_by_name("username")
passwordBox = browser.find_element_by_name("password")
loginButton = browser.find_element_by_xpath("//button[@type=\"submit\"]")
WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@name='username']"))).send_keys("username")

emailBox.send_keys("")
passwordBox.send_keys(" ")

sleep(10)

loginButton.click()
#browser.close()
