import pandas as pd
import pyodbc

data = pd.read_csv (r'C:\Users\Nikhil\Desktop\ags_intern\dataset.csv')
studio = pyodbc.connect('Driver={SQL Server};''Server=DESKTOP-9T4GEVI;''Database=patil;''Trusted_Connection=yes;')
cursor = studio.cursor()

data = pd.DataFrame(data, columns= ['dataset'] )
print(data.dataset)

cursor.execute('crate table table_1(table1 int); ')






