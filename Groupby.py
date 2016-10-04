# -*- coding: utf-8 -*-
"""
Created on Thu May  5 14:14:13 2016

@author: jmartel71
"""

import os
os.chdir('M:\City Energy Project\EEO Data Management\Scripts - Python\C_Datasets')
os.getcwd()

import pandas as pd
#SUM GAS DATA BY BUILDING AND PRINT TO EXCEL
gas_df = pd.read_csv('gas.csv', keep_default_na=False, na_values=[""], low_memory=False)
grouped = gas_df['Usage'].groupby(gas_df['PropertyName'])
grouped.sum().to_csv('output.csv')





