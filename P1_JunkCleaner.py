import random
import os
import xlrd
import openpyxl
import time
import numpy as np
import pandas as pd


def Cleaner(data_path, data_name):

    print("Thank you for providing your Data.\nProcessing the Results >>>>>>>>>>>>>>>>>>>>---->>>>>>>>>>>>>>>>")

    sec = random.randint(1, 3)  # generating a random number

    print(
        f'Please {sec}secs more >>>>>>>>>>>>>>>>------------------------------->>>>>>>>>>>>>>>>')
    time.sleep(sec)

    if not os.path.exists(data_path):
        print("Incorrect!!!-----Please Enter the correct path for the file!!")
        return
    else:
        if data_path.endswith(".csv"):
            print('Your file in CSV format')
            data = pd.read_csv(data_path, encoding_errors="ignore")

        elif data_path.endswith(".xlsx"):
            print('Your file is in Excel format')
            data = pd.read_excel(data_path)
        else:
            print("Unknown File type")
            return

    sec1 = random.randint(1, 4)
    print(
        f'We value your time, Please {sec1}secs more >>>>>>>>>>>>>>>>>>>>>---------------------->>>>>>>>>>>>>>>>')
    time.sleep(sec1)
    # Showing Number of Records
    print(
        f'\n\nDataset contain total rows: {data.shape[0]}\nDataset contains total columns: {data.shape[1]}')
    print(f"First 10 rows of data\n{data.head(10)}")

    # Cleaning Process
    duplicates = data.duplicated()
    total_duplicate = data.duplicated().sum()

    print(f'The total number of duplicate values: {total_duplicate}')
    sec2 = random.randint(1, 5)
    print(
        f'\nWe value your time, Please {sec2}secs more >>>>>>>>>>>>>>>>>>---------------------------------->>>>>>>>')
    time.sleep(sec2)

    # Saving The Data
    if total_duplicate > 0:
        duplicate_records = data[duplicates]
        duplicate_records.to_csv(f'{data_name}_duplicates.csv', index=None)

    df = data.drop_duplicates()

    total_missing_value = df.isnull().sum().sum()
    column_missing_value = df.isnull().sum()

    print(f'\nDataset has Total missing value: {total_missing_value}')
    print(
        f'Dataset contains missing values by columns\n{column_missing_value}')

    # Dealing with missing values:
    # fillna-- For Integers and float
    # dropna-- Other onjects

    columns = df.columns

    for col in columns:
        if df[col].dtype in (float, int):
            df[col] = df[col].fillna(round(df[col].mean()))

        else:
            df = df.dropna(subset=[col])

    sec4 = random.randint(1, 4)
    print(
        f'\nWe value your time, Please {sec4}secs more >>>>>>>>>>>>>>>>>----------------------------->>>>>>>>>>>\n')
    time.sleep(sec4)
    print(
        f"Congrats! Dataset is cleaned!\nNumber of Rows:{df.shape[0]}\nNumber of colums:{df.shape[1]}")

    print(
        f'--------------Data Statistics----------------------\n{df.describe()}\n\n')
    print(df.info())

    df.to_csv(f'{data_name}_Cleaned_Dataset.csv', index=None)
    print('Cleaned Dataset Saved in your memory location')


if __name__ == "__main__":
    while True:
        val = int(input('''
        Press 1 <<>> To Continue
        Press 9 <<>> To Exit
        Enter YOUR Choice >>> '''))
        if val == 1:
            print(
                "------------- Welcome to the Data Cleaner Application--------------\n**Please be Careful\n")
            data_path = input("Please provide File path: ")
            data_name = input("Please provide New_Dataset name: ").capitalize()

            Cleaner(data_path, data_name)
        else:
            print("Thank You!! Visit Again")
            break
