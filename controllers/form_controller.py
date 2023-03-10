from models.Task import Task
from models.TaskTracking import TaskTracking

class FormController:
    def __init__(self, view):
        self.view = view
        self.task_tracking = TaskTracking()
        self.task_tracking.opened.add(Task("Hello!"))
        self.task_tracking.opened.add(Task("At vero eos et accusamus et iusto odio dignissimos ducimus qui blanditiis praesentium voluptatum deleniti atque corrupti quos dolores et quas molestias excepturi sint occaecati cupiditate non provident, similique sunt in culpa qui officia deserunt mollitia animi, id est laborum et dolorum fuga. Et harum quidem rerum facilis est et expedita distinctio. Nam libero tempore, cum soluta nobis est eligendi optio cumque nihil impedit quo minus id quod maxime placeat facere possimus, omnis voluptas assumenda est, omnis dolor repellendus. Temporibus autem quibusdam et aut officiis debitis aut rerum necessitatibus saepe eveniet ut et voluptates repudiandae sint et molestiae non recusandae. Itaque earum rerum hic tenetur a sapiente delectus, ut aut reiciendis voluptatibus maiores alias consequatur aut perferendis doloribus asperiores repellat"))

    def add_task(self, text):
        self.task_tracking.add(text)
        self.view.show_list()

    def do_do_task_action(self, index):
        def do_task():
            self.task_tracking.close(index)
            self.view.show_list()
        return do_task

    def do_del_opened_task_action(self, index):
        def del_opened_task():
            self.task_tracking.delete_opened(index)
            self.view.show_list()
        return del_opened_task

    def do_del_closed_task_action(self, index):
        def del_closed_task():
            self.task_tracking.delete_closed(index)
            self.view.show_list()
        return del_closed_task