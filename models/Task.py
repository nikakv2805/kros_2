from datetime import datetime

class Task:
    def __init__(self, text: str):
        self.text = text
        self.created = datetime.now()

    def __str__(self):
        return f"Task is {self.text}\nIt was created at {self.created}"