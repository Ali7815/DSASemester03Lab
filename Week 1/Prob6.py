# -*- coding: utf-8 -*-
"""
Created on Fri Sep  9 11:14:53 2022

@author: Digital Zone
"""

import funcs
number=input("Enter Number: ")
number=int(number)
sumIterative=funcs.SumIterative(number)
sumRecursive=funcs.SumRecursive(number)
print("The sum of Iterative Is : " + str(sumIterative))
print("The sum of Recursive Is : " + str(sumRecursive))