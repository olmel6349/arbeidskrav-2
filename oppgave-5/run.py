# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 08:43:31 2024

@author: olmel6349
"""

import math

"""
Hovedfunksjonen som regner ut Ytre» omkrets og areal
"""
def main(a:int, b:int):
    #Ytre omkrets
    hypotenuse = find_hypotenuse(a, b)
    
    radius = a / 2 # Halvparten av diameteren
    
    half_circle = calculate_circumference_circle(radius) / 2 #Halvsirkel
    
    #Grunnlinje + hypotenus + halvsirkel. Trenger ikke høyden til rettvinklet trekant her
    outer_circumference = b + hypotenuse + half_circle
    
    #Formaterer svaret ned til to desimaler
    outer_circumference_formated = "{:.2f}".format(outer_circumference)
    
    print(f"«Ytre» omkrets: {outer_circumference_formated}")
    
    #Areal
    area_half_circle = calculate_area_circle(radius) / 2 #Halvsirkel
    
    #Areal av rettvinklet trekant
    area_triangle = calculate_area_triangle(b, a)
    
    #Arealet av halvsirkel + arealet av rettvinklet trekant
    area_figurine = area_half_circle + area_triangle
    
    #Formaterer svaret ned til to desimaler
    area_figurine_formated = "{:.2f}".format(area_figurine)
    
    print(f"Areal: {area_figurine_formated}")

#Areal sirkel = math.pi*r**2
def calculate_area_circle(radius:int):
    return math.pi*radius**2

#Omkrets sirkel = 2*math.pi*r
def calculate_circumference_circle(radius:int):
    return math.pi*2*radius

#Areal trekant = (grunnlinje * hoyde) / 2
def calculate_area_triangle(b:int, a:int):
    return (b * a) / 2

#Finn legenden på hypotenusen
def find_hypotenuse(a:int, b:int) :
    return math.sqrt(a**2 + b**2)

#Kjør utregning av Ytre» omkrets og areal
main(2, 3)