import pandas as pd
import pyodbc

path = r'C:\Users\sujeet\Desktop\Projects\AGS\AGS-intern-files\Sujeet\person.csv'

conn = pyodbc.connect('Driver={SQL Server};''Server=DESKTOP-CAFAM2K\SUJEETPATIL;''Database=Agsdb;''Trusted_Connection=yes;')
mycursor = conn.cursor()
mycursor2 = conn.cursor()

data = pd.read_csv(r"C:\Users\sujeet\Desktop\Projects\AGS\AGS-intern-files\Sujeet\data.csv")
print(data)