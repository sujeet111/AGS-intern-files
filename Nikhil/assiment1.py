import pyodbc
studio = pyodbc.connect('Driver={SQL Server};''Server=DESKTOP-9T4GEVI;''Database=nikhil;''Trusted_Connection=yes;')
cursor = studio.cursor()


cursor.execute("SELECT * FROM patil")
for row in cursor:
    print(row)

