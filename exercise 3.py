# -*- coding: utf-8 -*-
"""
Created on Mon Aug 23 22:30:32 2021

@author: Lenovo
"""

i = 0
while i < 3:
    word = input("Please enter a word I'm now thinking: ") 
    if word != "David":
        print ("Sorry, that's not the correct answer.")
        if i == 2:
            print ("You lose !")
    else:
        print ("You win !")
        break
    i += 1