import json

def load_tasks(filename="tasks.json"):
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_tasks(tasks, filename="tasks.json"):
    with open(filename, "w") as file:
        json.dump(tasks, file, indent=4)

def add_task(tasks):
    description = input("Enter task description: ")
    due_date = input("Enter due date (optional): ")
    tasks.append({"description": description, "due_date": due_date, "completed": False})

def view_tasks(tasks):
    for idx, task in enumerate(tasks):
        status = "Completed" if task["completed"] else "Pending"
        print(f"{idx + 1}. {task['description']} (Due: {task['due_date']}, Status: {status})")

def update_task(tasks):
    view_tasks(tasks)
    task_id = int(input("Enter the task number to update: ")) - 1
    if 0 <= task_id < len(tasks):
        tasks[task_id]["completed"] = True
    else:
        print("Invalid task number")

def delete_task(tasks):
    view_tasks(tasks)
    task_id = int(input("Enter the task number to delete: ")) - 1
    if 0 <= task_id < len(tasks):
        tasks.pop(task_id)
    else:
        print("Invalid task number")

def main():
    tasks = load_tasks()
    
    while True:
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice: ")
        
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            update_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            save_tasks(tasks)
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()












            
