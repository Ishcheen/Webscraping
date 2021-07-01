import requests
from bs4 import BeautifulSoup
URL= 'https://auth.geeksforgeeks.org/user/yoishitajain/practice/'
page=requests.get(URL)

soup=BeautifulSoup(page.content,'html.parser')
results=soup.find(id='detail1')
label=results.find_all('div',class_='mdl-cell mdl-cell--6-col mdl-cell--12-col-phone textBold')
for label in label:
    score=label.find('a')
s=score.text
print(int(s[17]+s[18]))
