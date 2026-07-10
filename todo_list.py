tasks = []
def show_tasks():
    if not tasks:
        print("No tasks available.")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")
while True:
    print("\n---- To_Do List----")
    print("1. Add Task")
    print("2. View Task")
    print("3. Remove Task")
    print("4. Exit")
    choice = input("Enter your choice(1-4): ")
    if choice == "1":
        task = input("Enter the task: ")
        tasks.append(task)
    elif choice == "2":
        show_tasks()
    elif choice == "3":
        show_tasks()
        try:
            number= int(input("Enter the task number to remove: "))
            removed=tasks.pop(number-1)
            print(f"Removed:{removed}")
        except (ValueError, IndexError):
            print("Invalid task number.")
    elif choice == "4":
         print("Goodbye!")
         break
    else:
        print("Invalid choice. Please try again.")

 


                  