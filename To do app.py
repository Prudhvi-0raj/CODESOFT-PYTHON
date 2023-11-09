tasks = []

def show_list():
    if not tasks:
        print("Your To-Do List is empty.")
    else:
        print("To-Do List:")
        for index, task in enumerate(tasks, 1):
            print(f"{index}. {task}")


def add_task(task):
    tasks.append(task)
    print(f"Task '{task}' added to the list.")


def remove_task(task_index):
    if task_index >= 1 and task_index <= len(tasks):
        removed_task = tasks.pop(task_index - 1)
        print(f"Task '{removed_task}' removed from the list.")
    else:
        print("Invalid task index. Task not removed.")


while True:
    print("\nMenu:")
    print("1. Show To-Do List")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Quit")

    choice = input("Enter your choice: ")

    if choice == '1':
        show_list()
    elif choice == '2':
        task = input("Enter a new task: ")
        add_task(task)
    elif choice == '3':
        task_index = int(input("Enter the task number to remove: "))
        remove_task(task_index)
    elif choice == '4':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option.")
