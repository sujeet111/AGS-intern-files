import pyodbc

conn = pyodbc.connect('Driver={SQL Server};''Server=DESKTOP-CAFAM2K\SUJEETPATIL;''Database=Agsdb;''Trusted_Connection=yes;')

mycursor = conn.cursor()
mycursor.execute("INSERT INTO table2 SELECT * FROM table1")

mycursor.execute("select * from table2")

query2 = mycursor.fetchall()
for i in query2:
    print(i)