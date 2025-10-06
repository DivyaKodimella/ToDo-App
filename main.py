from data_Schema import tasks
from add_Task import add_task
from delete_Task import delete_task
from done_Task import mark_task_as_done
from update_Task import update_task
from view_Task import view_tasks

def menu():
    """
    Displays the main menu for the To-Do List application.
    """
    print("\n===== To-Do List Application =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Mark Task as Done")
    print("5. Delete Task")
    print("6. Exit")
    print("==================================")

if __name__ == "__main__":
    while True:
        menu()
        choice = input("Enter your choice: ")
        
        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            update_task(tasks)
        elif choice == '4':
            mark_task_as_done(tasks)
        elif choice == '5':
            delete_task(tasks)
        elif choice == '6':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice, please enter a number between 1 and 6.")
            
        input("\nPress Enter to continue...")

