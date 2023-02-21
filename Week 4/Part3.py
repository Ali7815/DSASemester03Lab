# -*- coding: utf-8 -*-
"""
Created on Sun Oct  2 19:21:15 2022

@author: Digital Zone
"""

def printMatrix(A, starting_index,  rows, columns) :
    for i in range(starting_index, rows) :
        for j in range(starting_index , columns):
            print(A[i][j],end=" ")  
        print("\n") 
def MatMulRecursive(x, y, k):
     array = [[]]  
     if k == 1:
        array = x[0][0]*y[0][0]  
        return array 
     else:
          Rows  = len(x)  
          col   = len(x[0]) 
          #slicing of matrix fist  
          upper_left  = [x[i][:col//2]for i in range(Rows//2)]
          upper_right = [x[i][col//2:]for i in range(Rows//2)] 
          lower_left  = [x[i][:col//2]for i in range(Rows//2,Rows)]
          lower_right = [x[i][col//2:]for i in range(Rows//2,Rows)]  
          print(upper_left)
          #slising of matrix 2   
          Rows  = len(y)  
          col   = len(y[0])  
          upper_left_M2  = [y[i][:col//2]for i in range(Rows//2)]
          upper_right_M2 = [y[i][col//2:]for i in range(Rows//2)]
          lower_left_M2  = [y[i][:col//2]for i in range(Rows//2,Rows)] 
          lower_right_M2 = [y[i][col//2:]for i in range(Rows//2,Rows)] 
          # C00 = MatMulRecursive(upper_left,upper_left_M2,k//2) +   MatMulRecursive((upper_right,lower_left_M2,k//2)) 
          # C01 = MatMulRecursive((upper_left,upper_right_M2,k // 2) + MatMulRecursive(upper_right, lower_right_M2, k // 2))
          # C10 = MatMulRecursive((lower_left, upper_left_M2, k // 2) + MatMulRecursive(lower_right, lower_left_M2, k // 2))
          # C11 = MatMulRecursive((lower_left, upper_right_M2, k // 2)  + MatMulRecursive(lower_left, lower_right_M2, k // 2)) 
     # return array([[C00, C01], [C10, C11]]) 
    
    
    

def MatAdd(A,B) :
    rows = len(A) 
    col = len(A[0]) 
    for i in range(0, rows) :
         for j in range(0 , col): 
             sum_arry =  A[i][j] + B[i][j] 
             print(sum_arry,end=" ")  
         print("\n") 
def MatAddPartial(A, B, start, size) :
    for i in range(start, (size)) :
        sum_arry = 0 
        for j in range(start , (size)):  
            sum_arry =  A[i][j] + B[i][j] 
            print(sum_arry,end=" ")  
        print("\n")     
def MatMul(A,B) :
    rows = len(A) 
    col = len(A[0])
    for row_index in range(rows) :
        multi = 0 
        for i in range(rows):
            for j in range(col):
                multi = multi+ A[row_index][j]*B[j][i] 
            print(multi,end=" ")  
            multi  = 0 
        print("\n")  
    
 
    
 
    
 
         







# if "__name__" == "__main__":
A = [[4, 3, 8, 9, 5, 1, 2, 7, 6],
           [8, 3, 4, 1, 5, 9, 6, 7, 2], 
           [6, 1, 8, 7, 5, 3, 2, 9, 4], 
           [6, 9, 8, 7, 5, 3, 2, 1, 4], 
           [6, 1, 8, 7, 5, 3, 2, 1, 4],
           [6, 1, 3, 2, 9, 4, 8, 7, 5]] 
# printMatrix(A, 3, len(A) , len(A[0])) 
A = [[12,7,3],
    [4 ,5,6],
    [7 ,8,9]]

B = [[5,8,1],
    [6,7,3],
    [4,5,9]] 
      
rows = len(A) 
col = len(A[0]) 
#MatAdd(A,B) 
#MatAddPartial(A, B, 1, 3) 
# MatMul(A,B) 

x = [[1, 1, 2, 2],
     [3, 3, 4, 4],
     [5, 5, 6, 6],
     [7, 7, 8, 8]] 

print(MatMulRecursive(x, x, 4)) 



       
   