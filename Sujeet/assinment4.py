import pandas as pd
import pyodbc

path = r'C:\Users\sujeet\Desktop\Projects\AGS\AGS-intern-files\Sujeet\person.csv'

conn = pyodbc.connect('Driver={SQL Server};''Server=DESKTOP-CAFAM2K\SUJEETPATIL;''Database=Agsdb;''Trusted_Connection=yes;')
mycursor = conn.cursor()
mycursor2 = conn.cursor()

data = pd.read_csv("C:\Users\sujeet\Desktop\Projects\AGS\AGS-intern-files\Sujeet\person.csv")
print(data.Name)

for row in data.itertuples():
    mycursor.execute('INSERT INTO csv(name, country)VALUES (?,?)',row.Name, row.Country)
    mycursor.commit()
mycursor.close()

mycursor2.execute("select * from csv")
for row in mycursor2:
    print(row)
mycursor2.close()
conn.close()
