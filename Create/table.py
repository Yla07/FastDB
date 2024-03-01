import tkinter as tk
import mysql.connector
from create import number_of_tables, database_name

mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password=""
    )
mycursor = mydb.cursor()

root = tk.Tk()
root.title("FastDB(Table Creator)")

def create_table():
    global table_name_entry
    table_name = table_name_entry.get()
    mycursor.execute("USE " + database_name)
    mycursor.execute("CREATE TABLE " + table_name + " (id INT AUTO_INCREMENT PRIMARY KEY)")
    print("Table created successfully")

for i in range(number_of_tables):
    table_name_label = tk.Label(root, text="Table Name ", font=("Arial", 15))
    table_name_label.grid(column=0, row=i+1)
    
    table_name_entry = tk.Entry(root, width=30)
    table_name_entry.grid(column=1, row=i+1)
    
    table_name_button = tk.Button(root, text="Submit", padx=10, pady=5, fg="white", bg="black")
    table_name_button.grid(column=2, row=i+1)


    root.mainloop()


