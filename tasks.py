def add_task():
    task = input("Enter task: ")
    with open("data/tasks.txt", "a") as f:
        f.write(task + "\n")
    print("Task added.")

def view_tasks():
    try:
        with open("data/tasks.txt", "r") as f:
            print("\nTasks:")
            for i, task in enumerate(f, start=1):
                print(f"{i}. {task.strip()}")
    except FileNotFoundError:
        print("No tasks found.")
