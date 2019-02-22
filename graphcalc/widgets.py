from tkinter import ttk
from numpy import arange, sin, pi
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure


class Widgets(ttk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.create_widgets(master)
        self.grid()

    def exit(self):
        self.master.master.destroy()

    def create_widgets(self, master):
        quit = ttk.Button(self, text="QUIT", command=self.exit)
        quit.grid(row=0, column=0)

        # This table label is being created in the mainFrame
        table_l = ttk.Label(self.master, text="Table")
        table_l.grid(row=0, column=1, sticky='n')


class Graph(ttk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.create_widgets(master)
        self.grid(sticky='w')

    def exit(self):
        self.master.master.destroy()

    def create_widgets(self, master):
        f = Figure(figsize=(7, 5), dpi=100)
        a = f.add_subplot(111)
        t = arange(0.0, 3.0, 0.01)
        s = sin(2 * pi * t)

        a.plot(t, s)

        canvas = FigureCanvasTkAgg(f, master=master)
        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update()
        canvas.get_tk_widget().grid(row=1, column=0)
