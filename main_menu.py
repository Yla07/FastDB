import tkinter as tk
from Create import create as c


root = tk.Tk()
root.title("FastDB")
root.geometry("800x600")

def create_db():
    c.create_db()

# Creating labels
db_manage_label = tk.Label(root, text="Database Managment", font=("Arial", 20))
db_manage_label.grid(column=1, row=0, columnspan=2)

# Creating buttons
settings_button = tk.Button(root, text="...", padx=10, pady=5, fg="white", bg="black")
settings_button.grid(column=3, row=0)

create_button = tk.Button(root, text="CREATE", padx=10, pady=5, fg="white", bg="black", command=create_db)
create_button.grid(column=0, row=1)

delete_button = tk.Button(root, text="DROP", padx=10, pady=5, fg="white", bg="black")
delete_button.grid(column=0, row=2)

show_button = tk.Button(root, text="SHOW", padx=10, pady=5, fg="white", bg="black")
show_button.grid(column=0, row=3)


root.mainloop()