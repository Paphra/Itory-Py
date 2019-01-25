
from tkinter import ttk


class TSalesRet:

    def __init__(self, container, s_bar, insts):

        self.host = container
        self.sb = s_bar

        self.t_sales_ret = ttk.Frame(self.host)
        self.mf = ttk.Frame(self.t_sales_ret)

        self._works()

    def _works(self):
        self.host.add(self.t_sales_ret, text='Sales Returns')
        self.mf.grid(column=0, row=0, sticky='NESW')
