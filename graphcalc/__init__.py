from tkinter import *
from tkinter import ttk
from graphcalc.widgets import *

WIDTH = 800
HEIGHT = 600


def create_app():
    # Configure main window environment
    root = Tk()
    #root.geometry(str(WIDTH) + 'x' + str(HEIGHT))
    root.resizable(False, False)
    root.title("Graphing Calculator by Sean")

    mainFrame = ttk.Frame(root, padding="5")
    mainFrame.grid(column=0, row=0, sticky='n s w e')

    graphFrame = ttk.Frame(mainFrame, padding='5')
    graphFrame.grid(row=0, column=0, sticky='n w')

    #root.columnconfigure(0, weight=1)
    #root.rowconfigure(0, weight=1)

    # Create new instance of widgets
    w = Widgets(master=mainFrame)
    g = Graph(master=graphFrame)

    return root
