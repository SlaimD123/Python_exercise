# -*- coding: utf-8 -*-
"""
Created on Wed Aug 25 21:08:08 2021

@author: Lenovo
"""

print ("Giraffe\nAcademy")
print ("Giraffe\"Academy")
phrase = "\"giraffe academy\""
print("Tom said:"+phrase)
print(phrase.lower())

print(phrase.replace("a","A"))
print(phrase.index("e"))

print(phrase.isupper())
if phrase.islower():
    print(phrase.upper())
    
my_num = 5
my_num1 = 3
print (my_num + my_num1)

from math import *
a = float(input("Enter a number : "))
print(sqrt(a))
print(pow(a, 2))
print(pow(a, 3))
print(floor(a))
print(ceil(a))
print(round(a))
print(max(a, 0))
print(min(a, 0))
print(abs(a))
print(str(a) + " is my favourite number . ")