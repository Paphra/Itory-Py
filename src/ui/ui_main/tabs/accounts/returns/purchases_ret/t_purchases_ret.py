
from tkinter import ttk


class TPurchasesRet:

    def __init__(self, container, s_bar, insts):

        self.host = container
        self.sb = s_bar

        self.t_pur_ret = ttk.Frame(self.host)
        self.mf = ttk.Frame(self.t_pur_ret)

        self._works()

    def _works(self):
        self.host.add(self.t_pur_ret, text='Purchases Returns')
        self.mf.grid(column=0, row=0, sticky='NESW')