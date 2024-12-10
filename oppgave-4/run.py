# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 08:43:31 2024

@author: olmel6349
"""

"""
Python dictonary med Land som nøkkel og array med hovedsted og innbyggere som verdi
"""
data = {
    "Norge" : ["Oslo", 0.634],
    "England" : ["London", 8.982],
    "Frankrike" : ["Paris", 2.161],
    "Italia" : ["Roma", 2.873]
}

#Input
user_input = input('Skriv inn et land: ')

#Henter ut landet brukeren skriver inn.
if user_input in data:
    country = data.get(user_input)
    print(f"{country[0]} er hovedstaden i {user_input} og det er {country[1]} mill. innbyggere i {country[0]}")
else:
    print(f"Vi har ikke informasjon om landet: {user_input}")