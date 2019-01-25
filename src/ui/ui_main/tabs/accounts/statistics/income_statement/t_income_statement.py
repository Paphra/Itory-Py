
from tkinter import ttk


class TIncomeStatement:

    def __init__(self, container, s_bar, insts):

        self.host = container
        self.sb = s_bar

        self.t_inc_stmt = ttk.Frame(self.host)
        self.mf = ttk.Frame(self.t_inc_stmt)

        self._works()

    def _works(self):
        self.host.add(self.t_inc_stmt, text='Income Statement')
        self.mf.grid(column=0, row=0, sticky='NESW')
