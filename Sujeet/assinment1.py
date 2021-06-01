import pyodbc
#https://towardsdatascience.com/sql-server-with-python-679b8dba69fa
conn = pyodbc.connect('Driver={SQL Server};''Server=DESKTOP-CAFAM2K\SUJEETPATIL;''Database=Agsdb;''Trusted_Connection=yes;')

cursor = conn.cursor()
cursor.execute("select * from table1")
for row in cursor:
    print(row)