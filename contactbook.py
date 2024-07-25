import tkinter as tk
from tkinter import messagebox

class ContactBook:
    def __init__(self, root):
        self.contacts = []

        self.root = root
        self.root.title("Contact Book")

        # Labels and Entries for Contact Details
        self.name_label = tk.Label(root, text="Name")
        self.name_label.grid(row=0, column=0, padx=10, pady=5)
        self.name_entry = tk.Entry(root)
        self.name_entry.grid(row=0, column=1, padx=10, pady=5)

        self.phone_label = tk.Label(root, text="Phone")
        self.phone_label.grid(row=1, column=0, padx=10, pady=5)
        self.phone_entry = tk.Entry(root)
        self.phone_entry.grid(row=1, column=1, padx=10, pady=5)

        self.email_label = tk.Label(root, text="Email")
        self.email_label.grid(row=2, column=0, padx=10, pady=5)
        self.email_entry = tk.Entry(root)
        self.email_entry.grid(row=2, column=1, padx=10, pady=5)

        self.address_label = tk.Label(root, text="Address")
        self.address_label.grid(row=3, column=0, padx=10, pady=5)
        self.address_entry = tk.Entry(root)
        self.address_entry.grid(row=3, column=1, padx=10, pady=5)

        # Buttons
        self.add_button = tk.Button(root, text="Add Contact", command=self.add_contact)
        self.add_button.grid(row=4, column=0, padx=10, pady=5)

        self.update_button = tk.Button(root, text="Update Contact", command=self.update_contact)
        self.update_button.grid(row=4, column=1, padx=10, pady=5)

        self.delete_button = tk.Button(root, text="Delete Contact", command=self.delete_contact)
        self.delete_button.grid(row=4, column=2, padx=10, pady=5)

        self.search_label = tk.Label(root, text="Search by Name or Phone")
        self.search_label.grid(row=5, column=0, padx=10, pady=5)
        self.search_entry = tk.Entry(root)
        self.search_entry.grid(row=5, column=1, padx=10, pady=5)
        self.search_button = tk.Button(root, text="Search", command=self.search_contact)
        self.search_button.grid(row=5, column=2, padx=10, pady=5)

        self.contact_listbox = tk.Listbox(root)
        self.contact_listbox.grid(row=6, column=0, columnspan=3, padx=10, pady=5)
        self.contact_listbox.bind('<<ListboxSelect>>', self.load_contact_details)

    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        address = self.address_entry.get()

        if name and phone:
            self.contacts.append({"name": name, "phone": phone, "email": email, "address": address})
            self.display_contacts()
            self.clear_entries()
        else:
            messagebox.showwarning("Input Error", "Name and Phone are required!")

    def update_contact(self):
        selected_index = self.contact_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            self.contacts[index] = {
                "name": self.name_entry.get(),
                "phone": self.phone_entry.get(),
                "email": self.email_entry.get(),
                "address": self.address_entry.get()
            }
            self.display_contacts()
            self.clear_entries()
        else:
            messagebox.showwarning("Selection Error", "Select a contact to update!")

    def delete_contact(self):
        selected_index = self.contact_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            del self.contacts[index]
            self.display_contacts()
            self.clear_entries()
        else:
            messagebox.showwarning("Selection Error", "Select a contact to delete!")

    def search_contact(self):
        query = self.search_entry.get().lower()
        matched_contacts = [contact for contact in self.contacts if query in contact["name"].lower() or query in contact["phone"]]
        self.display_contacts(matched_contacts)

    def load_contact_details(self, event):
        selected_index = self.contact_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            contact = self.contacts[index]
            self.name_entry.delete(0, tk.END)
            self.name_entry.insert(0, contact["name"])
            self.phone_entry.delete(0, tk.END)
            self.phone_entry.insert(0, contact["phone"])
            self.email_entry.delete(0, tk.END)
            self.email_entry.insert(0, contact["email"])
            self.address_entry.delete(0, tk.END)
            self.address_entry.insert(0, contact["address"])

    def display_contacts(self, contacts=None):
        if contacts is None:
            contacts = self.contacts
        self.contact_listbox.delete(0, tk.END)
        for contact in contacts:
            self.contact_listbox.insert(tk.END, f"{contact['name']} - {contact['phone']}")

    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactBook(root)
    root.mainloop()

