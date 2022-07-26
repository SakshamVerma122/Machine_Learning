from selenium import webdriver
from selenium.webdriver.common.by import By
browser = webdriver.Chrome("chromedriver.exe")

browser.get("https://www.codechef.com/login?destination=/")

username_element = browser.find_element(By.ID,"edit-name")

username_element.send_keys("sakshamv001")