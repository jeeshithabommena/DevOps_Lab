import sqlite3
import tkinter as tk
from tkinter import messagebox

# add task function
def add_task():
    subject = subject_entry.get()
    planned = planned_entry.get()
    completed = completed_entry.get()

    conn = sqlite3.connect("study_planner.db")
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO tasks(subject, planned_hours, completed_hours) VALUES(?,?,?)",
        (subject, planned, completed)
    )

    conn.commit()
    conn.close()

    messagebox.showinfo("Success", "Task Added Successfully")

# view tasks
def view_tasks():
    conn = sqlite3.connect("study_planner.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM tasks")
    rows = cursor.fetchall()

    text.delete("1.0", tk.END)

    for row in rows:
        text.insert(tk.END, str(row) + "\n")

    conn.close()

# GUI window
root = tk.Tk()
root.title("Smart Study Planner")
root.geometry("400x400")

tk.Label(root, text="Subject").pack()
subject_entry = tk.Entry(root)
subject_entry.pack()

tk.Label(root, text="Planned Hours").pack()
planned_entry = tk.Entry(root)
planned_entry.pack()

tk.Label(root, text="Completed Hours").pack()
completed_entry = tk.Entry(root)
completed_entry.pack()

tk.Button(root, text="Add Task", command=add_task).pack(pady=5)
tk.Button(root, text="View Tasks", command=view_tasks).pack(pady=5)

text = tk.Text(root, height=10)
text.pack()

root.mainloop()