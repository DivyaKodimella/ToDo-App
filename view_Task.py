def view_tasks(tasks_list):
    """
    Displays all tasks with their ID, description, and status.
    """
    print("\n--- Your To-Do List ---")
    if not tasks_list:
        print("No tasks available.")
    else:
        print(f"{'ID':<5} {'Status':<10} {'Task':<30}")
        print("-" * 47)
        for task in tasks_list:
            print(f"{task['id']:<5} {task['status']:<10} {task['task']:<30}")
    print("-------------------------")