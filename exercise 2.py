# -*- coding: utf-8 -*-
"""
Created on Sun Aug 22 21:04:15 2021

@author: Lenovo
"""

a1 = ["Jack", "David", "William", "Tony"]
for name in a1:
    print (name)

for index in range(len(a1)):    
    print (a1[index])
    
a = 0
for number in range(1, 101):
    a += number
print (a)