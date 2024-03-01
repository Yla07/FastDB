import tkinter as tk
import mysql.connector
import table

 # Connecting to a server
mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password=""
    )
root = tk.Tk()  
def create_db():
    global database_name_Entry, nubmer_of_tables_Entry

    database_name = database_name_Entry.get()
    number_of_tables = int(nubmer_of_tables_Entry.get())

    mycursor = mydb.cursor()

    # Checking if the database exists
    mycursor.execute("SHOW DATABASES")
    databases = mycursor.fetchall()
    database_exists = False
    for db in databases:
        if database_name in db:
            database_exists = True
            break
    
    if database_exists == False:
        
        mycursor.execute("CREATE DATABASE " + database_name)
        print("Database created successfully")
        # Creating tables
        table
       
root.title("FastDB(Creating_DataBase)")

database_name_label = tk.Label(root, text="Database Name ", font=("Arial", 15))
database_name_label.grid(column=0, row=1)

database_name_Entry = tk.Entry(root, width=30)
database_name_Entry.grid(column=1, row=1)

nubmer_of_tables_label = tk.Label(root, text="Number of Tables ", font=("Arial", 15))
nubmer_of_tables_label.grid(column=0, row=2)

nubmer_of_tables_Entry = tk.Entry(root, width=30)
nubmer_of_tables_Entry.grid(column=1, row=2)

continue_button = tk.Button(root, text="Continue", padx=10, pady=5, fg="white", bg="black", command=create_db)
continue_button.grid(column=1, row=3)

number_of_tables = int(nubmer_of_tables_Entry.get())
database_name = database_name_Entry.get()




    
   


root.mainloop()