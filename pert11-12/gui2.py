import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Garden App")
        self.geometry('300x50')
        self.label = ttk.Label(self, text='silahkan berikan air')
        self.label.pack()

        self.button = ttk.Button(self, text='click me')
        self.button['command'] = self.button_click
        self.button.pack()

    def button_click(self):
        showinfo(title='info', message='sudah di beri air')

if __name__ == "__main__":
    app = App()
    app.mainloop()