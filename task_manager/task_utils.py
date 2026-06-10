from task_manager.validation import (validate_task_title,
                                      validate_task_description,
                                      validate_due_date)

tasks = []


def add_task(title, description, due_date):
    valid, msg = validate_task_title(title)
    if not valid:
        print(f"Invalid title: {msg}")
        return False

    valid, msg = validate_task_description(description)
    if not valid:
        print(f"Invalid description: {msg}")
        return False

    valid, msg = validate_due_date(due_date)
    if not valid:
        print(f"Invalid due date: {msg}")
        return False

    task = {
        "title": title.strip(),
        "description": description.strip(),
        "due_date": due_date.strip(),
        "completed": False
    }
    tasks.append(task)
    print(f"Task '{title.strip()}' added successfully.")
    return True


def mark_task_as_complete(title, tasks=tasks):
    for task in tasks:
        if task["title"].lower() == title.strip().lower():
            task["completed"] = True
            print(f"Task '{task['title']}' marked as complete.")
            return True
    print(f"No task found with title '{title}'.")
    return False


def view_pending_tasks(tasks=tasks):
    pending = [t for t in tasks if not t["completed"]]
    if not pending:
        print("No pending tasks.")
    else:
        print("\n--- Pending Tasks ---")
        for i, task in enumerate(pending, 1):
            print(f"{i}. [{task['due_date']}] {task['title']}: {task['description']}")
    return pending


def calculate_progress(tasks=tasks):
    if not tasks:
        print("No tasks available.")
        return 0
    completed = sum(1 for t in tasks if t["completed"])
    percentage = (completed / len(tasks)) * 100
    print(f"Progress: {completed}/{len(tasks)} tasks completed ({percentage:.1f}%)")
    return percentage