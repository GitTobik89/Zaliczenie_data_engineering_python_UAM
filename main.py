# -*- coding: utf-8 -*-
"""
Created on Fri Apr 18 17:05:27 2025

@author: sloms
"""

from CsvExtractor import CsvExtractor
from Deduplicator import Deduplicator
from JsonLoader import JsonLoader
from Job import Job


def main():
    input_path = "C:/Users/sloms/Desktop/BIG_DATA/Inżyniera_danych_python/zadanie/Zaliczenie_data_engineering_python_UAM/pracownicy.csv"
    output_path = "C:/Users/sloms/Desktop/BIG_DATA/Inżyniera_danych_python/zadanie/Zaliczenie_data_engineering_python_UAM/wynik_json.json"

    csv_extractor = CsvExtractor(input_path)
    file_deduplicator = Deduplicator(input_path,["Imię"])
    json_loader = JsonLoader("records", False, True)

    job = Job(input_path, output_path, csv_extractor, file_deduplicator, json_loader)
    job.run()

if __name__ == "__main__":
    main()
    
    
    
    