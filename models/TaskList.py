from models.Task import Task

class TaskList:
    def __init__(self):
        self.list = []

    def add(self, task: Task):
        self.list.append(task)

    def get(self, index: int):
        return self.list[index]

    def delete(self, index: int):
        el = self.list[index]
        self.list.remove(el)
        return el

    def __getitem__(self, item):
        return self.get(item)

    def __len__(self):
        return len(self.list)

    def __iter__(self):
        return self.list.__iter__()