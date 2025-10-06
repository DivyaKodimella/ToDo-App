def mark_task_as_done(tasks_list):
    """
    Changes a task's status from "Pending" to "Done".
    """
    if not tasks_list:
        print("\nNo tasks to mark as done.")
        return
    
    try:
        task_id = int(input("Enter the ID of the task to mark as done: ").strip())
    except ValueError:
        print("\nInvalid ID. Please enter a number.")
        return

    task_to_mark = None
    for task in tasks_list:
        if task['id'] == task_id:
            task_to_mark = task
            break
            
    if task_to_mark is None:
        print("\nTask with that ID not found.")
        return
        
    if task_to_mark['status'] == 'Done':
        print("\nThis task has already been marked as done.")
    else:
        task_to_mark['status'] = 'Done'
        print(f"\nTask '{task_to_mark['task']}' marked as done.")
