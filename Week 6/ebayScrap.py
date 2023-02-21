# -*- coding: utf-8 -*-
"""
Created on Fri Oct 14 20:01:56 2022

@author: Digital Zone
"""
# -*- coding: utf-8 -*-
"""
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd



url = "https://www.ebay.com/sch/175672/i.html?_from=R40&_nkw=laptop&LH_TitleDesc=0&_ipg=60"
r = requests.get(url)
htmlContent = r.content
soup = BeautifulSoup(htmlContent, "html.parser")
links=[]
allLaptop = soup.find_all('a',class_= "s-item__link")
for d in allLaptop:
    st=str(d)
    x=st.split('href="')
    y=x[1].split('"')
    links.append(y[0])
    
print(links[1])
print(len(links))
count=0
for i in range(1,len(links)):
    u=links[i]
    r = requests.get(u)
    htmlContent = r.content
    soup2 = BeautifulSoup(htmlContent, "html.parser")
    p=str(soup2.find('div',class_='ux-layout-section__item ux-layout-section__item--table-view').text)
    print(p)
    z=p.split()
    count=count+1
    if count==3:
        break
    
    # for lin in ulList:
    #     s=str(lin)
    #     print(s)
# print(allLaptop)\
# cls

# print(allLaptop.find('a', href=True)['href'])
# for tag in allLaptop:
#      link = tag.find('a')['href']
#      print(link)
    


    