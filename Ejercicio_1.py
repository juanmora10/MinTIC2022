# -*- coding: utf-8 -*-
"""
Created on Fri Jun  4 19:59:53 2021

@author: eljua
"""

# Leer Input:
# Número de Cédula
# Salario básico
# Año vinculación

# Output
# Número de Cédula 
# Salario Neto


def salario_neto():
    cedula = input("Escribe tu número de cédula ")
    # while (cedula.isnumeric() == False):
    #     cedula = input("Escribe tu número de cédula ")
 
    salario_basico = input("Escribe tu salario en pesos sin puntos, comas, o caracteres especiales ")
    # while salario_basico.isnumeric() == False:
    #     salario_basico = input("Escribe tu salario en pesos sin puntos, comas, o caracteres especiales ")
    salario_basico = int(salario_basico)
    
    año_vinculacion = input("Escribe el año de vinculación ")
    # while (año_vinculacion.isnumeric() == False):
    #     año_vinculacion = input("Escribe el año de vinculación ")
    año_vinculacion = int(año_vinculacion)
    
    if salario_basico>1200000 and año_vinculacion > 1990:
        descuento = 0.08
    elif salario_basico<550000 or año_vinculacion == 1990:
        descuento = 0.02
    else:
        descuento = 0.05
    
    print("Su cédula es: " + cedula + " " + "\n" + 
          "Su salario neto es: " + str(salario_basico*(1-descuento)))
    
salario_neto()
    
    
    
    
    
    
    
    
    
        
        
        
        
        