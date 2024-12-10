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

#Input land
user_country_input = input('Skriv inn et land: ')
#Input hovedstad
user_capital_input = input('Skriv inn hovedstad: ')
#Input innbyggere
user_population_input = input('Skriv inn antall innbyggere: ')

#Oppdater dictonary med ny verdi
data.update({user_country_input : [user_capital_input, user_population_input]})

#Skriv ut dictionary til konsollet
print(data)