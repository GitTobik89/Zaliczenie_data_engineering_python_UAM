# -*- coding: utf-8 -*-
"""
Created on Sat Apr 19 12:11:52 2025

@author: sloms
"""

import pandas as pd

class JsonLoader:
    def __init__(self, orient, index, lines):
        self.orient = orient
        self.index = index
        self.lines = lines

    def load(self, path, data):
        return data.to_json(path, orient=self.orient, index=self.index, lines=self.lines)