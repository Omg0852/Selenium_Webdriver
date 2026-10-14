from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


chrome_option = webdriver.ChromeOptions()

chrome_option.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_option)
driver.get("https://orteil.dashnet.org/cookieclicker/")

lang = driver.find_element(By.CLASS_NAME, value="langSelectButton title")
lang.click()
cookie = driver.find_element(By.XPATH, value="//*[@id='bigCookie']")
cookie.click()
# <div class="" style="padding:4px;" id="langSelect-EN">English</div>