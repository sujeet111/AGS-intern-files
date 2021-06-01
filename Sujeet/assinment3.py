import pyodbc

conn = pyodbc.connect('Driver={SQL Server};''Server=DESKTOP-CAFAM2K\SUJEETPATIL;''Database=Agsdb;''Trusted_Connection=yes;')

mycursor = conn.cursor()
insertcursor = conn.cursor()
# mycursor.execute("INSERT INTO age_diaplay(name,age) Select name, datediff( YY, bday.Date, GETDATE()) as age from bday")

insertcursor.execute("INSERT INTO age_diaplay(name,age) Select name, datediff( YY, bday.Date, GETDATE()) from bday")
mycursor.execute("select * from age_diaplay")
for row in mycursor:
    print(row)