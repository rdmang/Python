# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 22:17:03 2017

@author: Dmitry Stafeev
"""
from random import random
 
def randomOrder_key(Car):
    return random()

class Car(object):
    def __init__(self, name, speed, weight):
        self.name = name
        self.speed = speed
        self.weight = weight
    
    def __repr__(self):
        return '%s' % self.name
    
bmw = Car('bmw', 260, 1000)
mercedes = Car('mercedes', 240, 1200)
toyota = Car('toyota', 250, 1100)
cars = [bmw, mercedes, toyota]

a = sorted(cars, key = randomOrder_key)
print(a)