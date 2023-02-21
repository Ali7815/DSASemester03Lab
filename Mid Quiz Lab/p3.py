# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 12:53:42 2022

@author: Digital Zone
"""

import random

def Prob3():
    A=[]
    hashTable=[None]*20
    for i in range(20):
        num=random.randint(1, 10)
        A.append(num)
    
    for i in range(0,len(A)):
        C=A[i]
        h=0
        j=0
        h=hashFunc1(C)+(j*hashFunc2(C))
        count=0
        while count!=10:
            j=j+1
            h=hashFunc1(C)+(j*hashFunc2(C))
            count+=1
        hashTable[h]=A[i] 
        print(hashTable)
                            
        
        
def hashFunc1(C):
    h1=C%7
    return h1

def hashFunc2(C):
    h2=C%3
    return h2
    
    
def main():
    Prob3()
    
    
if __name__=="__main__":
    main()