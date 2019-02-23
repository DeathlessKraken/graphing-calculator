from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
from matplotlib import style


class Widgets(ttk.Frame):
    formula = "(x**3-2*x)/(2*(x**2-5))"
    view_size = 8.0

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.create_widgets(master)
        self.grid()

    def exit(self):
        self.master.master.destroy()

    def create_widgets(self, master):
        SUB = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")

        quit = ttk.Button(self, text="QUIT", command=self.exit)
        quit.grid(row=2, column=0)

        # This table label is being created in the mainFrame
        table_l = ttk.Label(self.master, text="Table")
        table_l.grid(row=0, column=1, sticky='n')

        y1_c = ttk.Checkbutton(master, text="Y1".translate(SUB))
        y1_c.grid(row=1, column=0)


class Graph(ttk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.create_widgets(master)
        self.grid(sticky='w')

    def exit(self):
        self.master.master.destroy()

    def create_widgets(self, master):
        style.use('fivethirtyeight')
        f = Figure(figsize=(7, 5), dpi=100)
        a = f.add_subplot(111)
        #t = arange(0.0, 3.0, 0.01)
        #s = sin(2 * pi * t)

        canvas = FigureCanvasTkAgg(f, master=master)
        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update()
        canvas.get_tk_widget().grid(row=1, column=0)
