import pandas as pd
import pyodbc
import os

conn = pyodbc.connect('Driver={SQL Server};''Server=DESKTOP-CAFAM2K\SUJEETPATIL;''Database=Agsdb;''Trusted_Connection=yes;')

def process_table(dataset): 
    data1 = pd.read_csv(dataset,delimiter='|')
    cursor = conn.cursor()
    for row in data1.itertuples():
        cursor.execute("INSERT into Table_1 values(?,?,?,?)",row.NAME,row.ID,row.Total_Amount,row.Total_Amount*0.02)
        cursor.commit()
    cursor.close()
    conn.close()

def display_table(table):
    cursor1 = conn.cursor()
    cursor1.execute("select * from "+table)
    return cursor1