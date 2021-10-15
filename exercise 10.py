# -*- coding: utf-8 -*-
"""
Created on Wed Sep  1 21:20:56 2021

@author: Lenovo
"""

from math import *
def function(a, b, c):
    if a == 0:
        print("Invalid input. Because a = 0")
    else:
        delta = b**2 - 4*a*c
        if delta > 0:
            x1 = (-b + sqrt(delta)) / 2*a
            x2 = (-b - sqrt(delta)) / 2*a
            print("x1 = " + str(x1) + ", x2 = " + str(x2))
        elif delta == 0:
            x1 = -b / 2*a
            print("x1 = x2 = " + str(x1))
        else:
            print("No Real Roots !")
        
a1 = int(input("Enter a number a = ")) 
b1 = int(input("Enter a number b = "))  
c1 = int(input("Enter a number c = "))
function(a1, b1, c1)

    