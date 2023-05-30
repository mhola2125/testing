# -*- coding: utf-8 -*-
"""
Created on Mon May 29 20:18:20 2023

@author: Carlos Guevara
"""
import pandas as pd 
import numpy as np
# Grades
students = [ "Gissela", "Daniel", "Andres", "Sandra", "Rosalyn" ]
math     = [ 16, 14, 17, 17, 17 ]
english  = [ 16, 17, 19, 18, 15 ]
art      = [ 11, 17, 13, 14, 17 ]
ppp      =  [ 11, 17, 13, 14, 12 ]
Overall      =  [ "A", "B", "A+", "A", "B" ]

# Dictionary
diplomado = {'Students':students, 'Math':math, 'English':english, 'Art':art, 'PP':ppp, 'Total':Overall}
gradesA11 = pd.DataFrame( diplomado )
gradesA12 = gradesA11

data = {
    'Name': ['John', 'Jane', 'John', 'Jane', 'John'],
    'Subject': ['Math', 'Math', 'English', 'English', 'Math'],
    'date': [ "A", "A", "B", "B", "C" ],
    'Score1': [90, 85, 80, 95, 92],
    'Score2': [54, 31, 80, np.nan, 92],
    'Score3': [87,  np.nan, 74, 84, 70],
    'Score4': [86, 81, 66, np.nan, 89]
}
dataframe1 = pd.DataFrame(data)