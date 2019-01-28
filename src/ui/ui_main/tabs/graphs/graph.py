
from tkinter import ttk
import tkinter as tk
import numpy as np
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class Graph:

    def __init__(self):
        pass

    def plot_it(self):
        for child in self.graph_canvas.winfo_children():
            child.destroy()
        fig = Figure(figsize=(7, 3.8), facecolor='white')

        axis = fig.add_subplot(111)
        axis.plot(self.x_values, self.y_values, marker='o')

        axis.set_xlabel(self.x_label)
        axis.set_ylabel(self.y_label)
        fig.suptitle(self.graph_title)

        axis.grid(linestyle='-')

        canvas = FigureCanvasTkAgg(fig, master=self.graph_canvas)
        canvas._tkcanvas.pack(side=tk.RIGHT, fill=tk.BOTH, expand=1)
