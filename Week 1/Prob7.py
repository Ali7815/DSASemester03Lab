# -*- coding: utf-8 -*-
"""
Created on Fri Sep  9 13:46:54 2022

@author: Digital Zone
"""

import funcs
A=[[1,13,13],[5,11,6],[4,4,9]]
col=funcs.ColumnWiseSum(A)
row=funcs.RowWiseSum(A)
print("The Sum in Column Wise : ", col)
print("The Sum in Row Wise : ", row)