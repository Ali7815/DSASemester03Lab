# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 15:00:27 2022

@author: Digital Zone
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd
r=requests.get('https://www.flipkart.com/search?q=phones&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off')
q=requests.get("https://www.flipkart.com/search?q=phones&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page=9")
content=r.content
content2=q.content
laptopData=[]
mobileData=[]
brandName=[]
price=[]
rating=[]
Typee=[] 
soup=BeautifulSoup(content2 , 'lxml')
mobiles=soup.find_all('div',class_="_2kHMtA") 
for i in mobiles:
    mobileData.append(i.find('div',class_='_4rR01T').text)
    rating.append(i.find("div",class_='_3LWZlK').text)
    price.append(i.find('div',class_='_30jeq3 _1_WHN1').text)
 

Typee=soup.find('a',class_="_1jJQdf _2Mji8F").text

df=pd.DataFrame({"Product Name":mobileData,"Ratings":rating,"Price":price,"Availability":"Yes","Type":Typee})
df.to_csv("Data.csv")