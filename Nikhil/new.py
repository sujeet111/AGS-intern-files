import pyodbc
studio = pyodbc.connect('Driver={SQL Server};''Server=LENOVO-PC;''Database=master;''Trusted_Connection=yes;')
cursor = studio.cursor()


cursor.execute("SELECT * FROM patil")
for row in cursor:
    print(row)

