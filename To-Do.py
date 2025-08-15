tasks = []

while True:
    print("\nWhat do you want to do?")
    print("[1] Add task")
    print("[2] View tasks")
    print("[3] Delete task")
    print("[4] Quit")
    
    menu = input("> ").strip()

    if menu == "1":
        task = input("Enter task:\n> ")
        tasks.append(task)
        print("Task added!")

    elif menu == "2":
        if not tasks:
            print("No tasks yet.")
        else:
            print("Your tasks:")
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")

    elif menu == "3":
        if not tasks:
            print("No tasks to delete.")
            continue

        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
        try:
            to_delete = int(input("Enter task number to delete: "))
            if 1 <= to_delete <= len(tasks):
                removed = tasks.pop(to_delete - 1)
                print(f"Deleted task: {removed}")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

    elif menu == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please enter 1, 2, 3, or 4.")
