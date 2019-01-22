
from tkinter import ttk


class TExpenses:

    def __init__(self, container, s_bar, acc_inst):

        self.host = container
        self.sb = s_bar
        self.acc_inst = acc_inst

        self.t_exp = ttk.Frame(self.host)
        self.mf = ttk.Frame(self.t_exp)

        self._works()

    def _works(self):
        self.host.add(self.t_exp, text='Expenses')
        self.mf.grid(column=0, row=0, sticky='NESW')
