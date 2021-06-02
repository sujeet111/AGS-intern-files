# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 10:57:16 2021

@author: patil
"""

import pandas as pd
import pyodbc as db     

data = pd.read_csv("C:\Office\AGS - Internship\AGS-intern-files\Gaurav\Assignment 4\\realestate.csv")
print(data.city)

conn = db.connect('Driver={SQL Server};''Server=DESKTOP-VI5MRAI\GAURAVPATIL;''Database=sample;''Trusted_Connection=yes;')

c = conn.cursor()

c.execute("SELECT 1 FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = N'Data_Table'")
print(c)

if c.fetchone()[0]==1 : {
	print('Table exists.')
}
else:
    print('Table Dosent exists.')
    c.execute('''CREATE TABLE Data_Table(Address varchar(5000),
                         City varchar(50),
                         Bedroom int,
                         Bathroom int,
                         Sq_Ft float,
                         price longint''');
    c.commit()

c.close()

cursor = conn.cursor()

for row in data.itertuples():
    print(row)
    cursor.execute("INSERT into Data_Table values(?,?,?,?,?,?)",row.street,row.city,row.beds,row.baths,row.sq__ft,row.price)
    cursor.commit()

cursor.close()

curso = conn.cursor()
curso.execute("select * from Data_Table with(nolock)")
for row in curso:
    print(row)

curso.close()
conn.close()