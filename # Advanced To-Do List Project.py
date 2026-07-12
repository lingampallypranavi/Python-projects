# Advanced To-Do List Project

tasks = []

while True:
    print("\n===== TO-DO LIST =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Mark Task as Completed")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    # Add task
    if choice == "1":
        task_name = input("Enter task: ")

        task = {
            "name": task_name,
            "completed": False
        }

        tasks.append(task)
        print("Task added successfully!")

    # View tasks
    elif choice == "2":
        if len(tasks) == 0:
            print("No tasks available.")

        else:
            print("\nYour Tasks:")
            for i, task in enumerate(tasks, start=1):

                status = "✓ Completed" if task["completed"] else "✗ Pending"

                print(f"{i}. {task['name']} - {status}")

    # Delete task
    elif choice == "3":
        if len(tasks) == 0:
            print("No tasks to delete.")

        else:
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task['name']}")

            num = int(input("Enter task number to delete: "))

            if 1 <= num <= len(tasks):
                removed = tasks.pop(num - 1)
                print(f"'{removed['name']}' deleted successfully!")
            else:
                print("Invalid task number.")

    # Mark completed
    elif choice == "4":
        if len(tasks) == 0:
            print("No tasks available.")

        else:
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task['name']}")

            num = int(input("Enter task number completed: "))

            if 1 <= num <= len(tasks):
                tasks[num-1]["completed"] = True
                print("Task marked as completed!")
            else:
                print("Invalid task number.")

    # Exit
    elif choice == "5":
        print("Thank you for using To-Do List")
        break

    else:
        print("Invalid choice! Try again.")