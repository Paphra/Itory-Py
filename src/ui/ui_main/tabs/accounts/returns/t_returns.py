
from tkinter import ttk
from .sales_ret.t_sales_ret import TSalesRet
from .purchases_ret.t_purchases_ret import TPurchasesRet


class TReturns:

    def __init__(self, container, s_bar, insts):

        self.host = container
        self.sb = s_bar

        self.t_returns = ttk.Frame(self.host)
        self.mf_ntb = ttk.Notebook(self.t_returns)

        # tabs
        self.t_sales_ret = TSalesRet(self.mf_ntb, self.sb, insts)
        self.t_pur_ret = TPurchasesRet(self.mf_ntb, self.sb, insts)

        self._works()

    def _works(self):
        self.host.add(self.t_returns, text='Returns')
        self.mf_ntb.grid(column=0, row=0, sticky='NESW')
