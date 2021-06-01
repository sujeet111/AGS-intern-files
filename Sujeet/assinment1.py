import pyodbc

conn = pyodbc.connect('Driver={SQL Server};''Server=DESKTOP-CAFAM2K\SUJEETPATIL;''Database=Agsdb;''Trusted_Connection=yes;')

cursor = conn.cursor()
cursor.execute("select * from table1")
for row in cursor:
    print(row)