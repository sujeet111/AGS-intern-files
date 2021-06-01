# -*- coding: utf-8 -*-
"""
Created on Tue Jun  1 10:26:23 2021

@author: patil
"""

import pyodbc as db
import pandas as pd

conn = db.connect('Driver={SQL Server};''Server=DESKTOP-VI5MRAI\GAURAVPATIL;''Database=sample;''Trusted_Connection=yes;')
print("Read")
cursor = conn.cursor()
sql_query = pd.read_sql_query('select* from sampleinfo',conn)
#cursor.execute("select * from sampleinfo")
#for row in cursor:
  #  print(row)
print(sql_query)
print("Over")

          