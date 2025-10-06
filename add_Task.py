from data_Schema import MAX_TASKS

def add_task(tasks_list):
    """
    Adds a new task to the list with a unique ID and "Pending" status.
    - Checks if the task limit has been reached.
    """
    global next_task_id
    if len(tasks_list) >= MAX_TASKS:
        print(f"\nError: Cannot add more tasks. The limit of {MAX_TASKS} has been reached.")
        return

    print("\n--- Add New Task ---")
    description = input("Enter the task description: ").strip()

    if not description:
        print("\nError: Task description cannot be empty.")
        return
    
    task = {
        "id": next_task_id,
        "task": description,
        "status": "Pending"
    }
    tasks_list.append(task)
    next_task_id += 1 # Increment for the next task
    print(f"\nSuccessfully added task: '{description}'")
