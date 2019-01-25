
from tkinter import ttk


class TDrawings:

    def __init__(self, container, s_bar, insts):

        self.host = container
        self.sb = s_bar

        self.t_drawings = ttk.Frame(self.host)
        self.mf = ttk.Frame(self.t_drawings)

        self._works()

    def _works(self):
        self.host.add(self.t_drawings, text='Drawings')
        self.mf.grid(column=0, row=0, sticky='NESW')
