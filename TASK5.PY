import tkinter as tk
from tkinter import messagebox, simpledialog

class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

class ContactManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Manager")
        self.root.geometry("400x500")
        self.root.config(bg="#f0f0f0")

        self.contacts = []

        self.title_label = tk.Label(root, text="Contact Manager", font=("Helvetica", 18, "bold"), bg="#f0f0f0")
        self.title_label.pack(pady=10)

        self.add_button = tk.Button(root, text="Add Contact", command=self.add_contact, font=("Arial", 14), bg="#4CAF50", fg="white")
        self.add_button.pack(pady=10)

        self.view_button = tk.Button(root, text="View Contacts", command=self.view_contacts, font=("Arial", 14), bg="#2196F3", fg="white")
        self.view_button.pack(pady=10)

        self.search_button = tk.Button(root, text="Search Contact", command=self.search_contact, font=("Arial", 14), bg="#FFC107", fg="black")
        self.search_button.pack(pady=10)

        self.update_button = tk.Button(root, text="Update Contact", command=self.update_contact, font=("Arial", 14), bg="#FF9800", fg="white")
        self.update_button.pack(pady=10)

        self.delete_button = tk.Button(root, text="Delete Contact", command=self.delete_contact, font=("Arial", 14), bg="#F44336", fg="white")
        self.delete_button.pack(pady=10)

        self.contacts_list_label = tk.Label(root, text="", font=("Arial", 12), bg="#f0f0f0", justify="left")
        self.contacts_list_label.pack(pady=10)

    def add_contact(self):
        name = simpledialog.askstring("Input", "Enter name:")
        if not name:
            return
        phone = simpledialog.askstring("Input", "Enter phone number:")
        email = simpledialog.askstring("Input", "Enter email:")
        address = simpledialog.askstring("Input", "Enter address:")
        new_contact = Contact(name, phone, email, address)
        self.contacts.append(new_contact)
        messagebox.showinfo("Success", "Contact added successfully!")

    def view_contacts(self):
        contact_list = "\n".join([f"{contact.name}: {contact.phone}" for contact in self.contacts])
        if contact_list:
            self.contacts_list_label.config(text=contact_list)
        else:
            self.contacts_list_label.config(text="No contacts available.")

    def search_contact(self):
        query = simpledialog.askstring("Search", "Enter name or phone number to search:")
        if not query:
            return
        found_contacts = [f"{contact.name}: {contact.phone}" for contact in self.contacts if query in contact.name or query in contact.phone]
        if found_contacts:
            self.contacts_list_label.config(text="\n".join(found_contacts))
        else:
            messagebox.showinfo("Search Result", "No contact found.")

    def update_contact(self):
        name = simpledialog.askstring("Update", "Enter the name of the contact to update:")
        if not name:
            return
        for contact in self.contacts:
            if contact.name == name:
                contact.phone = simpledialog.askstring("Input", "Enter new phone number:", initialvalue=contact.phone)
                contact.email = simpledialog.askstring("Input", "Enter new email:", initialvalue=contact.email)
                contact.address = simpledialog.askstring("Input", "Enter new address:", initialvalue=contact.address)
                messagebox.showinfo("Success", "Contact updated successfully!")
                return
        messagebox.showinfo("Update", "Contact not found.")

    def delete_contact(self):
        name = simpledialog.askstring("Delete", "Enter the name of the contact to delete:")
        if not name:
            return
        for contact in self.contacts:
            if contact.name == name:
                self.contacts.remove(contact)
                messagebox.showinfo("Success", "Contact deleted successfully!")
                return
        messagebox.showinfo("Delete", "Contact not found.")

if __name__ == "__main__":
    root = tk.Tk()
    contact_manager = ContactManager(root)
    root.mainloop()