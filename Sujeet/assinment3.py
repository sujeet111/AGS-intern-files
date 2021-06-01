import pyodbc

conn = pyodbc.connect('Driver={SQL Server};''Server=DESKTOP-CAFAM2K\SUJEETPATIL;''Database=Agsdb;''Trusted_Connection=yes;')

mycursor = conn.cursor()
mycursor.execute("INSERT INTO age_diaplay(name , age) Select name, datediff( YY, Date, GETDATE()) as age from bday")

mycursor.execute("select * from age_display")
for row in mycursor:
    print(row)