# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 21:58:07 2022

@author: Digital Zone
"""
import re
import requests
from lxml.html import fromstring
from bs4 import BeautifulSoup
import pandas as pd


specifics=[]
laptop=[]
brand=[]
model=[]
storage=[]
operatingSystem=[]
screen=[]
Ram=[]
warranty=[]
price=[]
OS=[]
speed=[]
typeStorage=[]

# w3schollsList=soup.find_all("li", class_="col-xs-6 col-sm-4 col-md-4 col-lg-3")
# for w3scholl in w3schollsList:
#     ulList = w3scholl.find_all('li')
#     for li in ulList:
#         brand.append(str(li))
# x=brand[0].split('</span>')
# y=x[1].split('</li>')
# print(x[1])
# print("y",y)
# print(brand[0])
# print(brand[1])
# print(brand[2])
        
url="https://www.mega.pk/laptop-price-pakistan/"
u="https://www.mega.pk/laptop-price-pakistan/"


for l in range(2,8):
    print("first Url,",url)
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
    # print(url)
    
# data=soup.find_all("li", class_="col-xs-6 col-sm-4 col-md-4 col-lg-3")
# for d in data:
#     ulList = d.find_all('li')
#     for li in ulList:
#         s=str(li)
#         x=s.split('</span>')
#         y=x[1].split('</li>')
#         specifics.append(y[0])
        
#     model.append(specifics[0])
#     Ram.append(specifics[1])
#     screen.append(specifics[2])  
#     OS.append(specifics[3])
#     storage.append(specifics[4])
#     typeStorage.append(specifics[5])
#     if(len(specifics)>6):
#         speed.append(specifics[6])
#     else:
#         speed.append('NA')
#     specifics.clear()

# for i in data:
#     p=str(i.find('div',class_='cat_price').text)
#     # z=price.split()
#     z=re.split('\n |, |\t|\n',p)
#     price.append(z[5])

    
   
# print(price) 
# for i in range(len(model)):
#     print(model[i],Ram[i],screen[i],OS[i],storage[i],typeStorage[i],speed[i])


df=pd.DataFrame({"Model":model,"Screen":screen,"Operating System":OS,"Storage":storage,"Type Storage":typeStorage,'Speed':speed,'Price':price})
df.to_csv("LaptopDataScrap.csv")
# # tab=soup.find("table",{"class":"wikitable sortable jquery-tablesorter"})
# laptop=soup.find_all("li", class_="col-xs-6 col-sm-4 col-md-4 col-lg-3")
# # result = soup.find('div', {'class': 'movie-add-info left'}).find('ul').findChildren(text=re.compile(r'GENRE'))
# for i in laptop:
#     specifics.append(i.find("div", {"id": "lap_name_div"}).text)
#     res=i.find('div', {'class': 'lap_thu_box bg-color-white'}).find('ul').findChildren(text=re.compile(r'Screen: '))
#     # print(res)
#     memory.append(res)
    
# # print(memory)   
# # print(specifics[0])
# # print(specifics[1])
# # # print(specifics[1])
# # print(specifics[2])
# # print(specifics[3])