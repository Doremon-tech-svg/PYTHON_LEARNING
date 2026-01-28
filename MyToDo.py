tasks = []

def show_menu():
    print("\n---- TO DO LIST ----")
    print("1. Show tasks")
    print("2. Add task")
    print("3. Remove task")
    print("4. Exit")

def show_tasks():
    if len(tasks) == 0:
        print("No tasks yet!")
    else:
        print("\nYour tasks:")
        for i in range(len(tasks)):
            print(i + 1, "-", tasks[i])

def add_task():
    task = input("Enter a new task: ")
    tasks.append(task)
    print("Task added!")

def remove_task():
    show_tasks()
    if len(tasks) == 0:
        return
    num = int(input("Enter task number to remove: "))
    if num > 0 and num <= len(tasks):
        removed = tasks.pop(num - 1)
        print("Removed:", removed)
    else:
        print("Invalid number")

while True:
    show_menu()
    choice = input("Choose an option (1-4): ")

    if choice == "1":
        show_tasks()
    elif choice == "2":
        add_task()
    elif choice == "3":
        remove_task()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice, try again.")
