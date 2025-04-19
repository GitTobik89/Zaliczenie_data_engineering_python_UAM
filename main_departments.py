# -*- coding: utf-8 -*-
"""
Created on Sat Apr 19 12:16:38 2025

@author: sloms
"""

from CsvExtractor import CsvExtractor
from ParquetLoader import ParquetLoader
from Job import Job

def main_departments():
    input_path = "C:/Users/sloms/Desktop/BIG_DATA/Inżyniera_danych_python/zadanie/Zaliczenie_data_engineering_python_UAM/pracownicy.csv"
    output_path = "C:/Users/sloms/Desktop/BIG_DATA/Inżyniera_danych_python/zadanie/Zaliczenie_data_engineering_python_UAM/wynik_departments.parquet"

    csv_extractor = CsvExtractor(input_path)
    parquet_loader = ParquetLoader(output_path)

    df = csv_extractor.extract()
    department_counts = df.groupby('Departament')['ID'].count().reset_index()
    department_counts.columns = ['Departament', 'Liczba_pracownikow']

    job = Job(input_path, output_path, csv_extractor, None, parquet_loader)
    job.run(department_counts)

if __name__ == "__main__":
    main_departments()