# -*- coding: utf-8 -*-
"""
Created on Fri Apr 18 17:05:27 2025

@author: sloms
"""

import pandas as pd

class Deduplicator:
    def __init__(self, path,columns_to_deduplication):
        self.columns_to_deduplication = columns_to_deduplication
        self.path = path
        self.df = pd.read_csv(self.path)

    def transform(self) -> pd.DataFrame:
        return self.df[self.columns_to_deduplication].drop_duplicates()