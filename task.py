import tkinter as tk
from tkinter import messagebox

def submit_form():
    name = name_var.get()
    email = email_var.get()
    age = age_var.get()

    if not name or not email or not age:
        messagebox.showwarning("Incomplete Data", "Please fill all fields.")
        return
    
    try:
        age = int(age)
    except ValueError:
        messagebox.showerror("Invalid Age", "Age must be a number.")
        return

    messagebox.showinfo("Form Submitted", f"Name: {name}\nEmail: {email}\nAge: {age}")
    clear_form()

def clear_form():
    name_var.set("")
    email_var.set("")
    age_var.set("")

# Create main window
root = tk.Tk()
root.title("Registration Form")

# Define StringVar for entry fields
name_var = tk.StringVar()
email_var = tk.StringVar()
age_var = tk.StringVar()

# Create and place widgets
tk.Label(root, text="Name:").grid(row=0, column=0, padx=10, pady=5, sticky="e")
tk.Entry(root, textvariable=name_var).grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Email:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
tk.Entry(root, textvariable=email_var).grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Age:").grid(row=2, column=0, padx=10, pady=5, sticky="e")
tk.Entry(root, textvariable=age_var).grid(row=2, column=1, padx=10, pady=5)

tk.Button(root, text="Submit", command=submit_form).grid(row=3, column=0, padx=10, pady=10)
tk.Button(root, text="Clear", command=clear_form).grid(row=3, column=1, padx=10, pady=10)

# Run the main loop
root.mainloop()
