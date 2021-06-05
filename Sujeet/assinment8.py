from tkinter import *
from tkinter import filedialog
import pandas as pd
import pyodbc
import os

conn = pyodbc.connect('Driver={SQL Server};''Server=DESKTOP-CAFAM2K\SUJEETPATIL;''Database=Agsdb;''Trusted_Connection=yes;')


def browseFiles():
    filename = filedialog.askopenfilename(initialdir = "/", title = "Select a File", filetypes = (("CSV","*.csv*"),
                                                       ("all files",
                                                        "*.*")))
      
    # Change label contents
    label_file_explorer.configure(text="File Opened: "+filename)
    processtable(filename)
      
def processtable(filename):
    data = pd.read_csv(filename)
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
        mycursor.commit()
    mycursor.close()
    createcsv('Table_1')
    createcsv('Table_2')
    createcsv('Table_3')

def createcsv(table):
    cwd = os.getcwd()
    data = pd.read_sql("SELECT * FROM "+table, conn)
    data.to_csv(cwd+ "\\" + table + ".csv" , index = False, header=True)

                                                                                                  
# Create the root window
window = Tk()
  
# Set window title
window.title('File Explorer')
  
# Set window size
window.geometry("500x500")
  
#Set window background color
window.config(background = "white")
  
# Create a File Explorer label
label_file_explorer = Label(window,
                            text = "TASK 8",
                            width = 100, height = 4,
                            fg = "blue")
  
      
button_explore = Button(window,
                        text = "Browse CSV and Process",
                        command = browseFiles)
  
button_exit = Button(window,
                     text = "Exit",
                     command = exit)


label_file_explorer.grid(column = 1, row = 1)
  
button_explore.grid(column = 1, row = 2)
  
button_exit.grid(column = 1,row = 4)
  
# Let the window wait for any events
window.mainloop()