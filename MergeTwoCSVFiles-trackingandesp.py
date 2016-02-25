# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 15:47:23 2016

@author: jmartel71
"""

import os
os.chdir('C:/Users/jmartel71/Documents/Python Scripts/C_Datasets')
os.getcwd()

import pandas as pd
tracking_df = pd.read_csv('tracking.csv', keep_default_na=False, na_values=[""])
espexport_df = pd.read_csv('espexport.csv', keep_default_na=False, na_values=[""])
#inner join using unique identifier
merged_inner = pd.merge(left=tracking_df,right=espexport_df, left_on='display_name', right_on='Building')
merged_inner.to_csv('merged.csv')
