class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})
        print(f"Task added: {task}")

    def remove_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            removed_task = self.tasks.pop(task_index)
            print(f"Task removed: {removed_task['task']}")
        else:
            print("Invalid task number.")

    def complete_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index]["completed"] = True
            print(f"Task marked as completed: {self.tasks[task_index]['task']}")
        else:
            print("Invalid task number.")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks available.")
        else:
            print("\nTo-Do List:")
            for idx, task in enumerate(self.tasks):
                status = "✔ Completed" if task["completed"] else "❌ Pending"
                print(f"{idx + 1}. {task['task']} - {status}")

if __name__ == "__main__":
    todo = ToDoList()
    while True:
        print("\nOptions: 1-Add Task | 2-Remove Task | 3-Complete Task | 4-View Tasks | 5-Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter the task: ")
            todo.add_task(task)
        elif choice == "2":
            todo.view_tasks()
            index = int(input("Enter task number to remove: ")) - 1
            todo.remove_task(index)
        elif choice == "3":
            todo.view_tasks()
            index = int(input("Enter task number to mark as completed: ")) - 1
            todo.complete_task(index)
        elif choice == "4":
            todo.view_tasks()
        elif choice == "5":
            print("Exiting To-Do List App. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
