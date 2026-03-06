import sqlite3
import matplotlib.pyplot as plt

conn = sqlite3.connect("study_planner.db")
cursor = conn.cursor()

print("1. Add Task")
print("2. View Tasks")
print("3. Performance Analysis")
print("4. Show Study Chart")

choice = input("Enter your choice: ")

if choice == "1":
    subject = input("Enter subject name: ")
    planned = int(input("Enter planned hours: "))
    completed = int(input("Enter completed hours: "))

    cursor.execute(
        "INSERT INTO tasks(subject, planned_hours, completed_hours) VALUES(?,?,?)",
        (subject, planned, completed)
    )

    conn.commit()
    print("Task added successfully!")

elif choice == "2":
    cursor.execute("SELECT * FROM tasks")
    rows = cursor.fetchall()

    print("\nStudy Tasks:")
    for row in rows:
        print(row)

elif choice == "3":

    cursor.execute("SELECT SUM(planned_hours) FROM tasks")
    planned_total = cursor.fetchone()[0]

    cursor.execute("SELECT SUM(completed_hours) FROM tasks")
    completed_total = cursor.fetchone()[0]

    print("\nTotal Planned Hours:", planned_total)
    print("Total Completed Hours:", completed_total)

elif choice == "4":

    cursor.execute("SELECT subject, completed_hours FROM tasks")
    data = cursor.fetchall()

    subjects = []
    hours = []

    for row in data:
        subjects.append(row[0])
        hours.append(row[1])

    plt.bar(subjects, hours)
    plt.xlabel("Subjects")
    plt.ylabel("Completed Hours")
    plt.title("Study Performance Chart")

    plt.show()

else:
    print("Invalid choice")

conn.close()