def print_menu():
    print("Welcome to Task Bar")
    print("1. Add a task")
    print("2. View tasks in Task Bar")
    print("3. Mark a task as done")
    print("4. Delete a task")
    print("5. Know the status of a task")
    print("6. Exit Task Bar")
    print("-----------------")

tasks = {}
print_menu()

while True:
    
    try:
        choice = int(input("Enter your choice (1-6): "))
    except ValueError:
        print("Please enter a valid number between 1 and 6.")
        continue
    
    if choice == 1:
        task = input("Enter the task you want to add to Task Bar: ")
        if task in tasks:
            print("This task already exists in Task Bar.")
        else:
            tasks[task] = "not completed"
            print(f"Task '{task}' added.")
        print("-----------------")

    elif choice == 2:
        if not tasks:
            print("Task Bar is empty!")
        else:
            for task, status in tasks.items():
                print(f"{task} - {status}")
        print("-----------------")

    elif choice == 3:
        if not tasks:
            print("Task Bar is empty!")
        else:
            task = input("Enter the task you want to mark as completed: ")
            if task in tasks:
                tasks[task] = "completed"
                print(f"Task '{task}' marked as completed.")
            else:
                print("Task not found.")
        print("-----------------")

    elif choice == 4:
        if not tasks:
            print("Task Bar is empty!")
        else:
            task = input("Enter the task you want to delete: ")
            if task in tasks:
                del tasks[task]
                print(f"Task '{task}' deleted.")
            else:
                print("Task not found.")
        print("-----------------")

    elif choice == 5:
        if not tasks:
            print("Task Bar is empty!")
        else:
            task = input("Enter the task to know its status: ")
            if task in tasks:
                print(f"Task '{task}' is {tasks[task]}.")
            else:
                print("Task not found.")
        print("-----------------")

    elif choice == 6:
        print("Task Bar is closed.")
        print("-----------------")
        break

    else:
        print("Enter a valid choice (1-6).")
        print("-----------------")
