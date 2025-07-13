import tkinter as tk
from tkinter import messagebox
import string
import random
import pyperclip  

# Function to generate password
def generate_password():
    try:
        length = int(length_entry.get())
        if length < 4:
            messagebox.showerror("Error", "Length must be at least 4")
            return

        characters = ""
        if var_upper.get():
            characters += string.ascii_uppercase
        if var_lower.get():
            characters += string.ascii_lowercase
        if var_numbers.get():
            characters += string.digits
        if var_symbols.get():
            characters += string.punctuation

        if not characters:
            messagebox.showerror("Error", "Please select at least one character set.")
            return

        # Generate password
        password = ''.join(random.choice(characters) for _ in range(length))
        password_entry.delete(0, tk.END)
        password_entry.insert(0, password)

    except ValueError:
        messagebox.showerror("Error", "Enter a valid number for length.")

# Function to copy password
def copy_password():
    password = password_entry.get()
    if password:
        pyperclip.copy(password)
        messagebox.showinfo("Copied", "Password copied to clipboard!")
    else:
        messagebox.showwarning("Warning", "No password to copy.")

# ------------------ GUI -------------------
root = tk.Tk()
root.title("Random Password Generator")
root.geometry("400x350")
root.config(bg="#1e1e1e")

# Heading
heading = tk.Label(root, text="Password Generator", font=("Helvetica", 18, "bold"), fg="white", bg="#1e1e1e")
heading.pack(pady=10)

# Length
tk.Label(root, text="Enter password length:", bg="#1e1e1e", fg="white").pack()
length_entry = tk.Entry(root, width=10)
length_entry.pack(pady=5)

# Character set options
var_upper = tk.BooleanVar()
var_lower = tk.BooleanVar()
var_numbers = tk.BooleanVar()
var_symbols = tk.BooleanVar()

tk.Checkbutton(root, text="Include Uppercase", variable=var_upper, bg="#1e1e1e", fg="white", selectcolor="#333333", activebackground="#1e1e1e").pack()
tk.Checkbutton(root, text="Include Lowercase", variable=var_lower, bg="#1e1e1e", fg="white", selectcolor="#333333", activebackground="#1e1e1e").pack()
tk.Checkbutton(root, text="Include Numbers", variable=var_numbers, bg="#1e1e1e", fg="white", selectcolor="#333333", activebackground="#1e1e1e").pack()
tk.Checkbutton(root, text="Include Symbols", variable=var_symbols, bg="#1e1e1e", fg="white", selectcolor="#333333", activebackground="#1e1e1e").pack()


# Generate button
tk.Button(root, text="Generate Password", command=generate_password, bg="#007acc", fg="white").pack(pady=10)

# Password display
password_entry = tk.Entry(root, font=("Helvetica", 12), width=30, justify='center')
password_entry.pack(pady=5)

# Copy button
tk.Button(root, text="Copy to Clipboard", command=copy_password, bg="#28a745", fg="white").pack()

# Run the app
root.mainloop()
