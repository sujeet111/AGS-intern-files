# -*- coding: utf-8 -*-
"""
Created on Tue Jun  1 14:48:08 2021

@author: patil
"""

import pyodbc as db

conn = db.connect('Driver={SQL Server};''Server=DESKTOP-VI5MRAI\GAURAVPATIL;''Database=sample;''Trusted_Connection=yes;')
cursor = conn.cursor()
cursor.execute("select * into copy_data from sampleinfo")      # Making new table and copying values of previous record
new_cursor = conn.cursor()                                     # Created new cursor
new_cursor.execute("select * from copy_data")                  # Displaying copied table data 
for row in new_cursor:
    print(row)
print("Over")

          