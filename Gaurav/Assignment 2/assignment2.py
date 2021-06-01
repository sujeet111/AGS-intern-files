# -*- coding: utf-8 -*-
"""
Created on Tue Jun  1 14:48:08 2021

@author: patil
"""

import pyodbc as db

conn = db.connect('Driver={SQL Server};''Server=DESKTOP-VI5MRAI\GAURAVPATIL;''Database=sample;''Trusted_Connection=yes;')


#c.execute("SELECT 1 FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = N'sample_copy'")
"""
if c.fetchone()[0]==1 : {
	print('Table exists.')
}
else:
    print('Table Dosent exists.')
    create_table = conn.cursor()
    create_table.execute("CREATE TABLE sample_copy(ID int ,NAME varchar(50),SURNAME varchar(50));")
    """
print("Copying data from sample data to copy data")
copy = conn.cursor()
copy.execute("INSERT INTO sample_copy(ID,NAME,SURNAME) SELECT ID,NAME,SURNAME FROM sampleinfo ");
new_cur = conn.cursor()
new_cur.execute("select * from sample_copy")                 
for row in new_cur:
    print(row)
conn.commit()
conn.close();

          