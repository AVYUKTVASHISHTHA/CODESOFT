import tkinter as tk
from tkinter import messagebox

# Initialize the main app window
app = tk.Tk()
app.title("To-Do List")
app.geometry("400x500")

# Task list to hold tasks and their statuses
tasks = []

# Function to add a new task
def add_task():
    task = task_entry.get()
    if task:
        tasks.append({"task": task, "done": False})
        task_entry.delete(0, tk.END)
        update_task_list()
    else:
        messagebox.showwarning("Input Error", "Please enter a task")

# Function to delete the selected task
def delete_task():
    selected_task_index = task_listbox.curselection()
    if selected_task_index:
        del tasks[selected_task_index[0]]
        update_task_list()
    else:
        messagebox.showwarning("Selection Error", "Please select a task to delete")

# Function to mark the selected task as done or undone
def toggle_task_status():
    selected_task_index = task_listbox.curselection()
    if selected_task_index:
        task_index = selected_task_index[0]
        tasks[task_index]["done"] = not tasks[task_index]["done"]
        update_task_list()
    else:
        messagebox.showwarning("Selection Error", "Please select a task to mark as done")

# Function to update the task list display
def update_task_list():
    task_listbox.delete(0, tk.END)
    for task in tasks:
        task_text = f"[{'✔' if task['done'] else ' '}] {task['task']}"
        task_listbox.insert(tk.END, task_text)

# GUI Layout
# Label for task entry
entry_label = tk.Label(app, text="Enter a new task:", font=("Arial", 12))
entry_label.pack(pady=(10, 0))

# Entry box for adding tasks
task_entry = tk.Entry(app, width=40)
task_entry.pack(pady=5)

# Frame to hold buttons horizontally
button_frame = tk.Frame(app)
button_frame.pack(pady=10)

# Buttons for adding, deleting, and marking tasks
add_button = tk.Button(button_frame, text="Add Task", width=10, command=add_task)
add_button.grid(row=0, column=0, padx=5)

delete_button = tk.Button(button_frame, text="Delete Task", width=10, command=delete_task)
delete_button.grid(row=0, column=1, padx=5)

done_button = tk.Button(button_frame, text="Mark as Done", width=10, command=toggle_task_status)
done_button.grid(row=0, column=2, padx=5)

# Label for task list display
list_label = tk.Label(app, text="Tasks:", font=("Arial", 12))
list_label.pack(pady=(15, 5))

# Task list display
task_listbox = tk.Listbox(app, width=40, height=15, selectmode=tk.SINGLE)
task_listbox.pack(pady=5)

# Run the application
app.mainloop()