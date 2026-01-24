from src.core import show_tasks, add_task, mark_done, delete_task
from src.storage import load_tasks, save_tasks

def run_cli():
    tasks = load_tasks()

    while True:
        print("""
        ==== Todo List Cli ====
        1) Show Tasks 
        2) Add Task
        3) Mark Task Done
        4) Delete Task
        0) Exit
        """) # s = Read, a = Create, u = Update, d = Delete

        choice = input("pick an option: ")

        if choice == "1":
            task_list = show_tasks(tasks)
            if not task_list:
                print("No tasks yet.")
            for i, task in enumerate(task_list, 1):
                status = "Completed" if task["done"] else "Not Completed"
                print(f"{i}. [{status}] {task['title']}")
            
        elif choice == "2":
            title = input("Task Name: ")
            add_task(tasks, title)

        elif choice == "3":
            idx = int(input("Task Number: ")) - 1
            mark_done(tasks, idx)

        elif choice == "4":
            idx = int(input("Task Number: ")) - 1
            delete_task(tasks, idx)

        elif choice == "0":
            save_tasks(tasks)
            print("Tasks saved. Allah Hafiz!")
            break
        
        else:
            print("Invalid Option!")