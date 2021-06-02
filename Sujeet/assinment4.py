import pandas as pd
import pyodbc



conn = pyodbc.connect('Driver={SQL Server};''Server=DESKTOP-CAFAM2K\SUJEETPATIL;''Database=Agsdb;''Trusted_Connection=yes;')
mycursor = conn.cursor()

data = pd.read_csv(r'C:\Users\sujeet\Desktop\Projects\AGS\AGS-intern-files\Sujeet\person.csv')
df = pd.DataFrame(data, columns= ['Name','Country'])

for row in df.itertuples():
    mycursor.execute('INSERT INTO csv(name, country)VALUES (?,?)',row.Name, row.Country)
    conn.commit()

mycursor.execute("select * from csv")
for row in mycursor:
    print(row)
