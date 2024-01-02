import tkinter as tk
from tkinter import messagebox

contacts = []

def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    address = address_entry.get()

    new_contact = {
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    }

    contacts.append(new_contact)
    update_contact_list()
    clear_entries()
    messagebox.showinfo("Contact Management", f"Contact '{name}' added successfully!")

def delete_contact():
    selected_contact = contact_list.curselection()
    if selected_contact:
        index = selected_contact[0]
        deleted_contact = contacts.pop(index)
        update_contact_list()
        messagebox.showinfo("Contact Management", f"Contact '{deleted_contact['name']}' deleted successfully!")
    else:
        messagebox.showinfo("Contact Management", "Please select a contact to delete.")

def update_contact():
    selected_contact = contact_list.curselection()
    if selected_contact:
        index = selected_contact[0]
        contact = contacts[index]
        
        # Update the selected contact details
        contact['name'] = name_entry.get()
        contact['phone'] = phone_entry.get()
        contact['email'] = email_entry.get()
        contact['address'] = address_entry.get()

        update_contact_list()
        clear_entries()
        messagebox.showinfo("Contact Management", f"Contact '{contact['name']}' updated successfully!")
    else:
        messagebox.showinfo("Contact Management", "Please select a contact to update.")

def update_contact_list():
    contact_list.delete(0, tk.END)
    if not contacts:
        contact_list.insert(tk.END, "No contacts available.")
    else:
        for contact in contacts:
            contact_list.insert(tk.END, f"{contact['name']} - {contact['phone']}")

def search_contact():
    search_term = search_entry.get().lower()
    found_contacts = []

    for contact in contacts:
        if search_term in contact['name'].lower() or search_term in contact['phone']:
            found_contacts.append(contact)

    contact_list.delete(0, tk.END)
    if found_contacts:
        for contact in found_contacts:
            contact_list.insert(tk.END, f"{contact['name']} - {contact['phone']}")
    else:
        contact_list.insert(tk.END, "No matching contacts found.")

def clear_entries():
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)

def main():
    global name_entry, phone_entry, email_entry, address_entry, search_entry, contact_list

    root = tk.Tk()
    root.title("Contact Management System")
    root.geometry("380x600")
    root.configure(bg="skyblue")

    # Create and place widgets
    tk.Label(root, text="Name:", bg="skyblue").grid(row=0, column=0, padx=5, pady=5)
    tk.Label(root, text="Phone:", bg="skyblue").grid(row=1, column=0, padx=5, pady=5)
    tk.Label(root, text="Email:", bg="skyblue").grid(row=2, column=0, padx=5, pady=5)
    tk.Label(root, text="Address:", bg="skyblue").grid(row=3, column=0, padx=5, pady=5)

    name_entry = tk.Entry(root)
    phone_entry = tk.Entry(root)
    email_entry = tk.Entry(root)
    address_entry = tk.Entry(root)

    name_entry.grid(row=0, column=1, padx=5, pady=5)
    phone_entry.grid(row=1, column=1, padx=5, pady=5)
    email_entry.grid(row=2, column=1, padx=5, pady=5)
    address_entry.grid(row=3, column=1, padx=5, pady=5)

    add_button = tk.Button(root, text="Add Contact", command=add_contact)
    add_button.grid(row=4, column=0, columnspan=2, pady=10)

    tk.Label(root, text="Search:", bg="skyblue").grid(row=5, column=0, padx=5, pady=5)
    search_entry = tk.Entry(root)
    search_entry.grid(row=5, column=1, padx=5, pady=5)

    search_button = tk.Button(root, text="Search", command=search_contact)
    search_button.grid(row=6, column=0, columnspan=2, pady=10)

    view_button = tk.Button(root, text="View All Contacts", command=update_contact_list)
    view_button.grid(row=7, column=0, columnspan=2, pady=10)

    contact_list = tk.Listbox(root, height=10, width=40)
    contact_list.grid(row=8, column=0, columnspan=2, pady=10)

    button_frame = tk.Frame(root, bg="skyblue")
    button_frame.grid(row=9, column=0, columnspan=2)

    delete_button = tk.Button(button_frame, text="Delete Contact", command=delete_contact)
    delete_button.grid(row=0, column=0, padx=5, pady=10)

    update_button = tk.Button(button_frame, text="Update Contact", command=update_contact)
    update_button.grid(row=0, column=1, padx=5, pady=10)

    clear_entries_button = tk.Button(button_frame, text="Clear Entries", command=clear_entries)
    clear_entries_button.grid(row=0, column=2, padx=5, pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()
