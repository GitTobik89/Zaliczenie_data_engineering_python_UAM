# -*- coding: utf-8 -*-
"""
Created on Sat Apr 19 12:15:04 2025

@author: sloms
"""

import pandas as pd

class ParquetLoader:
      def __init__(self,path, engine='auto', compression='snappy'):
        self.path=path
        self.engine = engine
        self.compression = compression

      def load(self, path, data): # Added data as an argument
        return data.to_parquet(path,engine=self.engine, compression=self.compression)