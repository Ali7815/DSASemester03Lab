# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 15:30:34 2022

@author: Digital Zone
"""

# import requests
# from bs4 import BeautifulSoup
# import pandas as pd
# r=requests.get('https://www.flipkart.com/search?q=laptop&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=off&as=off')
# content=r.content
# laptop=[]
# brand=[]
# model=[]
# memory=[]
# operatingSystem=[]
# display=[]
# warranty=[]
# price=[]
# soup=BeautifulSoup(content , 'lxml')
# laptop=soup.find_all('div',class_="_1fQZEK")
# for i in laptop:
#     brand.append(i.find('div',class_="_4rR01T").text)
#     model.append(i.find('li',class_="rgWa7D").text)
#     memory.append(i.find('li',class_="rgWa7D").text)

# df=pd.DataFrame({"Brand":brand,"Model":model,"Memory":memory})
# df.to_csv("LaptopData.csv")

url="https://www.mega.pk/laptop-price-pakistan/"
u="https://www.mega.pk/laptop-price-pakistan/"
print(url)
for i in range(2,6):
    url=url+str(i)+"/"
    print(url)
    url=u