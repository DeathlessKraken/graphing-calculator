from tkinter import *
from tkinter import ttk
from graphcalc.widgets import Widgets

WIDTH = 800
HEIGHT = 600


def create_app():
    # Configure main window environment
    root = Tk()
    root.geometry(str(WIDTH) + 'x' + str(HEIGHT))
    root.title("Graphing Calculator by Sean")

    displayFrame = ttk.Frame(root, padding="3 3 12 12")
    displayFrame.grid(column=0, row=0, sticky=(N, W, E, S))
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    # Create new instance of widgets
    w = Widgets(master=displayFrame)

    return root
