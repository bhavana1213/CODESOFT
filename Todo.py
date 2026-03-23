# 📝 TO-DO LIST APPLICATION

tasks = []

def show_tasks():
    if not tasks:
        print("\n📭 No tasks available!\n")
        return

    print("\n📋 YOUR TASKS:")
    for i, task in enumerate(tasks):
        status = "✔ Done" if task["done"] else "❌ Pending"
        print(f"{i+1}. {task['title']} - {status}")
    print()

def add_task():
    title = input("Enter task: ")
    tasks.append({"title": title, "done": False})
    print("✅ Task added!\n")

def mark_done():
    show_tasks()
    try:
        index = int(input("Enter task number to mark done: ")) - 1
        tasks[index]["done"] = True
        print("✔ Task marked as completed!\n")
    except:
        print("❌ Invalid input!\n")

def delete_task():
    show_tasks()
    try:
        index = int(input("Enter task number to delete: ")) - 1
        removed = tasks.pop(index)
        print(f"🗑 Deleted: {removed['title']}\n")
    except:
        print("❌ Invalid input!\n")

while True:
    print("===== TO-DO LIST MENU =====")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Mark Task as Done")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        show_tasks()
    elif choice == "2":
        add_task()
    elif choice == "3":
        mark_done()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        print("👋 Exiting... Goodbye!")
        break
    else:
        print("❌ Invalid choice!\n")