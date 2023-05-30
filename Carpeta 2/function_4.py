# -*- coding: utf-8 -*-
"""
Created on Mon May 29 20:19:10 2023

@author: Carlos Guevara
"""
import pandas as pd 
import numpy as np
    # =================================
    # Merge
data1 = {
    'ID': [1, 2, 3, 4, 5],
    'Name': ['John', 'Jane', 'Mike', 'Sara', 'Tom'],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Miami']}
df1 = pd.DataFrame(data1)
data2 = {
    'ID': [1, 2, 3, 4, 6],
    'Age': [25, 30, 35, 40, 45],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Seattle']}
df2 = pd.DataFrame(data2)

merged_df = pd.merge(df1, df2, on=['ID', 'City'], how = "left" , validate = "m:1" ).head()