# -*- coding: utf-8 -*-
"""
Created on Fri Sep  3 19:18:37 2021

@author: Lenovo
"""

from pylab import *
from math import *
from numpy import *

a = int(input("Enter a number a = "))
b = int(input("Enter a number b = "))
c = int(input("Enter a number c = "))
x = linspace(-100, 101)
y = a*x**2 + b*x + c
xx = zeros(len(x))
plot(x, y, 'r')
plot(x, xx)
title("parabola")
show()