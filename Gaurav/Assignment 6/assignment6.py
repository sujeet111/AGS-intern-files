# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 17:47:33 2021

@author: patil
"""
import pyodbc as db
import pandas as pd

conn = db.connect('Driver={SQL Server};''Server=DESKTOP-VI5MRAI\GAURAVPATIL;''Database=sample;''Trusted_Connection=yes;')
c = conn.cursor()
#c.execute("Drop Table Table_1")
#print("dropped")

def checktable(table_name):
    c = conn.cursor()
    try:
        #c.execute("SELECT 1 FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = N'"+table_name+"'")
        c.execute("SELECT * from "+table_name)
    except:
        print('Table Dosent exists.\n\n')
        new_table = conn.cursor()
        new_table.execute("CREATE TABLE "+table_name+"(NAME varchar(50),ID bigint,Price float);");
        new_table.commit()
        new_table.close()
    finally:
        c.close()

checktable("Table_1")
checktable("Table_2")
checktable("Table_3")
    
data = pd.read_csv("C:\Office\AGS - Internship\AGS-intern-files\Gaurav\Assignment 6\\data.csv")

cursor = conn.cursor()

for row in data.itertuples():
    b = str(row.ID)
    if(b[0]=='4'):
        a = row.Total_Amount - row.Total_Amount*0.02
        cursor.execute("INSERT into Table_1 values(?,?,?)",row.NAME,row.ID,a)
    elif(b[0]=='5'):
        a = row.Total_Amount - row.Total_Amount*0.03
        cursor.execute("INSERT into Table_2 values(?,?,?)",row.NAME,row.ID,a)
    else:
        a = row.Total_Amount - row.Total_Amount*0.04
        cursor.execute("INSERT into Table_3 values(?,?,?)",row.NAME,row.ID,a)
    cursor.commit()
    
cursor.close()

print("\n\nTable 1")
c = conn.cursor()
d = c.execute("select * from Table_1")
for row in d:
    print(row)
d=None
print("\n\nTable 2")
d = c.execute("select * from Table_2")
for row in d:
    print(row)
d=None
print("\n\nTable 3")
d = c.execute("select * from Table_3")
for row in d:
    print(row)
c.close()
conn.close()

    

    
    