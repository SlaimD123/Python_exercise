# -*- coding: utf-8 -*-
"""
Created on Tue Aug 24 20:33:30 2021

@author: Lenovo
"""

import random
x = random.randint(1, 30)

i = 1
while i > 0:
    y = int(input("Enter a number : "))
    if y < x:
        print("The number you guessed is lower")
    elif y > x:
        print("The number you guessed is higher")
    else:
        print("You are right !")
        break