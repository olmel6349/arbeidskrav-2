# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 08:43:31 2024

@author: olmel6349
"""
import math

"""
Variabel hvor mye pizza hver student spiser 
"""
AMOUNT_OF_PIZZA_EACH_STUDENT_EATS = 0.25

"""
Funksjon som regener ut hvor mye pizza man skal kjøpe inn uten bruk av math_ceil
Input: number_of_students
Output: antall pizza 
"""
def calculate_amount_of_pizza_needed(number_of_students:int):
    #Hvis det er mindre enn 4 studenter returner 1 pizza
    if(number_of_students <= 4):
        return 1
    
    #Antall studenter ganger variabel som holder hvor mange pizza hver student spiser
    amount = number_of_students * AMOUNT_OF_PIZZA_EACH_STUDENT_EATS
    
    #Hent ut tall etter desimal punktet
    numbers_after_decimal_point = amount - int(amount)
    
    #Hvis tallene bak komma er heltall returner antall som int
    if(numbers_after_decimal_point == 0):
        return int(amount)
        
    #Hvis tallene bak desimal er over eller større enn 0.5 rundes opp.
    if(numbers_after_decimal_point >= 0.5):
        return round(amount)
    
    #Hvis tallene bak desimal er under 0.5 rundes ned og legger til én.
    return round(amount) + 1


"""
Funksjon som regener ut hvor mye pizza man skal kjøpe inn med bruk av math.ceil
Input: number_of_students
Output: antall pizza som runder av til nærmeste int verdi ved bruk av math.ceil
"""
def calculate_amount_of_pizza_needed_with_math_ceil(number_of_stundents:int):
    amount = number_of_stundents * AMOUNT_OF_PIZZA_EACH_STUDENT_EATS
    return math.ceil(amount)

#Input
number_of_students = int(input('Skriv inn antall elever: '))

#Kalkuler og lagre i variabel
answer = calculate_amount_of_pizza_needed(number_of_students)

#Kalkuler og lagre i variabel ved bruk av math_ceil
#answer = calculate_amount_of_pizza_needed_with_math_ceil(number_of_students)

print(f"Det må kjøpes inn {answer} pizza")              