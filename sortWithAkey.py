# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 21:46:56 2017

@author: Dmitry Stafeev
"""
def byName_key(person):
    return person.name

class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return '%s %s' % (self.name, self.age)

jack = Person('Jack', 19)
adam = Person('Adam', 43)
becky = Person('Becky', 11)
soram = Person('Soram', 15)
people = [jack, adam, becky, soram]

result = sorted(people, key=byName_key)
print(result)