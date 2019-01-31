
from tkinter import ttk

from src.ui.routine.f_make import focus
from .purchases_ret.t_purchases_ret import TPurchasesRet
from .sales_ret.t_sales_ret import TSalesRet


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

        self.mf_ntb.bind("<<NotebookTabChanged>>", self._tabchanged)

    def select_tab(self, index):
        self.mf_ntb.select(index)

    def _tabchanged(self, event=None):
        sel_tb = self.mf_ntb.tab('current')
        self.sb.lb_left['text'] = "Current Tab: " + sel_tb['text']
        _name = sel_tb['text']

        if _name == 'Sales Returns':
            focus(self.t_sales_ret.sales_main)
        else:
            focus(self.t_pur_ret.purchases_main)
