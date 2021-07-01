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
PASSWORD = "ishitajain"
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
    # print(len(containers))
    for x in range(len(containers)):
        if "Industry" in containers[x].text:
            y=x
            break
    outcome=results.find_all('dd',class_='org-page-details__definition-text t-14 t-black--light t-normal')
    print(outcome[y].text.strip())
    # for x in range(len(containers)):
    #     if "Industry" in containers[x].text:
    #         print(outcome[x].text)


Scrape("laurus-labs")










# #### This program scrapes naukri.com's page and gives our result as a
# #### list of all the job_profiles which are currently present there.

# import requests
# from bs4 import BeautifulSoup
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from getpass import getpass
# import time

# #url of the page we want to scrape

# requests.get('https://www.linkedin.com/', auth=('yoishitajain@gmail.com', getpass()))
# url = "https://www.linkedin.com/company/laurus-labs/about/"

# # initiating the webdriver. Parameter includes the path of the webdriver.
# driver = webdriver.Chrome('E:/chromedriver_win32/chromedriver.exe')
# driver.get(url)

# # this is just to ensure that the page is loaded
# time.sleep(5)

# html = driver.page_source

# # this renders the JS code and stores all
# # of the information in static HTML code.

# # Now, we could simply apply bs4 to html variable
# soup = BeautifulSoup(html, "html.parser")
# all_divs = soup.find('div', {'id' : 'ember995'})
# print(all_divs)
# job_profiles = all_divs.find_all('div',class_='org-page-details__definition-text t-14 t-black--light t-normal')

# # printing top ten job profiles
# for job_profile in job_profiles :
# 	print(job_profile.text)

# driver.close() # closing the webdriver
