
from tkinter import ttk


class TBalanceSheet:

    def __init__(self, container, s_bar, sales_inst, pur_inst, acc_inst):

        self.host = container
        self.sb = s_bar
        self.acc_inst = acc_inst

        self.t_bal_sheet = ttk.Frame(self.host)
        self.mf = ttk.Frame(self.t_bal_sheet)

        self._works()

    def _works(self):
        self.host.add(self.t_bal_sheet, text='Balance Sheet')
        self.mf.grid(column=0, row=0, sticky='NESW')
