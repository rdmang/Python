# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 22:27:34 2017

@author: Dmitry Stafeev
"""
from random import randint
 
k = 10
A = [randint(-10,100) for x in range(k)] 
print('Unsorted:',A)

left = 0
right = len(A) - 1
 
while left <= right:
    for i in range(left, right, +1):
        if A[i] > A[i + 1]:
            A[i], A[i + 1] = A[i + 1], A[i]
    right -= 1
 
    for i in range(right, left, -1):
        if A[i - 1] > A[i]:
            A[i], A[i - 1] = A[i - 1], A[i]
    left += 1
    
print('Sorted:',A)