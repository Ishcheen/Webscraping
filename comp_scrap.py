from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from bs4 import BeautifulSoup as bs
import re as re
import time


USERNAME = "yoishitajain@gmail.com"
PASSWORD = ""
driver = webdriver.Chrome('E:/chromedriver_win32/chromedriver.exe')
driver.get("https://www.linkedin.com/uas/login")
time.sleep(3)

email=driver.find_element_by_id("username")
email.send_keys(USERNAME)
password=driver.find_element_by_id("password")
password.send_keys(PASSWORD)
time.sleep(3)
password.send_keys(Keys.RETURN)

def Scrape(company_name):
    driver.get('https://www.linkedin.com/company/'+ company_name+'/about/')
    time.sleep(10)
    
    company_page=driver.page_source
    linkedin_soup = bs(company_page.encode("utf-8"), 'html.parser')
    linkedin_soup.prettify()
    results=linkedin_soup.find(class_='overflow-hidden')
    containers = results.findAll('dt',class_='org-page-details__definition-term t-14 t-black t-bold')
   
    for x in range(len(containers)):
        if "Industry" in containers[x].text:
            y=x
            break
    outcome=results.find_all('dd',class_='org-page-details__definition-text t-14 t-black--light t-normal')
    print(outcome[y].text.strip())

Scrape("laurus-labs")










