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
cursor.execute("select * from sampleinfo with(nolock)")
for row in cursor:
    Dob = row.DOB
    Dob = datetime.strptime(Dob, '%Y-%m-%d')
    Age = today.date() - Dob.date()
    a = Age.days//365
    print("Copying data from sample data to copy data")
    copy = conn.cursor()
    query = "insert into sample_copy values("+str(row.ID)+",'"+row.NAME+"','"+row.SURNAME+"',"+str(a)+")"
    #print(query)
    copy.execute(query)
conn.commit()
curso = conn.cursor()
curso.execute("select * from sample_copy with(nolock)")
for row in curso:
    print(row)
print("Over")

conn.close()