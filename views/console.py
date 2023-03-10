from controllers.console_controller import ConsoleController
from util import str_date

ACTIONS_SET = {'a', 'po', 'pc', 'p', 'd', 'do', 'dc', 'q'}

class ConsoleView:
    def __init__(self):
        self.controller = ConsoleController(self)

    def add_new(self):
        print("Please, enter the description of the action: ", end='')
        text = input()
        self.controller.add_task(text)

    def print_opened(self):
        print("Here are all the opened tasks:")
        for i, task in enumerate(self.controller.task_tracking.opened):
            print(f"\t{i:3d}. {task.text}. Created at {str_date(task.created)}")

    def print_closed(self):
        print("Here are all the closed tasks:")
        for i, task in enumerate(self.controller.task_tracking.closed):
            print(f"\t{i:3d}. {task.text}. Created at {str_date(task.created)}")

    def print_all(self):
        self.print_opened()
        self.print_closed()

    def task_added(self):
        print("Successfully added new task")

    def task_done(self):
        print("Successfully done task")

    def opened_task_deleted(self):
        print("Successfully deleted opened task")

    def closed_task_deleted(self):
        print("Successfully deleted closed task")

    def do_close_task(self):
        if len(self.controller.task_tracking.opened) == 0:
            print("There are no opened task to do")
            return
        print("Please, choose, what task do you want to close.")
        while True:
            print("Enter task's ID (if you want us to remind you opened tasks, print 'r'; to return to menu, print 'm'): ", end='')
            action = input().lower()
            if action == 'r':
                self.print_opened()
                print("Please, enter done task's id (or 'm' for menu): ")
                action = input().lower()
            if action == 'm':
                return
            if action.isdigit() and 0 <= int(action) < len(self.controller.task_tracking.opened):
                break
        index = int(action)
        self.controller.do_task(index)

    def delete_opened(self):
        if len(self.controller.task_tracking.opened) == 0:
            print("There are no opened task to delete")
            return
        print("Please, choose, what task do you want to delete.")
        while True:
            print("Enter task's ID (if you want us to remind you opened tasks,"
                  " print 'r'; to return to menu, print 'm'): ", end='')
            action = input().lower()
            if action == 'r':
                self.print_opened()
                print("Please, enter task's id (or 'm' for menu): ")
                action = input().lower()
            if action == 'm':
                return
            if action.isdigit() and 0 <= int(action) < len(self.controller.task_tracking.opened):
                break
        index = int(action)
        self.controller.del_opened_task(index)

    def delete_closed(self):
        if len(self.controller.task_tracking.closed) == 0:
            print("There are no closed task to delete")
            return
        print("Please, choose, what task do you want to delete.")
        while True:
            print("Enter task's ID (if you want us to remind closed "
                  "tasks to you, print 'r'; to return to menu, print 'm'): ", end='')
            action = input().lower()
            if action == 'r':
                self.print_opened()
                print("Please, enter task's id (or 'm' for menu): ")
                action = input().lower()
            if action == 'm':
                return
            if action.isdigit() and 0 <= int(action) < len(self.controller.task_tracking.closed):
                break
        index = int(action)
        self.controller.del_closed_task(index)

    def get_action(self):
        print("What do you want to do?")
        print("Options are:\n- a - add new task;\n- po - print opened tasks;")
        print("- pc - print closed tasks;\n- p - print all tasks;\n- d - do and close task;")
        print("- do - delete opened task;\n- dc - delete closed task;\n- q - quit and close program.")
        print("Choose one [a/po/pc/p/d/do/dc/q]: ", end='')
        action = input().lower()
        while action not in ACTIONS_SET:
            print("Your answer isn't one of the possible.\n Please, choose one among [a/po/pc/p/d/do/dc/q]: ", end='')
            action = input().lower()
        if action == 'q':
            quit(0)
        elif action == 'a':
            print("Ok, you've chosen to add new action.")
            self.add_new()
        elif action == 'po':
            print("Ok, you've chosen to print all opened tasks.")
            self.print_opened()
        elif action == 'pc':
            print("Ok, you've chosen to print all closed tasks.")
            self.print_closed()
        elif action == 'p':
            print("Ok, you've chosen to print all tasks.")
            self.print_all()
        elif action == 'd':
            print("Ok, you've decided to do and close task.")
            self.do_close_task()
        elif action == 'do':
            print("Ok, you've decided to delete opened task.")
            self.delete_opened()
        elif action == 'dc':
            print("Ok, you've decided to delete closed task.")
            self.delete_closed()

    def main(self):
        print("Welcome to my task tracking system!")
        while True:
            self.get_action()
            print()

if __name__ == '__main__':
    view = ConsoleView()
    view.main()