from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

#creating a PATH variable to locate the webdriver path on the local machine
PATH = "/home/magdi/Downloads/chromedriver_linux64/chromedriver"

userInput = input("What word would you like searched today? ").lower()

driver = webdriver.Chrome(PATH)
driver.get("https://www.dictionary.com/")
searchBar = driver.find_element_by_id("searchbar_input")
searchBar.clear()
searchBar.send_keys(userInput)
searchBar.send_keys(Keys.RETURN)

input("")
driver.close()