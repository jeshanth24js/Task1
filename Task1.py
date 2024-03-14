import json
import datetime

class Task:
    def __init__(self, title, priority, due_date):
        self.title = title
        self.priority = priority
        self.due_date = due_date
        self.completed = False

    def mark_as_completed(self):
        self.completed = True

class TodoList:
    def __init__(self, filename):
        self.tasks = []
        self.filename = filename

    def add_task(self, title, priority, due_date):
        task = Task(title, priority, due_date)
        self.tasks.append(task)

    def remove_task(self, title):
        self.tasks = [task for task in self.tasks if task.title != title]

    def mark_task_as_completed(self, title):
        for task in self.tasks:
            if task.title == title:
                task.mark_as_completed()
                break

    def save_tasks(self):
        with open(self.filename, 'w') as f:
            json.dump([task.__dict__ for task in self.tasks], f)

    def load_tasks(self):
        try:
            with open(self.filename, 'r') as f:
                self.tasks = [Task(**task) for task in json.load(f)]
        except FileNotFoundError:
            self.tasks = []

    def display_tasks(self):
        for task in self.tasks:
            print(f"Title: {task.title}, Priority: {task.priority}, Due Date: {task.due_date}, Completed: {task.completed}")

todo_list = TodoList('tasks.json')
todo_list.load_tasks()
todo_list.display_tasks()
