# -*- coding: utf-8 -*-
"""
Created on Thu Oct 13 00:01:28 2022

@author: Digital Zone
"""

import re
import requests
from bs4 import BeautifulSoup
import pandas as pd
specifics=[]
laptop=[]
brand=[]
model=[]
storage=[]
screen=[]
Ram=[]
price=[]
OS=[]
speed=[]
typeStorage=[]
url="https://www.mega.pk/laptop-price-pakistan/"
u="https://www.mega.pk/laptop-price-pakistan/"
for l in range(2,8):
    r=requests.get(url)
    content=r.content
    soup=BeautifulSoup(content,'lxml')
    data=soup.find_all("li", class_="col-xs-6 col-sm-4 col-md-4 col-lg-3")
    for d in data:
        ulList = d.find_all('li')
        for li in ulList:
            s=str(li)
            x=s.split('</span>')
            y=x[1].split('</li>')
            specifics.append(y[0])
            
        model.append(specifics[0])
        Ram.append(specifics[1])
        screen.append(specifics[2])  
        OS.append(specifics[3]) 
        storage.append(specifics[4])
        if(len(specifics)>5):
            typeStorage.append(specifics[5])
        else:
            typeStorage.append('NA')
        if(len(specifics)>6):
            speed.append(specifics[6])
        else:
            speed.append('NA')
        specifics.clear()

    for i in data:
        p=str(i.find('div',class_='cat_price').text)
        # z=price.split()
        z=re.split('\n |, |\t|\n',p)
        if(len(z)>3):
            price.append(z[5])
        else:
            price.append('Coming Soon')
    url=u
    url=url+str(l)+"/"
df=pd.DataFrame({"Model":model,"RAM":Ram,"Screen":screen,"Operating System":OS,"Storage":storage,"Type Storage":typeStorage,'Speed':speed,'Price':price})
df.to_csv("MegaWebLaptop.csv")