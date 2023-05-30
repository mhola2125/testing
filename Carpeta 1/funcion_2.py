# -*- coding: utf-8 -*-
"""
Created on Mon May 29 20:17:50 2023

@author: Carlos Guevara
"""
pais_1 = [30,20,50,100,200,1] 

pais_2 = ["Perú",30,"Chile",20,"Argentina",50,"Brasil",100]

pais_3 = ["Perú",30,"Chile",20,["Argentina",50],["Brasil",100]]

    # Manipulacion
pais_1[1] = "Alemania" 
pais_2[1:4] = [20,40]
pais_1.append([1,"hola"])

    # =================================
    # Tuplas: Sin elementos de cierre
    # =================================
    # Util para funciones por que su estructura no cambia, se crean otras tuplas
tupla_1 = 3,8,2,5,"pais"
tupla_2 = tupla_1[0:2]
list_to_tupla = tuple(pais_1)
tupla_to_list = list(tupla_2)


    # =================================
    # Diccionarios
    # =================================
paises_dict1_1 = {"Colombia":45, "Chile":22, "Uruguay":55}    
paises_dict1_2 = {"Argentina":50, "Brasil":100, "Perú":30 } 
paises_dict1_3 = {"Colombia":45, "Chile":[22,44]}  