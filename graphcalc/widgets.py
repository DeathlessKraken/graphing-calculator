from tkinter import ttk
from numpy import arange, sin, pi
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
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
        self.quit = ttk.Button(self, text="QUIT", command=self.exit)
        self.quit.grid(row=0, column=0)

        self.table_l = ttk.Label(self, text="Table").grid(row=1, column=0)

        self.f = Figure(figsize=(7, 5), dpi=100)
        self.a = self.f.add_subplot(111)
        self.t = arange(0.0, 3.0, 0.01)
        self.s = sin(2 * pi * self.t)

        self.a.plot(self.t, self.s)
        # self.a.set_title('Linear Regression')
        # self.a.set_xlabel('X axis label')
        # self.a.set_ylabel('Y label')

        self.canvas = FigureCanvasTkAgg(self.f, master=master)
        self.canvas.get_tk_widget().grid(row=1, column=0)
