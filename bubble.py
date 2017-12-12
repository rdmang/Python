# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 21:53:47 2017

@author: Dmitry Stafeev
"""
from random import randint
 
k = 10
A = [randint(-10,100) for x in range(k)]
print('Unsorted:',A)

def bubble_sort(A):
    for i in range(len(A)):
        for j in range(len(A) - 1, i, -1):
            if A[j] < A[j-1]:
                A[j], A[j-1] = A[j-1], A[j]

    return A

A = bubble_sort(A)
print('Sorted:',A)