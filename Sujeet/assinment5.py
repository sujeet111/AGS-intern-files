import pandas as pd
import pyodbc

path = r'C:\Users\sujeet\Desktop\Projects\AGS\AGS-intern-files\Sujeet\person.csv'

conn = pyodbc.connect('Driver={SQL Server};''Server=DESKTOP-CAFAM2K\SUJEETPATIL;''Database=Agsdb;''Trusted_Connection=yes;')
data = pd.read_csv(r"C:\Users\sujeet\Desktop\Projects\AGS\AGS-intern-files\Sujeet\data.csv")
mycursor = conn.cursor()

def checktable(table_name):
    c = conn.cursor()
    try:
        c.execute("SELECT 1 FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = N'"+table_name+"'")
        if c.fetchone()[0]==1 : {
        	print('Table exists.\n\n')
        }    
    except:
        print('Table Dosent exists.\n\n')
        new_table = conn.cursor()
        new_table.execute("CREATE TABLE "+table_name+"(NAME varchar(50),ID bigint);");
        new_table.commit()
        new_table.close()
    finally:
        c.close()

checktable("Table_1")
checktable("Table_2")
checktable("Table_3")

for row in data.itertuples():
    var = str(row.ID)
    if var[0] == 4:
        mycursor.execute('INSERT INTO table1(name, id)VALUES (?,?)',row.Name, row.ID)
        mycursor.commit()
    elif var[0] == 5:
        mycursor.execute('INSERT INTO table1(name, id)VALUES (?,?)',row.Name, row.ID)
        mycursor.commit()
    elif var[0] == 6:
        mycursor.execute('INSERT INTO table1(name, id)VALUES (?,?)',row.Name, row.ID)
        mycursor.commit()
mycursor.close()

mycursor1 = conn.cursor()
mycursor1.execute("select * from table_1")
for row in mycursor1:
    print(row)
mycursor1.close()
mycursor2 = conn.cursor()
mycursor2.execute("select * from table_2")
for row in mycursor2:
    print(row)
mycursor2.close()
mycursor3 = conn.cursor()
mycursor3.execute("select * from table_3")
for row in mycursor3:
    print(row)
mycursor3.close()
conn.close()

