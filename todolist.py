import tkinter as tk
from tkinter import simpledialog, messagebox

class ToDoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")
        self.root.geometry("400x400")
        self.root.configure(bg="orange")  
        self.tasks = []

        # Create and set up widgets
        self.task_entry = tk.Entry(root, width=30)
        self.task_entry.grid(row=0, column=0, padx=10, pady=10, columnspan=2, sticky="ew")

        self.add_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_button.grid(row=0, column=2, padx=10, pady=10)

        self.task_listbox = tk.Listbox(root, selectmode=tk.SINGLE, width=40, height=10)
        self.task_listbox.grid(row=1, column=0, columnspan=3, padx=10, pady=10, sticky="ew")

        self.remove_button = tk.Button(root, text="Remove Task", command=self.remove_task)
        self.remove_button.grid(row=2, column=0, padx=10, pady=10)

        self.update_button = tk.Button(root, text="Update Progress", command=self.update_progress)
        self.update_button.grid(row=2, column=1, padx=10, pady=10)

        self.clear_button = tk.Button(root, text="Clear All Tasks", command=self.clear_tasks)
        self.clear_button.grid(row=2, column=2, padx=10, pady=10)

    def add_task(self):
        task = self.task_entry.get().strip()
        if task:
            self.tasks.append({"name": task, "progress": "Yet to do"})
            self.update_task_listbox()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a task.")

    def remove_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            self.tasks.pop(selected_index[0])
            self.update_task_listbox()
        else:
            messagebox.showwarning("Warning", "Please select a task to remove.")

    def clear_tasks(self):
        self.tasks.clear()
        self.update_task_listbox()

    def update_progress(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            task_info = self.tasks[selected_index[0]]
            progress_options = ["Yet to do", "Partial", "Completed"]
            selected_progress = tk.StringVar(self.root)
            selected_progress.set(task_info["progress"])
            
            progress_menu = tk.OptionMenu(self.root, selected_progress, *progress_options)
            progress_menu.grid(row=3, column=0, columnspan=3, pady=5, sticky="ew")

            def update_task_progress():
                task_info["progress"] = selected_progress.get()
                self.update_task_listbox()
                progress_menu.destroy()

            update_button = tk.Button(self.root, text="Update", command=update_task_progress)
            update_button.grid(row=4, column=0, columnspan=3, pady=5, sticky="ew")
        else:
            messagebox.showwarning("Warning", "Please select a task to update progress.")

    def update_task_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for index, task_info in enumerate(self.tasks, start=1):
            task_name = task_info["name"]
            task_progress = task_info["progress"]
            self.task_listbox.insert(tk.END, f"{index}. {task_name} - {task_progress}")

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoListApp(root)
    root.mainloop()
