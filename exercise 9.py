# -*- coding: utf-8 -*-
"""
Created on Sun Aug 29 20:01:29 2021

@author: Lenovo
"""

def sum(n):
    i = 0
    for number in range(1, n + 1):
        i += number
    return i
a = int(input("Enter a number : "))
print (sum(a))