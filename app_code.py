# This is a data cleaning application 

"""
Please create a python application that can take datasets and clean the data
- It should ask for datasets path and name
- it should check number of duplicats and remove all the duplicates 
- it should keep a copy of all the duplicates
- it should check for missing values 
- if any column that is numeric it should replace nulls with mean else it should drop that rows
- at end it should save the data as clean data and also return 
- duplicates records, clean_data 
"""

# importing dependencies

import pandas as pd
import numpy as np 
import os 
import time 
import openpyxl
import xlrd
import random

 # data_path = " "
 # data_name = " "


def data_cleaning_master(data_path, data_name):
    print("Thank you for giving the details!")
    
    sec=random.randint(1,4) # generating random number
    
    # print delay message 
    print(f"Please wait for{sec} Seconds! Checking file path")
    time.sleep(sec)
    
    # Checking if the path exists 
    if not os.path.exists(data_path):
        print("Incorrect Path! Try again with correct path ")
        return
    else:
        # Checking the file path 
        if data_path.endswith(".csv"):
            print("Dataset is csv!")
            data = pd.read_csv(data_path, encoding_errors="ignore")

        elif data_path.endswith(".xlsx"):  
            print("Dataset is an Excel file!")    
            data = pd.read_excel(data_path)
         
        else:
            print("Unknown file type")
            return
    # print delay message 
    sec=random.randint(1,4)
    print(f"Please wait for{sec} Seconds! Checking total columns and rows")
    time.sleep(sec)  
              
    # Showing the number of records 
    print(f"Dataset contains total rows: {data.shape[0]} \nDataset contains total columns: {data.shape[1]}")

    # Start cleaning data 
    
    # print delay message 
    sec=random.randint(1,4)
    print(f"Please wait for{sec} Seconds! Checking total duplicates")
    time.sleep(sec)
    
    # Checking duplicates
    duplicates = data.duplicated()
    total_duplicated = data.duplicated().sum()
    
    print(f"Dataset has total duplicate records: {total_duplicated}")
    
    
    # print delay message 
    sec=random.randint(1,4)
    print(f"Please wait for{sec} Seconds! Saving total duplicate rows")
    time.sleep(sec)

    # Storing duplicate records in another file 
    if total_duplicated > 0:
        duplicates_records = data[duplicates]
        duplicates_records.to_csv(f"{data_name}_duplicates.csv", index=None)
    
    # Deleting duplicates 
    df = data.drop_duplicates()


    # print delay message 
    sec=random.randint(1,4)
    print(f"Please wait for{sec} Seconds! Checking for missing values ")
    time.sleep(sec)

    # Finding missing values 
    total_missing_value = df.isnull().sum().sum()
    missing_values_by_columns = df.isnull().sum()
    print(f"Dataset has total missing values: {total_missing_value}")
    print(f"Dataset containing missing values by columns:\n{missing_values_by_columns}")

    # Dealing with missing values 
    # fillna --int , float
    # dropna-- any object
    
    # print delay message 
    sec=random.randint(1,4)
    print(f"Please wait for{sec} Seconds! Cleaning Datasets")
    time.sleep(sec)
    
    
    columns = df.columns
    for col in columns:
        if df[col].dtypes in (int, float):
            # Filling mean for numeric columns in all rows
            df[col] = df[col].fillna(df[col].mean())
        else:
            # Dropping the missing value records for non-numeric columns
            df.dropna(subset=[col], inplace=True)
    
    
    # print delay message 
    sec=random.randint(1,4)
    print(f"Please wait for{sec} Seconds! Exporting datasets")
    time.sleep(sec)
       
    # Data is cleaned 
    print(f"Congratulations!! Dataset is cleaned \nNumber of Rows: {df.shape[0]} \nNumber of columns: {df.shape[1]}")

    # Saving the cleaned dataset
    df.to_csv(f"{data_name}_Cleaned_Data.csv", index=None)
    print("Dataset is saved!")

if __name__ == "__main__" :
        # asking path and file name
    print("Welcome to Dataset Cleaning Master!")    
    data_path = input("Please enter dataset path : " ) 
    data_name = input("Please enter dataset name : " )
        
    #calling the function 
    data_cleaning_master(data_path,data_name)
