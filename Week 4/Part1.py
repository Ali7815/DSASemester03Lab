# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 13:34:14 2022

@author: Digital Zone
"""
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import pandas as pd
# Problem 1-Draw the line chart for the total number of steps on daily basis.
df=pd.read_csv('dailySteps_merged.csv')
dfE_NoH = pd.read_csv('dailySteps_merged.csv',header = 4, usecols=[0])  
# df = pd.read_csv(file_path, header=None, usecols=[3,6])
print(dfE_NoH) 
list1=df['ActivityDay'].values.tolist()
list2=df['StepTotal'].values.tolist()
list3=[]
list4=[]
lis=list1
plt.title("Total Steps per Day Line Graph")
plt.xlabel("Date")
plt.ylabel("Total Steps")
for i in range(0,len(list1)):
    sum=0
    for j in range(0,len(list1)):
        if lis[i]==list1[j]:
            
            sum=sum+int(list2[j])
            list2[j]=0
    if sum>0:
        list3.append(sum)
        list4.append((lis[i]))
plt.plot(list4,list3)
plt.show()
# End-------------------------------------

# Problem 2-Draw the bar chart for the daily distance covered.
df=pd.read_csv('dailyActivity_merged.csv')
list1=df['ActivityDate'].values.tolist()
list2=df['TotalSteps'].values.tolist()
list3=[]
list4=[]
lis=list1
plt.title("Daily Distance per Day Bar Graph")
plt.xlabel("Date")
plt.ylabel("Total Steps")
for i in range(0,len(list1)):
    sum=0
    for j in range(0,len(list1)):
        if lis[i]==list1[j]:
            
            sum=sum+int(list2[j])
            list2[j]=0
    if sum>0:
        list3.append(sum)
        list4.append((lis[i]))
plt.bar(list4,list3)
plt.show()
# End-------------------------------------

# Problem 3-Draw the scatter chart for the total time in the bed.
df=pd.read_csv("sleepDay_merged.csv")
list1=df['SleepDay'].values.tolist()
list2=df['TotalTimeInBed'].values.tolist()
list3=[]
list4=[]
lis=list1
plt.title("Total Time in Bed Scatter Graph")
plt.xlabel("Date")
plt.ylabel("Total Time in Bed")
for i in range(0,len(list1)):
    sum=0
    for j in range(0,len(list1)):
        if lis[i]==list1[j]:
            sum=sum+int(list2[j])
            list2[j]=0
    if sum>0:
        list3.append(sum)
        list4.append(lis[i])
plt.scatter(list4,list3)
plt.show()   
# End------------------------------------- 

# Problem 4-Draw the Pie chart for the hourly steps on the 12th April 2016. 
df=pd.read_csv("hourlySteps_merged.csv")
list1=df['ActivityHour'].values.tolist()
list2=df['StepTotal'].values.tolist()
plt.title("Total Hourly Steps on 12th April 2016")
list3=[]
list4=[]
lis=list1
for i in range(0,len(list1)):
    sum=0
    x=list1[i].split()
    if x[0]=="4/12/2016":
        for j in range(0,len(list1)):
            if lis[i]==list1[j]:
                sum=sum+int(list2[j])
                list2[j]=0
    if sum>0:
        list3.append(sum)
        list4.append(lis[i])
plt.pie(list3)
plt.show()
# with PdfPages(r'D:\Study\charts2.pdf') as export_pdf:
#     plt.scatter(list4,list3)
#     plt.title('Unemployment Rate Vs Index Price', fontsize=14)
#     plt.xlabel('Unemployment Rate', fontsize=14)
#     plt.ylabel('Index Price', fontsize=14)
#     plt.grid(True)
#     export_pdf.savefig()
#     plt.close()
# # End-------------------------------------