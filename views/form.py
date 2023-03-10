from tkinter import *
from controllers.form_controller import FormController
from views.VerticalScrolledFrame import VerticalScrolledFrame
from util import str_date

WINDOW_WIDTH = 450
WINDOW_HEIGHT = 400

class Form:
    def __init__(self):
        self.controller = FormController(self)
        self.top = Tk()
        self.opened_list_visible = StringVar(value="opened")

        self.top.title("Система слідкування за задачами. Коцюбинська Вероніка")

        screen_width = self.top.winfo_screenwidth()
        screen_height = self.top.winfo_screenheight()
        x_cordinate = int((screen_width/2) - (WINDOW_WIDTH/2))
        y_cordinate = int((screen_height/2) - (WINDOW_HEIGHT/2) - 40)

        self.top.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}+{x_cordinate}+{y_cordinate}")
        self.top.resizable(0, 0)

    def name(self):
        labelName = Label(self.top, text="Система слідкування за задачами\nЛабораторна робота 2 Вероніки Коцюбинської")
        labelName.grid(row=0, padx=5, pady=5)

    def add_button(self):
        def add():
            # Set up window
            win = Toplevel()
            win.title("Додати завдання")
            win.attributes("-toolwindow", True)

            colLbl = Label(win, text="Текст завдання")
            entry = Entry(win)
            colLbl.grid(row=0, column=0, padx=5, pady=5)
            entry.grid(row=0, column=1, padx=5, pady=5)

            def UpdateThenDestroy():
                if entry.get() != "":
                    self.controller.add_task(entry.get())
                    win.destroy()

            okButt = Button(win, text="Додати")
            okButt.bind("<Button-1>", lambda e: UpdateThenDestroy())
            okButt.grid(row=1, column=0, padx=5, pady=5)

            canButt = Button(win, text="Відмінити")
            canButt.bind("<Button-1>", lambda c: win.destroy())
            canButt.grid(row=1, column=1, padx=5, pady=5, stick=W)

        button_add = Button(self.top, text="Додати завдання", command=add)
        button_add.grid(row=1, padx=5, pady=5)

    def add_opened(self):
        if len(self.controller.task_tracking.opened) > 0:
            opened_list = VerticalScrolledFrame(self.top, height=200, width=400)
            opened_list.grid(row=3, padx=5, pady=5)
            item_frames = []
            for i, task in enumerate(self.controller.task_tracking.opened):
                item_frames.append(Frame(opened_list.interior, highlightbackground="grey", highlightthickness=2, width=390))
                item_frames[i].pack(fill='x', pady=2)
                Button(item_frames[i], text="✘", height=1, width=2, command=self.controller.do_del_opened_task_action(i))\
                    .grid(row=0, column=2, padx=5, pady=5, sticky=NE)
                Button(item_frames[i], text="✔", height=1, width=2, command=self.controller.do_do_task_action(i))\
                    .grid(row=0, column=3, padx=5, pady=5, sticky=NE)
                labelText = Label(item_frames[i], text=task.text, wraplengt=300)
                labelCreated = Label(item_frames[i], text=str_date(task.created), font=("Arial", 7))
                labelText.grid(row=0, column=0, rowspan=2, padx=5, pady=5)
                labelCreated.grid(row=1, column=1, columnspan=3, padx=5, pady=2, sticky=SE)
                item_frames[i].columnconfigure(0, weight=5, minsize=300)
                item_frames[i].columnconfigure(1, weight=2, minsize=20)
                item_frames[i].columnconfigure(2, weight=1)
                item_frames[i].columnconfigure(3, weight=1)
        else:
            f = Frame(self.top, width=400, height=200)
            f.grid(row=3, padx=5, pady=5)
            l = Label(f, text="У списку немає елементів", wraplengt=300)
            l.pack()

    def add_closed(self):
        if len(self.controller.task_tracking.closed) > 0:
            closed_list = VerticalScrolledFrame(self.top, height=200, width=400)
            closed_list.grid(row=3, padx=5, pady=5)
            for i, task in enumerate(self.controller.task_tracking.closed):
                item_frame = Frame(closed_list.interior, highlightbackground="grey", highlightthickness=2, width=390)
                item_frame.pack(fill='x', pady=2)
                button_del = Button(item_frame, text="✘", height=1, width=2,
                                    command=self.controller.do_del_closed_task_action(i))
                labelText = Label(item_frame, text=task.text, wraplengt=300)
                labelCreated = Label(item_frame, text=str_date(task.created), font=("Arial", 7))
                labelText.grid(row=0, column=0, rowspan=2, padx=5, pady=5)
                labelCreated.grid(row=1, column=1, columnspan=3, padx=5, pady=2, sticky=SE)
                button_del.grid(row=0, column=3, padx=5, pady=5, sticky=NE)
                item_frame.columnconfigure(0, weight=5, minsize=300)
                item_frame.columnconfigure(1, weight=2, minsize=20)
                item_frame.columnconfigure(2, weight=1)
                item_frame.columnconfigure(3, weight=1)
        else:
            f = Frame(self.top, width=400, height=200)
            f.grid(row=3, padx=5, pady=5)
            l = Label(f, text="У списку немає елементів", wraplengt=300)
            l.pack()

    def show_list(self):
        for item in self.top.grid_slaves():
            if int(item.grid_info()["row"]) == 3:
                item.grid_forget()
        if self.opened_list_visible.get() == "opened":
            self.add_opened()
        else:
            self.add_closed()

    def switch_button(self):
        switch_frame = Frame(self.top)
        switch_frame.grid(row=2, column=0, padx=5, pady=5, columnspan=2)
        opened_button = Radiobutton(switch_frame, text="Відкриті", variable=self.opened_list_visible,
                                    indicatoron=False, value="opened", width=8, command=self.show_list)
        closed_button = Radiobutton(switch_frame, text="Виконані", variable=self.opened_list_visible,
                                    indicatoron=False, value="closed", width=8, command=self.show_list)
        opened_button.pack(side="left")
        closed_button.pack(side="right")

    def run(self):
        self.name()
        self.add_button()
        self.switch_button()
        self.show_list()
        self.top.columnconfigure(0, minsize=WINDOW_WIDTH)
        self.top.mainloop()

if __name__ == '__main__':
    form = Form()
    form.run()