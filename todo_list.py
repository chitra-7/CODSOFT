tasks = []

def show_menu():
    print("\n--- TO-DO LIST ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task Completed")
    print("4. Delete Task")
    print("5. Exit")

def add_task():
    task = input("Enter the task: ")
    tasks.append({'task': task, 'completed': False})
    print("Task added!")

def view_tasks():
    if not tasks:
        print("No tasks yet!")
        return
    for idx, task in enumerate(tasks):
        status = "✓" if task['completed'] else "✗"
        print(f"{idx+1}. {task['task']} [{status}]")

def mark_completed():
    view_tasks()
    try:
        task_no = int(input("Enter task number to mark complete: "))
        tasks[task_no-1]['completed'] = True
        print("Task marked as completed.")
    except (IndexError, ValueError):
        print("Invalid input!")

def delete_task():
    view_tasks()
    try:
        task_no = int(input("Enter task number to delete: "))
        tasks.pop(task_no-1)
        print("Task deleted.")
    except (IndexError, ValueError):
        print("Invalid input!")

while True:
    show_menu()
    choice = input("Choose an option: ")
    
    if choice == '1':
        add_task()
    elif choice == '2':
        view_tasks()
    elif choice == '3':
        mark_completed()
    elif choice == '4':
        delete_task()
    elif choice == '5':
        print("Goodbye!")
        break
    else:
        print("Invalid choice! Try again.")