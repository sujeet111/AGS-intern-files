# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 10:57:16 2021

@author: patil
"""

import pandas as pd
import pyodbc as db

data = pd.read_csv("C:\Office\AGS - Internship\AGS-intern-files\Gaurav\Assignment 4\data.txt")
print(data.ID)

#df = pd.DataFrame(data, columns= ['ID','Name','Surname','Age'])

conn = db.connect('Driver={SQL Server};''Server=DESKTOP-VI5MRAI\GAURAVPATIL;''Database=sample;''Trusted_Connection=yes;')

cursor = conn.cursor()

for row in data.itertuples():
    print(row)
    cursor.execute("INSERT into sample_copy values("+str(row.ID)+",'"+row.Name+"','"+row.Surname+"',"+str(row.Age)+")")
    cursor.commit()

cursor.close()

curso = conn.cursor()
curso.execute("select * from sample_copy with(nolock)")
for row in curso:
    print(row)

curso.close()
conn.close()