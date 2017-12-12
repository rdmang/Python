# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 21:36:18 2017

@author: Dmitry Stafeev
"""
from random import randint
 
k = 10
A = [randint(-10,100) for x in range(k)]
print('Unsorted:',A)

def insertion_sort(A):
    for i in range (1,len(A)):
        value = A[i]
        j = i-1
        while j>=0 and A[j]> value:
            A[j+1] = A[j]
            j = j - 1
        A[j+1] = value
    return A

A = insertion_sort(A)
print('Sorted:',A)