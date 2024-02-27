
# Importing libraries
import mysql.connector
import time as t
import os
import tkinter as tk
from tkinter import messagebox


# Connecting to a server 
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password=""
)
mycursor = mydb.cursor()

# Checking if the database exists
mycursor.execute("SHOW DATABASES")
databases = mycursor.fetchall()
database_exists = False
for db in databases:
    if 'mydatabase' in db:
        database_exists = True
        break

if database_exists:
    print("Database exists")
    continue_ = input("Do you want to delete the database? (y/n): ")
    
    if continue_ == 'y':
        mycursor.execute("DROP DATABASE mydatabase")
        print("Database deleted successfully")
    else:
        if continue_ == 'n':
            print("Ok")
        else:
            print("Invalid input")
else:
    print("Database does not exist")
    t.sleep(1)
    print("Creating database. Please wait...")
    t.sleep(5)
    mycursor.execute("CREATE DATABASE mydatabase")
    mycursor.execute("USE mydatabase")
    mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")
    mycursor.execute("INSERT INTO customers (name, address) VALUES ('John', 'Highway 21')")
    print("Database created successfully")


mydb.close()