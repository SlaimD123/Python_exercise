# -*- coding: utf-8 -*-
"""
Created on Fri Aug 27 21:38:44 2021

@author: Lenovo
"""

network_file = open("network 1.txt", "r")
a = network_file.readlines()[1]
network_test = open("network test.txt", "w")
network_test.write(a)
b = input("Enter a sentence: ")
network_test.write(b)
network_file.close()
network_test.close()