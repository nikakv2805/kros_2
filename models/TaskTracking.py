from models.Task import Task
from models.TaskList import TaskList

class TaskTracking:
    def __init__(self):
        self.opened = TaskList()
        self.closed = TaskList()

    def add(self, text: str):
        task = Task(text)
        self.opened.add(task)

    def close(self, index: int):
        task = self.opened.delete(index)
        self.closed.add(task)

    def delete_opened(self, index: int):
        self.opened.delete(index)

    def delete_closed(self, index: int):
        self.closed.delete(index)