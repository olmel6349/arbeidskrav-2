# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 08:43:31 2024

@author: olmel6349
"""

"""
Funksjon som regner ut hvilket år du er født
Input: int
"""
def calculate_age(age:int):
    return 2024 - age 

#Input
age_input = int(input('Hvilket år er du født? ') )

#Kjør funksjonen
age_result = calculate_age(age_input)

#Printer ut svaret
print(f"Du er {age_result} år gammel")