# -*- coding: utf-8 -*-
"""
Created on Fri Sep 23 11:01:50 2022

@author: Digital Zone
"""
def numSeparator(num):
    Array1=[]
    while(num>0):
        mod=num%10
        Array1.append(mod)
        num=int(num/10)
    return Array1
def Multiply_integer(a,b):    
    A1=numSeparator(a)
    A2=numSeparator(b)
    array=[]
    L1=len(A1)
    base=0
    sum=""
    carry=0
    for j in A2:
        for i in range(0,L1):
            count=L1-1
            num=j*A1[i]+carry            
            if(num>=10 and i!=count):
                mod=num%10
                carry=num//10
                num=mod
            else:
                num=num
                carry=0
            sum=str(num)+sum        
        carry=0
        if(base>0):
            sum=sum.ljust(base + len(sum), '0')
        base=base+1
        sum=int(sum)
        array.append(sum)
        sum=str("")
    sum=0
    for i in array:
        sum=sum+i
    return str(sum)
def Multiply_string(a,b):
    a=int(a)
    b=int(b)
    A1=numSeparator(a)
    A2=numSeparator(b)
    array=[]
    L1=len(A1)
    base=0
    sum=""
    carry=0
    for j in A2:
        for i in range(0,L1):
            count=L1-1
            num=j*A1[i]+carry            
            if(num>=10 and i!=count):
                mod=num%10
                carry=num//10
                num=mod
            else:
                num=num
                carry=0
            sum=str(num)+sum        
        carry=0
        if(base>0):
            sum=sum.ljust(base + len(sum), '0')
        base=base+1
        sum=int(sum)
        array.append(sum)
        sum=str("")
    sum=0
    for i in array:
        sum=sum+i
    return str(sum)
def Visualize_Karatsuba(a,b):
    A1=numSeparator(a)
    A2=numSeparator(b)
    print(a)
    print(b)
    print("```````````````")
    array=[]
    L1=len(A1)
    base=0
    sum=""
    carry=0
    for j in A2:
        for i in range(0,L1):
            count=L1-1
            num=j*A1[i]+carry            
            if(num>=10 and i!=count):
                mod=num%10
                carry=num//10
                num=mod
            else:
                num=num
                carry=0
            sum=str(num)+sum        
        carry=0
        if(base>0):
            sum=sum.ljust(base + len(sum), '0')
        base=base+1
        sum=int(sum)
        array.append(sum)
        sum=str("")
    higherLength=0
    for i in array:
        length=numSeparator(i)
        if(higherLength<len(length)):
            highterLength=len(length)
    for i in array:
        st=str(i)
        res=st.zfill(highterLength)
        print(res)       
    sum=0
    for i in array:
        sum=sum+i
    print("```````````````")
    print(sum)
    print("```````````````")
def Multiply_Recursive(a,b):
    if(len(a)==1 or len(b)==1):
        return int(a)*int(b)
    else:
        n1=len(a)
        n2=len(b)
        if(n1>n2):
            lar=n1
        else:
            lar=n2
        a=a.zfill(lar)
        b=b.zfill(lar)         
        n=len(a)
        aL=a[:len(a)//2]
        aR=a[len(a)//2:]
        bL=b[:len(b)//2]
        bR=b[len(b)//2:]
        x1=int(Multiply_Recursive(aL, bL))
        x2=int(Multiply_Recursive(aL, bR))
        x3=int(Multiply_Recursive(aR, bL))
        x4=int(Multiply_Recursive(aR, bR))
        return str(x1*pow(10,int(n))+(x2+x3)*pow(10,int(n/2))+x4)

def Karatsuba_Recursive(a,b):
    if(len(a)==1 or len(b)==1):
        return int(a)*int(b)
    else:
        n=len(a)
        aL=a[:len(a)//2]
        bL=a[len(a)//2:]
        cL=b[:len(b)//2]
        dL=b[len(b)//2:]
        p=int(aL)+int(bL)
        q=int(cL)+int(dL)
        ac=int(Karatsuba_Recursive(aL, cL))   
        bd=int(Karatsuba_Recursive(bL, dL))
        ab_bc=int(Karatsuba_Recursive(str(p), str(q)))
        abbc= ab_bc - ac - bd
        return str(ac*pow(10,int(n)) + abbc*pow(10,int(n/2)) + bd)

def Multiply2(x,y):
    a=int(x,2)
    b=int(y,2)
    a=str(a)
    b=str(b)
    if(len(a)==1 or len(b)==1):
        res=int(a)*int(b)
        return str(bin(res))
    else:
        n=len(a)
        aL=a[:len(a)//2]
        bL=a[len(a)//2:]
        cL=b[:len(b)//2]
        dL=b[len(b)//2:]
        p=int(aL)+int(bL)
        q=int(cL)+int(dL)
        ac=int(Karatsuba_Recursive(aL, cL))   
        bd=int(Karatsuba_Recursive(bL, dL))
        ab_bc=int(Karatsuba_Recursive(str(p), str(q)))
        abbc= ab_bc - ac - bd
        res=ac*pow(10,int(n)) + abbc*pow(10,int(n/2)) + bd
        return str(bin(res))