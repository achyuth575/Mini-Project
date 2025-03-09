class TaskNode:
    """A node in the doubly linked list for tasks."""
    def _init_(self, task):
        self.task = task
        self.prev = None
        self.next = None

class TaskManager:
    def _init_(self):
        self.head = None  # Head of the doubly linked list
        self.tail = None  # Tail of the doubly linked list
        self.undo_stack = []  # Stack for undo actions
        self.redo_stack = []  # Stack for redo actions
        self.task_queue = []  # Simple queue for scheduled tasks

    def add_task(self, task):
        """Adds a new task to the linked list."""
        new_node = TaskNode(task)
        if not self.head:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

        self.undo_stack.append(("add", task))  # Store in undo stack
        self.redo_stack.clear()  # Clear redo stack after a new action
        print(f"✅ Task added: {task}")

    def remove_task(self, task):
        """Removes a task from the linked list."""
        current = self.head
        while current:
            if current.task == task:
                if current.prev:
                    current.prev.next = current.next
                if current.next:
                    current.next.prev = current.prev
                if current == self.head:
                    self.head = current.next
                if current == self.tail:
                    self.tail = current.prev

                self.undo_stack.append(("remove", task))
                self.redo_stack.clear()
                print(f"❌ Task removed: {task}")
                return
            current = current.next

        print(f"⚠ Task '{task}' not found!")

    def view_tasks(self):
        """Displays all tasks."""
        if not self.head:
            print("📭 No tasks available.")
            return

        print("\n📋 Your Tasks:")
        current = self.head
        while current:
            print(f"- {current.task}")
            current = current.next

    def undo(self):
        """Undoes the last action."""
        if not self.undo_stack:
            print("⚠ Nothing to undo!")
            return

        action, task = self.undo_stack.pop()
        if action == "add":
            self.remove_task(task)
            self.redo_stack.append(("add", task))
        elif action == "remove":
            self.add_task(task)
            self.redo_stack.append(("remove", task))

    def redo(self):
        """Redoes the last undone action."""
        if not self.redo_stack:
            print("⚠ Nothing to redo!")
            return

        action, task = self.redo_stack.pop()
        if action == "add":
            self.add_task(task)
        elif action == "remove":
            self.remove_task(task)

    def schedule_task(self, task):
        """Adds a task to the queue for future execution."""
        self.task_queue.append(task)
        print(f"📅 Task scheduled: {task}")

    def view_scheduled_tasks(self):
        """Displays scheduled tasks."""
        if not self.task_queue:
            print("📭 No scheduled tasks.")
            return

        print("\n⏳ Scheduled Tasks:")
        for task in self.task_queue:
            print(f"- {task}")

# Command-line interface
if __name__ == "__main__":
    task_manager = TaskManager()

    while True:
        print("\n📌 Task Manager")
        print("⿡ Add Task")
        print("⿢ Remove Task")
        print("⿣ View Tasks")
        print("⿤ Undo")
        print("⿥ Redo")
        print("⿦ Schedule Task")
        print("⿧ View Scheduled Tasks")
        print("⿨ Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            task_name = input("Enter task name: ")
            task_manager.add_task(task_name)

        elif choice == "2":
            task_name = input("Enter task name to remove: ")
            task_manager.remove_task(task_name)

        elif choice == "3":
            task_manager.view_tasks()

        elif choice == "4":
            task_manager.undo()

        elif choice == "5":
            task_manager.redo()

        elif choice == "6":
            task_name = input("Enter task name to schedule: ")
            task_manager.schedule_task(task_name)

        elif choice == "7":
            task_manager.view_scheduled_tasks()

        elif choice == "8":
            print("👋 Exiting Task Manager. Have a productive day!")
            break

        else:
            print("⚠ Invalid choice. Please try again.")
