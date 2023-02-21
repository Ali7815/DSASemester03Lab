# -*- coding: utf-8 -*-
"""
Created on Sat Oct  1 15:17:43 2022

@author: Digital Zone
"""

import matplotlib.pyplot as plt
import pandas as pd
import math
train=pd.read_csv('Train.csv')
Part2=pd.read_csv('Train.csv') #Load Data using Panda
test=pd.read_csv('Test.csv')
Type=[]
disList=[]
print(len(train))
for i in range(0,len(test)):
    sum=0
    row=test.iloc[i]
    for j in range(0,len(train)):
        sum=0
        row2=train.iloc[j]
        for k in range(0,len(row)-1):
            sum=sum+pow((row[k]-row2[k]),2) 
        dis=math.sqrt(sum) #Calcuating Distance
        
        disList.append(dis)
    smallest=min(disList)
    idx=disList.index(smallest)
    row2=train.iloc[idx]
    Type.append(row2[20])
    print("The Patient",i+1,"Disease is : ",row2[20]) #Labeling Disease to Each Patient
    disList.clear()
test['TYPE']=Type
test.to_csv("Test.csv", index=False)
# 6- Now split the main data in two parts: Part1 contain the data with no change,
 # Part 2: contains the data without label. 
#7-Now run your algorithm on Part2 while taking Part1 data as reference. 
# How much labels you assign# correctly? Give the answer in percentage. 
# Can you increase the percentage of ratio of correctly classified instances. 
disList=[]
Type=[]
Part2.pop('TYPE') 
for i in range(0,len(Part2)):
    sum=0
    row=Part2.iloc[i]
    for j in range(0,len(train)):
        sum=0
        row2=train.iloc[j]
        for k in range(0,len(row)-1):
            sum=sum+pow((row[k]-row2[k]),2) 
        dis=math.sqrt(sum) #Calcuating Distance
        
        disList.append(dis)
    smallest=min(disList)
    idx=disList.index(smallest)
    row2=train.iloc[idx]
    Type.append(row2[20])
    print("The Patient",i+1,"Disease is : ",row2[20]) #Labeling Disease to Each Patient
    disList.clear()
Part2['TYPE']=Type
Part2.to_csv("T2.csv", index=False)   
count=0
for i in range(0,len(Part2)):
    par2=Part2.iloc[i]
    trai=train.iloc[i]
    if(par2[len(par2)-1]==trai[len(trai)-1]):
        count=count+1
percen=(count/len(Part2))*100
print("Percentage of Ratio : ", percen)
        
        
# Correctness Ratio
            
        