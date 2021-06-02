# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 15:18:47 2021

@author: patil
"""

import pyodbc as db
import pandas as pd

conn = db.connect('Driver={SQL Server};''Server=DESKTOP-VI5MRAI\GAURAVPATIL;''Database=sample;''Trusted_Connection=yes;')
#c = conn.cursor()
#c.execute("Drop Table Table_1")
#print("dropped")

def checktable(table_name):
    c = conn.cursor()
    try:
        c.execute("SELECT 1 FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = N'"+table_name+"'")
        if c.fetchone()[0]==1 : {
        	print('Table exists.\n\n')
        }    
    except:
        print('Table Dosent exists.\n\n')
        new_table = conn.cursor()
        new_table.execute("CREATE TABLE "+table_name+"(NAME varchar(50),ID bigint);");
        new_table.commit()
        new_table.close()
    finally:
        c.close()

checktable("Table_1")
checktable("Table_2")
checktable("Table_3")
    
data = pd.read_csv("C:\Office\AGS - Internship\AGS-intern-files\Gaurav\Assignment 5\\data.csv")

cursor = conn.cursor()

for row in data.itertuples():
    b = str(row.ID)
    if(b[0]=='4'):
        cursor.execute("INSERT into Table_1 values(?,?)",row.NAME,row.ID)
    elif(b[0]=='5'):
        cursor.execute("INSERT into Table_2 values(?,?)",row.NAME,row.ID)
    else:
        cursor.execute("INSERT into Table_3 values(?,?)",row.NAME,row.ID)
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

    

    
    