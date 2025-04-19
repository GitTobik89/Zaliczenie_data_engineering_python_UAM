# -*- coding: utf-8 -*-
"""
Created on Sat Apr 19 12:15:44 2025

@author: sloms
"""


from CsvExtractor import CsvExtractor
from Deduplicator import Deduplicator
from ParquetLoader import ParquetLoader
from Job import Job


def main_parquet():
    input_path = "C:/Users/sloms/Desktop/BIG_DATA/Inżyniera_danych_python/zadanie/Zaliczenie_data_engineering_python_UAM/pracownicy.csv"
    output_path = "C:/Users/sloms/Desktop/BIG_DATA/Inżyniera_danych_python/zadanie/Zaliczenie_data_engineering_python_UAM/wynik_parquet.parquet"

    csv_extractor = CsvExtractor(input_path)
    file_deduplicator = Deduplicator(input_path, ["Imię"])
    parquet_loader = ParquetLoader(output_path)

    job = Job(input_path, output_path, csv_extractor, file_deduplicator, parquet_loader)
    job.run()

if __name__ == "__main__":
    main_parquet()