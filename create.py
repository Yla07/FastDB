import tkinter as tk
import mysql.connector

root = tk.Tk()
root.title("FastDB(Creating_DataBase)")

database_name_label = tk.Label(root, text="Database Name ", font=("Arial", 15))
database_name_label.grid(column=0, row=1)

database_name = tk.Entry(root, width=30)
database_name.grid(column=1, row=1) 



def create():
    
    # Connecting to a server
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password=""
    )
    mycursor = mydb.cursor()



root.mainloop()