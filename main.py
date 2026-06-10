from task_manager.task_utils import (add_task,
                                      mark_task_as_complete,
                                      view_pending_tasks,
                                      calculate_progress)


def display_menu():
    print("\n===== Task Management System =====")
    print("1. Add a new task")
    print("2. Mark a task as complete")
    print("3. View pending tasks")
    print("4. Calculate progress")
    print("5. Exit")
    print("==================================")


def main():
    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            due_date = input("Enter due date (YYYY-MM-DD): ")
            add_task(title, description, due_date)

        elif choice == "2":
            index = input("Enter task number to mark complete: ")
            mark_task_as_complete(index)

        elif choice == "3":
            view_pending_tasks()

        elif choice == "4":
            calculate_progress()

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()