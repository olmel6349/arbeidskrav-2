# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 08:43:31 2024

@author: olmel6349
"""

import numpy as np 

"""
Funksjon som regner ut radiantallet til vinkelen
Input: gradtallet
"""
def calculate_vrad(v_grad):
    return v_grad*np.pi/180

#Input
v_grad = float(input('Skriv inn gradtallet: ' ))

#Variabel med svaret
v_rad = calculate_vrad(v_grad)

print(f"Resultat: {v_rad}")
