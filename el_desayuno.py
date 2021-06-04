# -*- coding: utf-8 -*-
"""
Created on Fri Jun  4 12:06:29 2021

@author: eljua
"""

### Reto 1

#--------------------------------------------------------------------
## Descripción del reto "El Desayuno"

# Arepa
# Huevo
# Salchicha

## Input -> Cantidad de empleados que reservan el desayuno

## Output
 
# Cantidad de desayunos  = r = 1 * reservaciones
# Cantidad de arepas     = a = 1 * r
# Cantidad de huevos     = h = (2 * r) + 4
# Cantidad de salchichas = s = (r + h) / 5
#
#                              {s <= 20; e = "uno"}
# Cantidad de empleados  = e = {20 < s <= 30; e = "Dos"}
#                              {30 < s <= 50; e = "Tres"}
#                              {50 < s; e = "Cuatro"}

#--------------------------------------------------------------------

## Código sin ciclo

def desayuno():
    reservaciones = input("Escribe el número de reservaciones ")
    if (reservaciones.isnumeric() == True):
        reservaciones = int(reservaciones)
        arepas = reservaciones
        huevos = int((2*reservaciones) + 4)
        salchichas = int((reservaciones+huevos)/5)
        if salchichas <= 20:
            cantidad_empleados = "Uno "
        elif (20 < salchichas <= 30):
            cantidad_empleados = "Dos "
        elif (30 < salchichas <= 50):
            cantidad_empleados = "Tres "
        elif (salchichas > 50):
            cantidad_empleados = "Cuatro "
        print(str(arepas) + " " + str(huevos) + " " + str(salchichas) + "\n" + cantidad_empleados) 
    
desayuno()          

## Código con "while" 

# def desayuno():
#     reservaciones = input("Escribe el número de reservaciones ")
#     while (reservaciones.isnumeric() == False):
#         reservaciones = input("Escribe el número de reservaciones ")
#     reservaciones = int(reservaciones)
#     arepas = reservaciones
#     huevos = int((2*reservaciones) + 4)
#     salchichas = int((reservaciones+huevos)/5)
#     if salchichas <= 20:
#         cantidad_empleados = "Uno "
#     elif (20 < salchichas <= 30):
#         cantidad_empleados = "Dos "
#     elif (30 < salchichas <= 50):
#         cantidad_empleados = "Tres "
#     elif (salchichas > 50):
#         cantidad_empleados = "Cuatro "
#     print(str(arepas) + " " + str(huevos) + " " + str(salchichas) + "\n" + cantidad_empleados)

# desayuno()



            
            