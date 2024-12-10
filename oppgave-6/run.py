# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 08:43:31 2024

@author: olmel6349
"""

import matplotlib.pyplot as plt
"""
Funksjonen 𝑓(𝑥)=−𝑥2−5
Input: x
"""
def calculate(x:int):
    return -x**2-5

#Liste med punkter for x-aksen
x_axis = []

#Liste med punkter for y-aksen
y_axis = []

#Looper fra -10 til 10 + 1 og populerer x_axis og y_axis listene
for x in range(-10, 10 + 1):
    x_axis.append(x) 
    y_axis.append(calculate(x))

#Plotter funksjonen
plt.plot(x_axis, y_axis)