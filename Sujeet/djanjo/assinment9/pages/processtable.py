import pandas as pd
import pyodbc
import os

conn = pyodbc.connect('Driver={SQL Server};''Server=DESKTOP-RPK4555;''Database=agsdb;''Trusted_Connection=yes;')
def process_table(dataset): 
    conn = pyodbc.connect('Driver={SQL Server};''Server=DESKTOP-RPK4555;''Database=agsdb;''Trusted_Connection=yes;')
    data1 = pd.read_csv(dataset,delimiter='|')
    cursor = conn.cursor()
    for row in data1.itertuples():
        cursor.execute("INSERT into tabledata values(?,?,?)",row.NAME,row.ID,row.Total_Amount)
        cursor.commit()
    cursor.close()
    conn.close()

def display_table(table):
    conn1 = pyodbc.connect('Driver={SQL Server};''Server=DESKTOP-RPK4555;''Database=agsdb;''Trusted_Connection=yes;')
    cursor1 = conn1.cursor()
    cursor1.execute("select * from "+table)
    return cursor1