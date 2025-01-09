class Task:
    def __init__(self, task_name, status="Pending"):
        self.task_name = task_name
        self.status = status
    
    def task_complete(self):
        self.status = "Completed"

    def modify_name (self, new_name):
        self.task_name = new_name

class ToDoList:
    def __init__(self):
        self.tasks = []
    
    #Add a task to the to-do list
    def add_task(self, task_name):
        task = Task (task_name)
        self.tasks.append(task)

    #List all tasks in the to-do list
    def list_tasks(self):
        if not self.tasks:
            print("No tasks.")
            return
        print("Tasks:")
        for task in self.tasks:
            print(f"- {task.task_name}")
    
    #Mark task as completed
    def complete_task(self, task_name):
        for task in self.tasks:
            if task.task_name == task_name:
                task.task_complete()
                print (f"Task: {task.task_name} has been completed!")
                return
        print(f"Task '{task_name}' not found.")
        
    #Clear the entire to-do list
    def clear_to_do_list (self):
        self.tasks.clear()
        print (f"To Do List has {self.tasks.count} tasks.")

    #Display the information of a task
    def display_task (self, task_name):
        for task in self.tasks:
            if task.task_name == task_name:
                print(f"Task: {task.task_name}")
                print(f"Status: {task.status}")
                return
        print(f"Task '{task_name}' not found.")

    #Modify the name of a task
    def modify_task(self, old_name, new_name):
        for task in self.tasks:
            if task.task_name == old_name:
                task.modify_name(new_name)
                print(f"Task '{old_name}' has been renamed to '{new_name}'.")
                return
        print(f"Task '{old_name}' not found.")