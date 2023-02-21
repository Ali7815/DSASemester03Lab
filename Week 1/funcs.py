# -*- coding: utf-8 -*-
"""
Created on Thu Sep  8 21:30:50 2022

@author: Digital Zone
"""
#Problem 1
def SearchA(Arr,x):
    indices=[]
    for i in range(len(Arr)):       
        if(Arr[i] == x):
            indices.append(i)
    return indices
#Problem 3
def Minimum(Arr,starting,ending):
    smallest=Arr[starting]   
    index = starting 
    for i in range(starting,ending):
        if(Arr[i+1]<smallest):
            smallest=Arr[i+1]
            index=i+1
    return index
#Problem 4
def Sort4(Arr):
    for i in range(len(Arr)):
        min=Minimum(Arr, i, len(Arr)-1)
        temp=Arr[i]
        Arr[i]=Arr[min]
        Arr[min]=temp
    return Arr
#Problem 5
def StringReverse(str,starting,ending):
    if(starting==ending):
        return str[starting]
    else:
        arr=str[starting:ending]
        arr=arr[::-1]  
        return arr
#Problem 6
def SumIterative(number):
    num=number
    sum=0
    while(num!=0):
        mod=num%10
        sum=sum+mod
        num=num/10
        num=int(num)
    return sum
def SumRecursive(number):
    if(number==0):
        return number
    else:
        return (number%10 + SumRecursive(int(number/10))) 
#Problem 7
def ColumnWiseSum(Mat):
    sum=0
    columnArr=[]
    rows=len(Mat)
    columns=len(Mat[0])
    for i in range(columns):
        for j in range(rows):
            sum=sum+Mat[j][i]
        columnArr.append(sum)
        sum=0
    return columnArr
def RowWiseSum(Mat):
    sum=0
    rowArr=[]
    rows=len(Mat)
    columns=len(Mat[0])
    for i in range(rows):
        for j in range(columns):
            sum=sum+Mat[i][j]
        rowArr.append(sum)
        sum=0
    return rowArr
#Problem 8
def SortedMerge(Arr1,Arr2):
    aLength=len(Arr1)
    bLength=len(Arr2)
    sortedArray=[None]*(aLength+bLength)
    i=0
    j=0
    k=0
    while i<aLength and j<bLength:
        if(Arr1[i]<Arr2[j]):
            sortedArray[k]=Arr1[i]
            i=1+i
            k=k+1
        else:
            sortedArray[k]=Arr2[j]
            j=j+1
            k=k+1
    return sortedArray
#Problem 9
def PalindromRecursive(str):
   if len(str)<1:
       return True
   else:
       if (str[0]==str[-1]):
           return PalindromRecursive(str[1:-1])
       else:
           return False
#Problem 10
def Sort10(Arr):
    minus=0
    plus=0
    sort=[]
    chk=False
    chk2=False
    for i in range(len(Arr)):
        for j in range(len(Arr)):
            if(Arr[j]<0):
                for k in range(len(Arr)):
                    if(Arr[j]<Arr[k]):                        
                        chk=True
                        minus=Arr[i]
                    else:
                        chk=False
        if(chk==True):
            sort.append(minus)
        for j in range(len(Arr)):
            if(Arr[i]>0 and Arr[i]<Arr[i+1]):
                chk2=True
                plus=Arr[i]
            else:
                chk2=False
        if(chk2==True):
            sort.append(plus)
                