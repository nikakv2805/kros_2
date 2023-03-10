import tkinter as tk

class Model:
    def __init__(self):
        self.value = 0

    def increment(self):
        self.value += 1

    def get_value(self):
        return self.value

class View(tk.Frame):
    def __init__(self, master, controller):
        super().__init__(master)
        self.controller = controller

        self.label = tk.Label(self, text="0")
        self.label.pack()

        self.button = tk.Button(self, text="Increment", command=self.controller.increment_value)
        self.button.pack()

    def update(self, value):
        self.label.config(text=value)

class Controller:
    def __init__(self):
        self.model = Model()
        self.view = View(master=None, controller=self)

    def increment_value(self):
        self.model.increment()
        self.view.update(self.model.get_value())

if __name__ == '__main__':
    root = tk.Tk()
    controller = Controller()
    controller.view.pack()
    root.mainloop()