# -*- coding: utf-8 -*-
"""
Created on Thu Jun  3 18:30:44 2021

@author: patil
"""

from tkinter import *
from tkinter import filedialog
import time as t

import pyodbc as db
import pandas as pd
conn = db.connect('Driver={SQL Server};''Server=DESKTOP-VI5MRAI\GAURAVPATIL;''Database=sample;''Trusted_Connection=yes;')
c = conn.cursor()

def checktable(table_name):
    c = conn.cursor()
    try:
        #c.execute("SELECT 1 FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = N'"+table_name+"'")
        c.execute("SELECT * from "+table_name)
    except:
        print('Table Dosent exists.\n\n')
        new_table = conn.cursor()
        new_table.execute("CREATE TABLE "+table_name+"(NAME varchar(50),ID bigint,Price float,Discount float);");
        new_table.commit()
        new_table.close()
    finally:
        c.close()

def execute(filepath):
    checktable("Table_1")
    checktable("Table_2")
    checktable("Table_3")
        
    data = pd.read_csv(filepath+"\data1.csv")
    
    cursor = conn.cursor()
    old = t.time()
    
    for row in data.itertuples():
        b = str(row.ID)
        if(b[0]=='4'):
            cursor.execute("INSERT into Table_1 values(?,?,?,?)",row.NAME,row.ID,row.Total_Amount,row.Total_Amount*0.02)
        elif(b[0]=='5'):
            cursor.execute("INSERT into Table_2 values(?,?,?,?)",row.NAME,row.ID,row.Total_Amount,row.Total_Amount*0.03)
        else:
            cursor.execute("INSERT into Table_3 values(?,?,?,?)",row.NAME,row.ID,row.Total_Amount,row.Total_Amount*0.04)
        cursor.commit()
        
    cursor.close()
    required = t.time()-old
    
    print("\n\nTable 1")
    df = pd.read_sql_query('select * from Table_1',conn)
    df.to_csv (filepath+"\Table_1.csv", index = False, header=True)
    
    print("\n\nTable 2")
    df = pd.read_sql_query('select * from Table_2',conn)
    df.to_csv (filepath+"\Table_2.csv", index = False, header=True)
    
    print("\n\nTable 3")
    df = pd.read_sql_query('select * from Table_3',conn)
    df.to_csv (filepath+"\Table_3.csv", index = False, header=True)
    
    print("\n\nTime Required is : ",required)
    conn.close()
  

def openFile():
    filepath = filedialog.askdirectory()
    execute(filepath)
    print(filepath)
  
window = Tk()
button = Button(text="",command=openFile())
button.pack()
window.mainloop()