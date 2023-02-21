# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 13:29:09 2022

@author: Digital Zone
"""
def main():
    print("Ali")
    A=MyHashTable(128)
    A.printArray()
    A.Insert("Ali")
    A.printList()
    
    
    
class KeyNode:
    Key=""
    Value=0
    def __init__(self,Key,Value):
        self.Key=Key
        self.Value=Value

class MyHashTable:
    hSize=0
    KeysOccupied=0
    A=[[]]
    def __init__(self,hSize):
        self.A=hSize*[[]]
        self.hSize=hSize
        
    
    def printArray(self):
        print(self.A)
        
    def printList(self):
        for i in self.A:
            for j in i:
                print(j.Key, " ",j.Value)
                
    def GetHashTableSize(self):
        return self.hSize
    
    def GetNumberOfKeys(self):
        return self.KeysOccupied
    
    def UpdateKey(self,Key,Value):
        obj=KeyNode(Key,Value)
        
    def HashFunction(self,key,hashValue):
        sum=0
        for i in range(0,len(key)):
            a=key[i]
            asc=ord(a)
            sum=sum+asc
        val=sum%hashValue
        return val
    def Insert(self,key):
        v=self.HashFunction(key,128)
        Node=KeyNode(key,v)
        self.A[v].append(Node)
if __name__=="__main__":
    main()
        