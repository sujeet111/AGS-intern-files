import pandas as pd
import pyodbc



conn = pyodbc.connect('Driver={SQL Server};''Server=DESKTOP-CAFAM2K\SUJEETPATIL;''Database=Agsdb;''Trusted_Connection=yes;')
mycursor = conn.cursor()

data = pd.read_csv("C:\Users\sujeet\Desktop\Projects\AGS\AGS-intern-files\Sujeet\person.csv")
print(data.Name)

for row in data.itertuples():
    mycursor.execute('INSERT INTO csv(name, country)VALUES (?,?)',row.Name, row.Country)
    conn.commit()

mycursor.execute("select * from csv")
for row in mycursor:
    print(row)
