# -*- coding: utf-8 -*-
"""
Created on Tue Jun  1 17:09:25 2021

@author: patil
"""
         
import pyodbc as db
from datetime import datetime

today = datetime.today()
print(today)
conn = db.connect('Driver={SQL Server};''Server=DESKTOP-VI5MRAI\GAURAVPATIL;''Database=sample;''Trusted_Connection=yes;')
print("Read")
cursor = conn.cursor()
cursor.execute("select * from sampleinfo")
for row in cursor:
    Dob = row.DOB
    Dob = datetime.strptime(Dob, '%Y-%m-%d')
    Age = today.date() - Dob.date()
    a = Age.days//365
    print(a)
    copy = conn.cursor()
    print(row.ID)
    print(row.NAME)
    print(row.SURNAME)
    print("Copying data from sample data to copy data")
    query = "insert into sample_copy values("+str(row.ID)+",'"+row.NAME+"','"+row.SURNAME+"',"+str(a)+")"
    copy.execute(query)
curso = conn.cursor()
curso.execute("select * from sample_copy")
for row in curso:
    print(row)
print("Over")
