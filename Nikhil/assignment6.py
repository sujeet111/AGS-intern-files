import pandas as pd
import pyodbc

data = pd.read_csv (r'C:\Users\Nikhil\Desktop\ags_intern\dataset.csv')
studio = pyodbc.connect('Driver={SQL Server};''Server=DESKTOP-9T4GEVI;''Database=patil;''Trusted_Connection=yes;')

cursor = studio.cursor()

#data = pd.DataFrame(data, columns= ['ID','Name'] )

for row in data.itertuples():
    var = str(row.ID)
    if var[0] == '4':
        discount = int(row.TotalAmount) - (int(row.TotalAmount) * 2 / 100)
        cursor.execute('INSERT INTO Table_01(ID, Name, TotalAmount, discount)VALUES (?,?,?,?)',row.ID, row.Name, row.TotalAmount, int(row.TotalAmount) * 2 / 100)
        print(discount)
       

    elif var[0] == '5':
        TotalAmount = int(row.TotalAmount) - (int(row.TotalAmount) * 3 / 100)
        cursor.execute('INSERT INTO Table_02(ID, Name, TotalAmount, discount)VALUES (?,?,?,?)',row.ID, row.Name, row.TotalAmount, int(row.TotalAmount) * 3 / 100)
     
    
    elif var[0] == '6': 
        TotalAmount = int(row.TotalAmount) - (int(row.TotalAmount) * 4 / 100)  
        cursor.execute('INSERT INTO Table_03(ID, Name, TotalAmount, discount)VALUES (?,?,?,?)',row.ID, row.Name, row.TotalAmount, int(row.TotalAmount) * 4 / 100)


    else:
        print("pass")

cursor.close()

print("Table_01")
cursor1 = studio.cursor()
cursor1.execute("select * from Table_01")
for row in cursor1:
    print(row)
cursor1.close()


print("Table_02")
cursor2 = studio.cursor()
cursor2.execute("select * from Table_02")
for row in cursor2:
    print(row)
cursor2.close()


print("Table_03")
cursor3 = studio.cursor()
cursor3.execute("select * from Table_03")
for row in cursor3:
    print(row)
cursor3.close()
studio.close()
