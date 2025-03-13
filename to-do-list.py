class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task, "done": False})
        print("Task added successfully!")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks available.")
            return
        for idx, task in enumerate(self.tasks, start=1):
            status = "[✓]" if task["done"] else "[ ]"
            print(f"{idx}. {status} {task['task']}")

    def update_task(self, task_index):
        if 0 < task_index <= len(self.tasks):
            self.tasks[task_index - 1]["done"] = not self.tasks[task_index - 1]["done"]
            print("Task updated successfully!")
        else:
            print("Invalid task number.")

    def delete_task(self, task_index):
        if 0 < task_index <= len(self.tasks):
            self.tasks.pop(task_index - 1)
            print("Task deleted successfully!")
        else:
            print("Invalid task number.")

def main():
    todo = ToDoList()
    while True:
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")
        
        choice = input("Choose an option: ")
        if choice == "1":
            task = input("Enter task: ")
            todo.add_task(task)
        elif choice == "2":
            todo.view_tasks()
        elif choice == "3":
            todo.view_tasks()
            index = int(input("Enter task number to update: "))
            todo.update_task(index)
        elif choice == "4":
            todo.view_tasks()
            index = int(input("Enter task number to delete: "))
            todo.delete_task(index)
        elif choice == "5":
            print("Exiting application. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
