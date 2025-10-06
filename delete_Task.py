def delete_task(tasks_list):
    """
    Removes a task from the list by its ID.
    """
    if not tasks_list:
        print("\nNo tasks to delete.")
        return
        
    try:
        task_id = int(input("Enter the ID of the task to delete: ").strip())
    except ValueError:
        print("\nInvalid ID. Please enter a number.")
        return

    task_found = False
    for i, task in enumerate(tasks_list):
        if task['id'] == task_id:
            removed_task_desc = tasks_list.pop(i)['task']
            task_found = True
            break
    
    if task_found:
        print(f"\nSuccessfully deleted task: '{removed_task_desc}'")
    else:
        print("\nTask with that ID not found.")
