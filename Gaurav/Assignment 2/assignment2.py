# -*- coding: utf-8 -*-
"""
Created on Tue Jun  1 14:48:08 2021

@author: patil
"""

import pyodbc as db

conn = db.connect('Driver={SQL Server};''Server=DESKTOP-VI5MRAI\GAURAVPATIL;''Database=sample;''Trusted_Connection=yes;')

c = conn.cursor()
c.execute("SELECT 1 FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = N'sample_copy'")

if c.fetchone()[0]==1 : {
	print('Table exists.')
}
else:
    print('Table Dosent exists.')
    create_table = conn.cursor()
    create_table.execute("CREATE TABLE sample_copy(ID int ,NAME varchar(50),SURNAME varchar(50));")
    
copy = conn.cursor()
print("Copying data from sample data to copy data")
copy.execute("INSERT INTO sample_copy(ID,NAME,SURNAME) SELECT ID,NAME,SURNAME FROM sampleinfo ")
new_cursor = conn.cursor()                                
new_cursor.execute("select * from sample_copy")                 
for row in new_cursor:
    print(row)
conn.close();

          