# -*- coding: utf-8 -*-
"""
Created on Tue Jun  8 13:04:56 2021

@author: patil
"""

import pyodbc as db
import pandas as pd
import time as t
import _thread

def checktable(table_name):
    conn = db.connect('Driver={SQL Server};''Server=DESKTOP-VI5MRAI\GAURAVPATIL;''Database=sample;''Trusted_Connection=yes;')
    c = conn.cursor()
    try:
        c.execute("SELECT * from "+table_name)
    except:
        print('Table Dosent exists.\n\n')
        new_table = conn.cursor()
        new_table.execute("CREATE TABLE "+table_name+"(NAME varchar(50),ID bigint,Price float,Discount float);");
        new_table.commit()
        new_table.close()
    finally:
        c.close()
        conn.close()

def executeNew1(dataset) :
    con = db.connect('Driver={SQL Server};''Server=DESKTOP-VI5MRAI\GAURAVPATIL;''Database=sample;''Trusted_Connection=yes;')

    print("Thread 1 starting time : ",t.time())
    #data1 = pd.read_csv("C:\Office\AGS - Internship\AGS-intern-files\Gaurav\Assignment 6\\"+dataset+".csv")
    data1 = pd.read_csv(dataset)
    data1 = data1.iloc[:,:5000]
    cursor = con.cursor()
    old = t.time()
    
    for row in data1.itertuples():
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
    print("\n\nTime Required for Thread 1 : ",required)
    con.close()

def executeNew2(dataset) :
    conn = db.connect('Driver={SQL Server};''Server=DESKTOP-VI5MRAI\GAURAVPATIL;''Database=sample;''Trusted_Connection=yes;')
    data = pd.read_csv(dataset)
    data = data.iloc[5000:,:]
    print("Thread 2 starting time : ",t.time())
    curso = conn.cursor()
    old1 = t.time()
    
    for row in data.itertuples():
        b = str(row.ID)
        if(b[0]=='4'):
            curso.execute("INSERT into Table_1 values(?,?,?,?)",row.NAME,row.ID,row.Total_Amount,row.Total_Amount*0.02)
        elif(b[0]=='5'):
            curso.execute("INSERT into Table_2 values(?,?,?,?)",row.NAME,row.ID,row.Total_Amount,row.Total_Amount*0.03)
        else:
            curso.execute("INSERT into Table_3 values(?,?,?,?)",row.NAME,row.ID,row.Total_Amount,row.Total_Amount*0.04)
        curso.commit()
        
    curso.close()
    required = t.time()-old1
    print("\n\nTime Required for Thread 2 : ",required)
    conn.close()

def executefile(dataset):  
        checktable("Table_1")
        checktable("Table_2")
        checktable("Table_3")

        e = t.time()

        _thread.start_new_thread(executeNew1,(dataset,))
        _thread.start_new_thread(executeNew2,(dataset,))

        print("time needed is ",t.time()-e)
        return 1
    
executefile("C:\Office\AGS - Internship\AGS-intern-files\Gaurav\Assignment 6\\Book1.csv")