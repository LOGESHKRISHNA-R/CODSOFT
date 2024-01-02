import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password(length, additional_factors):
    source_characters = ""

    if additional_factors:
        first_char = additional_factors[0]
        rest_of_chars = additional_factors[1:]

        # Include both lowercase and uppercase letters for the first character
        source_characters += first_char.lower() + first_char.upper() + rest_of_chars

    # Add additional random characters to meet the specified length
    while len(source_characters) < length - 2:
        source_characters += random.choice(string.ascii_letters + string.digits)

    # Add one or two random numbers at the end
    source_characters += ''.join(random.choices(string.digits, k=random.randint(1, 2)))

    generated_password = ''.join(random.sample(source_characters, length))

    messagebox.showinfo("Password Generator", f"Generated Password: {generated_password}")

def main():
    root = tk.Tk()
    root.title("Password Generator")

    length_label = tk.Label(root, text="Password Length:")
    length_label.grid(row=0, column=0, padx=5, pady=5)

    length_entry = tk.Entry(root)
    length_entry.grid(row=0, column=1, padx=5, pady=5)

    factors_label = tk.Label(root, text="Additional Factors:")
    factors_label.grid(row=1, column=0, padx=5, pady=5)

    factors_entry = tk.Entry(root)
    factors_entry.grid(row=1, column=1, padx=5, pady=5)

    generate_button = tk.Button(root, text="Generate Password", command=lambda: generate_password(
        int(length_entry.get()),
        factors_entry.get()
    ))
    generate_button.grid(row=2, column=0, columnspan=2, pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()
