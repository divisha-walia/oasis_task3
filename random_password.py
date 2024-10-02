import tkinter as tk
import random
import string
import pyperclip
letters = string.ascii_letters
digits = string.digits
symbols = string.punctuation
def generate_password():
    password_length = int(length_entry.get())
    include_letters = letters_var.get()
    include_digits = digits_var.get()
    include_symbols = symbols_var.get()

    characters = ""
    if include_letters:
        characters += letters
    if include_digits:
        characters += digits
    if include_symbols:
        characters += symbols

    if not characters:
        password_label.config(text="Please select at least one character type.")
        return

    password = ''.join(random.choice(characters) for _ in range(password_length))
    password_label.config(text=password)

    # Implement clipboard integration
    pyperclip.copy(password)
    clipboard_label.config(text="Password copied to clipboard.")
root = tk.Tk()
root.title("Password Generator")

# Password length label and entry
length_label = tk.Label(root, text="Password Length:")
length_entry = tk.Entry(root)

# Character type checkboxes
letters_var = tk.BooleanVar()
digits_var = tk.BooleanVar()
symbols_var = tk.BooleanVar()

letters_check = tk.Checkbutton(root, text="Include Letters", variable=letters_var)
digits_check = tk.Checkbutton(root, text="Include Numbers", variable=digits_var)
symbols_check = tk.Checkbutton(root, text="Include Symbols", variable=symbols_var)

# Generate password button
generate_button = tk.Button(root, text="Generate Password", command=generate_password)

# Password result label
password_label = tk.Label(root, text="")

# Clipboard status label
clipboard_label = tk.Label(root, text="")

# Arrange widgets
length_label.grid(row=0, column=0)
length_entry.grid(row=0, column=1)
letters_check.grid(row=1, column=0)
digits_check.grid(row=2, column=0)
symbols_check.grid(row=3, column=0)
generate_button.grid(row=4, column=0, columnspan=2)
password_label.grid(row=5, column=0, columnspan=2)
clipboard_label.grid(row=6, column=0, columnspan=2)

root.mainloop()