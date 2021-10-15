# -*- coding: utf-8 -*-
"""
Created on Thu Aug 26 21:40:36 2021

@author: Lenovo
"""

enemy = []
for i in range(1, 6):
    enemy.append(input("Enter a name: "))
print(enemy)
a = input("Enter a name: ")
print(a)
enemy.remove(a)
print(enemy)