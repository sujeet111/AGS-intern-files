# -*- coding: utf-8 -*-
"""
Created on Thu Jun  3 16:07:39 2021

@author: patil
"""
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 17:47:33 2021

@author: patil
"""
import pyodbc as db
import pandas as pd
import time as t
import threading as td
import multiprocessing
import _thread

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

#checktable("Table_1")
#checktable("Table_2")
#checktable("Table_3")

def executeNew1(dataset) :
    con = db.connect('Driver={SQL Server};''Server=DESKTOP-VI5MRAI\GAURAVPATIL;''Database=sample;''Trusted_Connection=yes;')

    print("Thread 1 starting time : ",t.time())
    data1 = pd.read_csv("C:\Office\AGS - Internship\AGS-intern-files\Gaurav\Assignment 6\\"+dataset+".csv")
    
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
    '''
    print("\n\nTable 1")
    sql_query = pd.read_sql_query('select * from Table_1',conn)
    print(sql_query)
    
    print("\n\nTable 2")
    sql_query = pd.read_sql_query('select * from Table_2',conn)
    print(sql_query)
    
    print("\n\nTable 3")
    sql_query = pd.read_sql_query('select * from Table_3',conn)
    print(sql_query)
    '''
    print("\n\nTime Required for Thread 1 : ",required)
    con.close()

def executeNew2(dataset) :
    conn = db.connect('Driver={SQL Server};''Server=DESKTOP-VI5MRAI\GAURAVPATIL;''Database=sample;''Trusted_Connection=yes;')
    print("Thread 2 starting time : ",t.time())
    data = pd.read_csv("C:\Office\AGS - Internship\AGS-intern-files\Gaurav\Assignment 6\\"+dataset+".csv")
    
    curso = conn.cursor()
    old = t.time()
    
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
    required = t.time()-old
    '''
    print("\n\nTable 1")
    sql_query = pd.read_sql_query('select * from Table_1',conn)
    print(sql_query)
    
    print("\n\nTable 2")
    sql_query = pd.read_sql_query('select * from Table_2',conn)
    print(sql_query)
    
    print("\n\nTable 3")
    sql_query = pd.read_sql_query('select * from Table_3',conn)
    print(sql_query)
    '''
    print("\n\nTime Required for Thread 2: ",required)
    conn.close()
  
e = t.time()
#t1 = td.Thread(target=executeNew1("Book1"))
#t2 = td.Thread(target=executeNew2("Book2"))
_thread.start_new_thread( executeNew1,("Book1",) )
_thread.start_new_thread( executeNew2,("Book2",) )
#p1 = multiprocessing.Process(target=executeNew1("Book1"))
#p2 = multiprocessing.Process(target=executeNew2, args=("Book2"))
    # starting thread 1

#t1.start()
    # starting thread 2
#t2.start()
  
    # wait until thread 1 is completely executed
#t1.join()
    # wait until thread 2 is completely executed
#t2.join()
print("time needed is ",t.time()-e)
conn.close()
    # both threads completely executed
print("Done!")