# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 21:48:36 2017

@author: Dmitry Stafeev
"""
from random import randint
 
k = 10
A = [randint(-10,100) for x in range(k)]
print('Unsorted:',A)

def merge_sort(A):
    if len(A) <= 1:
        return A
    middle = int(len(A)/2)
    left = merge_sort(A[:middle])
    right = merge_sort(A[middle:])
    return merge(left,right)
def merge(left,right):
    result = []
    while len(left) > 0 and len(right) > 0:
        if left[0] <= right[0]:
            result.append(left[0])
            left = left[1:]
        else:
            result.append(right[0])
            right = right[1:]
    if len(left) > 0:
        result += left
    if len(right) > 0:
        result += right
    return result

A = merge_sort(A)
print('Sorted:',A)