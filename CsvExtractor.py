# -*- coding: utf-8 -*-
"""
Created on Fri Apr 18 17:05:27 2025

@author: sloms
"""

import pandas as pd
from os.path import exists

class CsvExtractor:
  def __init__(self, path):
    self.path = path

  def validate_path(self):
    return exists(self.path)

  def extract(self):
    return pd.read_csv(self.path)
