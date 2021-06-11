import pandas as pd
import pyodbc
import os

conn = pyodbc.connect('Driver={SQL Server};''Server=localhost;''Database=agsdb;''UID = SA;''PWD = Bose2515;''Trusted_Connection=yes;')
';UID='+username+';PWD='+ password)
def process_table(dataset): 
    data1 = pd.read_csv(dataset,delimiter='|')
    cursor = conn.cursor()
    for row in data1.itertuples():
        cursor.execute("INSERT into tabledata values(?,?,?,?)",row.NAME,row.ID,row.Total_Amount)
        cursor.commit()
    cursor.close()
    conn.close()

def display_table(table):
    cursor1 = conn.cursor()
    cursor1.execute("select * from "+table)
    return cursor1