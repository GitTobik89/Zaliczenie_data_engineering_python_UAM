# -*- coding: utf-8 -*-
"""
Created on Sat Apr 19 13:41:16 2025

@author: sloms
"""

import pandas as pd
df = pd.read_parquet('C:/Users/sloms/Desktop/BIG_DATA/Inżyniera_danych_python/zadanie/Zaliczenie_data_engineering_python_UAM/wynik_departments.parquet')
df.to_csv('filename.csv')
print(df)