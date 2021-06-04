import pyodbc
from datetime import date
studio = pyodbc.connect('Driver={SQL Server};''Server=DESKTOP-9T4GEVI;''Database=patil;''Trusted_Connection=yes;')
cursor = studio.cursor()
cursor2 = studio.cursor()
  
cursor.execute(" INSERT INTO STUD2(name,age) SELECT name,DATEDIFF(yy,STUD1.dob,GETDATE()) from STUD1")  
cursor2.execute("select * from STUD2")
for row in cursor2:
    print(row)

    # datediff( YY, bday.Date, GETDATE())