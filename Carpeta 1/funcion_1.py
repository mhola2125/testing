# -*- coding: utf-8 -*-
"""
Created on Mon May 29 20:16:13 2023

@author: Carlos Guevara
"""

pais_1 = [30,20,50,100,200,1] 

pais_2 = ["Perú",30,"Chile",20,"Argentina",50,"Brasil",100]

pais_3 = ["Perú",30,"Chile",20,["Argentina",50],["Brasil",100]]

    # Indexacion de listas
a1 = pais_1[0]    
a2 = pais_1[1]
a3 = pais_2[-1]
a4 = pais_2[-2]
a5 = pais_3[4][0]

b1 = pais_3[0:1] # [incluye:Noincluye] <- IMPORTANTISIMO
b2 = pais_3[:4] 
b3 = pais_3[0:2]
print("hola mundo")
print("adios mundo")
print("adios mundo")
