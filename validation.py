from datetime import datetime

def validate_task_title(title):
    if not title or len(title.strip()) == 0:
        return False, "Title cannot be empty."
    if len(title.strip()) < 3:
        return False, "Title must be at least 3 characters long."
    return True, ""


def validate_task_description(description):
    if not description or len(description.strip()) == 0:
        return False, "Description cannot be empty."
    return True, ""


def validate_due_date(due_date):
    if not due_date or len(due_date.strip()) == 0:
        return False, "Due date cannot be empty."
    parts = due_date.strip().split("-")
    if len(parts) != 3:
        return False, "Due date must be in YYYY-MM-DD format."
    year, month, day = parts
    if not (year.isdigit() and month.isdigit() and day.isdigit()):
        return False, "Due date must contain only numbers."
    if not (1 <= int(month) <= 12):
        return False, "Month must be between 01 and 12."
    if not (1 <= int(day) <= 31):
        return False, "Day must be between 01 and 31."
    return True, ""