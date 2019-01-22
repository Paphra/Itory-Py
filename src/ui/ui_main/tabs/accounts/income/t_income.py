
from tkinter import ttk


class TIncome:

    def __init__(self, container, s_bar, acc_inst):

        self.host = container
        self.sb = s_bar
        self.acc_inst = acc_inst

        self.t_inc = ttk.Frame(self.host)
        self.mf = ttk.Frame(self.t_inc)

        self._works()

    def _works(self):
        self.host.add(self.t_inc, text='Income')
        self.mf.grid(column=0, row=0, sticky='NESW')
