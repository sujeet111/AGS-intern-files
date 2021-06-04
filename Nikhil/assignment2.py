import pyodbc
studio = pyodbc.connect('Driver={SQL Server};''Server=DESKTOP-9T4GEVI;''Database=patil;''Trusted_Connection=yes;')
cursor = studio.cursor()

cursor.execute("INSERT INTO STUD1 SELECT * FROM STUD")   
cursor.execute("select * from stud1")
query= cursor.fetchall()
for i in query: 
    print(i)
