import tkinter as tk
from tkinter import messagebox

class ToDoList:
    def __init__(self, root):
        self.tasks = []

        self.root = root
        self.root.title("To-Do List")

        # Task Entry
        self.task_entry = tk.Entry(root, width=40)
        self.task_entry.grid(row=0, column=0, padx=10, pady=10)

        # Add Task Button
        self.add_task_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_task_button.grid(row=0, column=1, padx=10, pady=10)

        # Task Listbox
        self.task_listbox = tk.Listbox(root, selectmode=tk.SINGLE, width=50, height=15)
        self.task_listbox.grid(row=1, column=0, columnspan=2, padx=10, pady=10)
        self.task_listbox.bind('<Double-1>', self.edit_task)
        self.task_listbox.bind('<B1-Motion>', self.drag_task)
        self.task_listbox.bind('<ButtonRelease-1>', self.drop_task)

        # Update Task Button
        self.update_task_button = tk.Button(root, text="Update Task", command=self.update_task)
        self.update_task_button.grid(row=2, column=0, padx=10, pady=10)

        # Delete Task Button
        self.delete_task_button = tk.Button(root, text="Delete Task", command=self.delete_task)
        self.delete_task_button.grid(row=2, column=1, padx=10, pady=10)

        self.dragging_task = None
        self.dragging_index = None

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.display_tasks()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error", "Task cannot be empty!")

    def edit_task(self, event):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            self.task_entry.delete(0, tk.END)
            self.task_entry.insert(0, self.tasks[index])

    def update_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            updated_task = self.task_entry.get()
            if updated_task:
                self.tasks[index] = updated_task
                self.display_tasks()
                self.task_entry.delete(0, tk.END)
            else:
                messagebox.showwarning("Input Error", "Task cannot be empty!")
        else:
            messagebox.showwarning("Selection Error", "Select a task to update!")

    def delete_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            del self.tasks[index]
            self.display_tasks()
        else:
            messagebox.showwarning("Selection Error", "Select a task to delete!")

    def display_tasks(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)

    def drag_task(self, event):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            self.dragging_index = selected_index[0]
            self.dragging_task = self.tasks[self.dragging_index]
            self.task_listbox.delete(self.dragging_index)

    def drop_task(self, event):
        if self.dragging_task:
            drop_index = self.task_listbox.nearest(event.y)
            self.tasks.insert(drop_index, self.dragging_task)
            self.dragging_task = None
            self.dragging_index = None
            self.display_tasks()

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoList(root)
    root.mainloop()

