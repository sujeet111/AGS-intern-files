import pandas as pd
import pyodbc

conn = pyodbc.connect('Driver={SQL Server};''Server=DESKTOP-CAFAM2K\SUJEETPATIL;''Database=Agsdb;''Trusted_Connection=yes;')
data = pd.read_csv(r"C:\Users\sujeet\Desktop\Projects\AGS\AGS-intern-files\Sujeet\data.csv")
mycursor = conn.cursor()

for row in data.itertuples():
    var = str(row.ID)
    if var[0] == '4':
        amount = int(row.Total_Amount) - (int(row.Total_Amount) * 2 / 100)
        mycursor.execute('INSERT INTO Table_1(NAME, ID, Total_Amount, discount)VALUES (?,?,?,?)',row.NAME, row.ID, amount, int(row.Total_Amount) * 2 / 100)

    elif var[0] == '5':
        amount = int(row.Total_Amount) - (int(row.Total_Amount) * 3 / 100)      
        mycursor.execute('INSERT INTO Table_2(NAME, ID, Total_Amount, discount)VALUES (?,?,?,?)',row.NAME, row.ID, amount , int(row.Total_Amount) * 3 / 100)

    elif var[0] == '6':
        amount = int(row.Total_Amount) - (int(row.Total_Amount) * 4 / 100)
        mycursor.execute('INSERT INTO Table_3(NAME, ID, Total_Amount, discount)VALUES (?,?,?,?)',row.NAME, row.ID, amount, int(row.Total_Amount) * 4 / 100)
    else:
       print("pass")
mycursor.close()

print("Table 1")
mycursor1 = conn.cursor()
mycursor1.execute("select * from Table_1")
for row in mycursor1:
    print(row)
mycursor1.close()
print("Table 2")
mycursor2 = conn.cursor()
mycursor2.execute("select * from Table_2")
for row in mycursor2:
    print(row)
mycursor2.close()
print("Table 3")
mycursor3 = conn.cursor()
mycursor3.execute("select * from Table_3")
for row in mycursor3:
    print(row)
mycursor3.close()
conn.close()