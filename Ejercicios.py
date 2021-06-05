# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 17:12:29 2021

@author: eljua
"""


# numerador = 7
# denominador = 2
# división = numerador/denominador
# print(división)

# num1 = 10
# print(num1)


# num1 += 5
# print(num1)


# num1 += numerador
# print(num1)

# unBool = True
# otroBool = False

# ambas = unBool and otroBool
# print(ambas)


# unaOrAmbas = unBool or otroBool
# print(unaOrAmbas)


# Creación de programa para requisitos para aplicación a subsidio
# subsidio 
# 1. Vivir en estratos 0, 1, 2 o 3.
# 2. Ganar hasta 2 salarios minimos
# 3. Vivir en zona rural

# estarto1, estrato2, estrato3 = 1,2,3

# estrato = estrato1 or estrato2 or estrato3
# salario < 2*905000

estrato = input("Escribe tu estrato en número ")
while (estrato.isnumeric() == False):
    estrato = input("Escribe tu estrato en número ")
estrato = int(estrato)

salario = input("Escribe tu salario en pesos sin puntos, comas, o caracteres especiales ")
while salario.isnumeric() == False:
    salario = input("Escribe tu salario en pesos sin puntos, comas, o caracteres especiales ")
print("Zona Rural = 1" + "\n" + "Zona Urbana = 2")

zona = input("Escribe el número asignado a tu zona ")
while (zona.isnumeric() == False) and (zona):
    zona = input("Escribe el número asignado a tu zona ")
    

if estrato <= 3:
    if salario > 1810000:
        if zona == 1:
            print("Cumples todos los requisitos")
    
    
        
