def update_task(tasks_list):
    """
    Edits the description of an existing task.
    """
    if not tasks_list:
        print("\nNo tasks to update.")
        return

    try:
        task_id = int(input("Enter the ID of the task to update: ").strip())
    except ValueError:
        print("\nInvalid ID. Please enter a number.")
        return
        
    task_to_update = None
    for task in tasks_list:
        if task['id'] == task_id:
            task_to_update = task
            break
            
    if task_to_update is None:
        print("\nTask with that ID not found.")
        return
        
    new_description = input(f"Enter the new description for task '{task_to_update['task']}': ").strip()
    if new_description:
        task_to_update['task'] = new_description
        print("\nTask updated successfully.")
    else:
        print("\nDescription cannot be empty. Update cancelled.")
