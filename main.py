from selenium import webdriver
from selenium.webdriver.common.by import By
import dependencies


# TO KEEP THE TAB OR TASK OPEN
chrome_option = webdriver.ChromeOptions()



chrome_option.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_option)
driver.get("https://python.org")

# price_of_the_product = driver.find_element(By.XPATH, value='/html/body/div/div[3]/div/section/div[2]/div[2]/div/ul/li[1]/time/span')
# year = price_of_the_product.text
ul = driver.find_element(By.CLASS_NAME, value='menu')

# time_tag = driver.find_element(By.XPATH, value='//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[2]/time')
l1 = []
links = []
time_tag = driver.find_elements(By.TAG_NAME, value="time")
for i in time_tag:
    l1.append(i.text)
events_div = driver.find_elements(By.XPATH, value='//*[@id="content"]/div/section/div[2]/div[2]/div/ul')

dict = {}
l1 = l1[::-1]
l3 = events_div[0].find_elements(By.TAG_NAME, value='a')
for i in l3:
    links.append(i.text)
j =-1
for i in range(5):
    j += 1
    pair = {'time':f"{l1[j]}",
            'name':f"{links[j]}",
            }
    dict.update({i: pair})




print(dict)
driver.quit()