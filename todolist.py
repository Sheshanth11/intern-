# TO-DO LIST APPLICATION

todo_list = []  # List to store tasks

def display_menu():
    print("\n TO-DO LIST MENU")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Done")
    print("4. Update Task")
    print("5. Delete Task")
    print("6. Exit")

def add_task():
    task = input("Enter the task: ")
    todo_list.append({"task": task, "done": False})
    print(" Task added successfully!")

def view_tasks():
    if not todo_list:
        print(" No tasks in the list.")
        return
    print("\n Your To-Do List:")
    for index, item in enumerate(todo_list, start=1):
        status = " Done" if item["done"] else " Not Done"
        print(f"{index}. {item['task']} [{status}]")

def mark_task_done():
    view_tasks()
    try:
        task_num = int(input("Enter task number to mark as done: "))
        if 1 <= task_num <= len(todo_list):
            todo_list[task_num - 1]["done"] = True
            print(" Task marked as done!")
        else:
            print(" Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def update_task():
    view_tasks()
    try:
        task_num = int(input("Enter task number to update: "))
        if 1 <= task_num <= len(todo_list):
            new_task = input("Enter the updated task: ")
            todo_list[task_num - 1]["task"] = new_task
            print("Task updated successfully!")
        else:
            print(" Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def delete_task():
    view_tasks()
    try:
        task_num = int(input("Enter task number to delete: "))
        if 1 <= task_num <= len(todo_list):
            deleted = todo_list.pop(task_num - 1)
            print(f"️ Deleted task: '{deleted['task']}'")
        else:
            print("️ Invalid task number.")
    except ValueError:
        print(" Please enter a valid number.")

# Main loop
while True:
    display_menu()
    choice = input("Enter your choice (1-6): ")
    
    if choice == '1':
        add_task()
    elif choice == '2':
        view_tasks()
    elif choice == '3':
        mark_task_done()
    elif choice == '4':
        update_task()
    elif choice == '5':
        delete_task()
    elif choice == '6':
        print(" Exiting To-Do List App. Goodbye!")
        break
    else:
        print("Invalid choice. Please select from 1 to 6.")
