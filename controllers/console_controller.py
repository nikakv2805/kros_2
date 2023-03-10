from models.Task import Task
from models.TaskTracking import TaskTracking

class ConsoleController:
    def __init__(self, view):
        self.view = view
        self.task_tracking = TaskTracking()
        self.task_tracking.opened.add(Task("Hello!"))
        self.task_tracking.opened.add(Task("At vero eos et accusamus et iusto odio dignissimos ducimus qui blanditiis praesentium voluptatum deleniti atque corrupti quos dolores et quas molestias excepturi sint occaecati cupiditate non provident, similique sunt in culpa qui officia deserunt mollitia animi, id est laborum et dolorum fuga. Et harum quidem rerum facilis est et expedita distinctio. Nam libero tempore, cum soluta nobis est eligendi optio cumque nihil impedit quo minus id quod maxime placeat facere possimus, omnis voluptas assumenda est, omnis dolor repellendus. Temporibus autem quibusdam et aut officiis debitis aut rerum necessitatibus saepe eveniet ut et voluptates repudiandae sint et molestiae non recusandae. Itaque earum rerum hic tenetur a sapiente delectus, ut aut reiciendis voluptatibus maiores alias consequatur aut perferendis doloribus asperiores repellat"))

    def add_task(self, text):
        self.task_tracking.add(text)
        self.view.task_added()

    def do_task(self, index):
        self.task_tracking.close(index)
        self.view.task_done()

    def del_opened_task(self, index):
        self.task_tracking.delete_opened(index)
        self.view.opened_task_deleted()

    def del_closed_task(self, index):
        self.task_tracking.delete_closed(index)
        self.view.closed_task_deleted()
