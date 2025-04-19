# -*- coding: utf-8 -*-
"""
Created on Sat Apr 19 12:13:02 2025

@author: sloms
"""

class Job:
    def __init__(self, input_path, output_path, CSV_Extractor, file_deduplicator, loader): #file_deduplicator is optional, changed the variable name file_deduplicator to deduplicator
        self.input_path = input_path
        self.output_path = output_path
        self.CSV_Extractor = CSV_Extractor
        self.deduplicator = file_deduplicator #assigned file_deduplicator to the correct attribute variable deduplicator
        self.loader = loader

    def run(self, data=None):  # Modified run to accept optional data
        if self.deduplicator: #if file_deduplicator is provided
            source_data = self.CSV_Extractor.extract()  # Remove self.input_path
            transformed_data = self.deduplicator.transform()  # Call transform without arguments
            self.loader.load(self.output_path, transformed_data) # changed order of arguments. path first, then data
        else: # if data is provided
            source_data = self.CSV_Extractor.extract()
            self.loader.load(self.output_path, data)