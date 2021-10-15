# -*- coding: utf-8 -*-
"""
Created on Sat Sep 11 22:23:19 2021

@author: Lenovo
"""

def order(a, b, c):
    if a > b and b > c:
        print(a, b, c)
    elif a > b and b < c:
        print(a, c, b)
    elif a > b and a < c:
        print(c, a, b)
    elif a < b and a < c:
        print(c, b, a)
    elif b > a and a > c:
        print(b, a, c)
    else:
        print(b, c, a)        

def amount(a, b, c):
    print(a * "#")
    print(b * "#")
    print(c * "#")
x = int(input("Inter a number z = "))
y = int(input("Inter a number y = "))
z = int(input("Inter a number z = "))
order(x, y, z)
amount(x, y, z)
