def add_task(tasks):
    description = input("Enter a task description: ").strip()

    if not description:
        print("Task description cannot be blank.")
        return

    tasks.append({"description": description, "completed": False})
    print("Task added.")


def view_tasks(tasks):
    if not tasks:
        print("No tasks yet.")
        return

    print("\nYour tasks:")
    for number, task in enumerate(tasks, start=1):
        status = "Completed" if task["completed"] else "Pending"
        print(f"{number}. {task['description']} - {status}")


def get_task_index(tasks):
    if not tasks:
        print("No tasks yet.")
        return None

    view_tasks(tasks)

    try:
        number = int(input("Enter the task number: "))
    except ValueError:
        print("Please enter a whole number.")
        return None

    if number < 1 or number > len(tasks):
        print(f"Please enter a task number from 1 to {len(tasks)}.")
        return None

    # Displayed task numbers start at 1; Python list indexes start at 0.
    return number - 1


def complete_task(tasks):
    index = get_task_index(tasks)
    if index is None:
        return

    if tasks[index]["completed"]:
        print("Task is already completed.")
        return

    tasks[index]["completed"] = True
    print("Task marked as completed.")


def delete_task(tasks):
    index = get_task_index(tasks)
    if index is None:
        return

    task = tasks.pop(index)
    print(f"Deleted task: {task['description']}")


def show_menu():
    print("\n1. Add a task")
    print("2. View all tasks")
    print("3. Mark a task as completed")
    print("4. Delete a task")
    print("5. Exit")


def main():
    tasks = []
    print("Welcome to Python Task Tracker!")

    while True:
        show_menu()
        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")


if __name__ == "__main__":
    main()
