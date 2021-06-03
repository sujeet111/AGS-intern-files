# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 17:47:33 2021

@author: patil
"""
import pyodbc as db
import pandas as pd
import time as t

conn = db.connect('Driver={SQL Server};''Server=DESKTOP-VI5MRAI\GAURAVPATIL;''Database=sample;''Trusted_Connection=yes;')
c = conn.cursor()

def checktable(table_name):
    c = conn.cursor()
    try:
        #c.execute("SELECT 1 FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = N'"+table_name+"'")
        c.execute("SELECT * from "+table_name)
    except:
        print('Table Dosent exists.\n\n')
        new_table = conn.cursor()
        new_table.execute("CREATE TABLE "+table_name+"(NAME varchar(50),ID bigint,Price float,Discount float);");
        new_table.commit()
        new_table.close()
    finally:
        c.close()

checktable("Table_1")
checktable("Table_2")
checktable("Table_3")
    
data = pd.read_csv("C:\Office\AGS - Internship\AGS-intern-files\Gaurav\Assignment 6\\data1.csv")

cursor = conn.cursor()
old = t.time()

for row in data.itertuples():
    b = str(row.ID)
    if(b[0]=='4'):
        cursor.execute("INSERT into Table_1 values(?,?,?,?)",row.NAME,row.ID,row.Total_Amount,row.Total_Amount*0.02)
    elif(b[0]=='5'):
        cursor.execute("INSERT into Table_2 values(?,?,?,?)",row.NAME,row.ID,row.Total_Amount,row.Total_Amount*0.03)
    else:
        cursor.execute("INSERT into Table_3 values(?,?,?,?)",row.NAME,row.ID,row.Total_Amount,row.Total_Amount*0.04)
    cursor.commit()
    
cursor.close()
required = t.time()-old
'''
print("\n\nTable 1")
sql_query = pd.read_sql_query('select * from Table_1',conn)
print(sql_query)

print("\n\nTable 2")
sql_query = pd.read_sql_query('select * from Table_2',conn)
print(sql_query)

print("\n\nTable 3")
sql_query = pd.read_sql_query('select * from Table_3',conn)
print(sql_query)
'''
print("\n\nTime Required is : ",required)
conn.close()
  