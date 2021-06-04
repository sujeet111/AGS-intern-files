import pandas as pd
import pyodbc
data = pd.read_csv (r'C:\Users\Nikhil\Desktop\ags_intern\file.csv')
studio = pyodbc.connect('Driver={SQL Server};''Server=DESKTOP-9T4GEVI;''Database=patil;''Trusted_Connection=yes;')
cursor = studio.cursor()
cursor1 = studio.cursor()
data = pd.DataFrame(data, columns= ['Name','Country','Age'])

print(data.Name)

for row in data.itertuples():
    cursor.execute('INSERT INTO csv(Name, Country.Age)VALUES (?,?,?)',row.Name, row.Country,row.Age)
    studio.commit()
cursor.close()

cursor1.execute("select * from patil.dbo.people_info")
for row in cursor1:
    print(row)
cursor1.close()
studio.close()