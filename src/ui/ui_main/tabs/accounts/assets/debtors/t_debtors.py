
from tkinter import ttk


class TDebtors:

    def __init__(self, container, s_bar, insts):

        self.host = container
        self.sb = s_bar

        self.t_debt = ttk.Frame(self.host)
        self.mf = ttk.Frame(self.t_debt)

        self._works()

    def _works(self):
        self.host.add(self.t_debt, text='Debtors')
        self.mf.grid(column=0, row=0, sticky='NESW')
