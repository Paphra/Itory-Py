
from tkinter import ttk

from ui.routine.f_make import focus
from ui.ui_main.tabs.accounts.liabilities.accruals.t_accruals import TAccruals
from .creditors.t_creditors import TCreditors


class TLiabilities:

    def __init__(self, container, s_bar, insts):

        self.host = container
        self.sb = s_bar

        self.t_liabs = ttk.Frame(self.host)
        self.mf_ntb = ttk.Notebook(self.t_liabs)

        # tabs
        self.t_accruals = TAccruals(self.mf_ntb, self.sb, insts)
        self.t_creditors = TCreditors(self.mf_ntb, self.sb, insts)

        self._works()

    def _works(self):
        self.host.add(self.t_liabs, text='Liabilities')
        self.mf_ntb.grid(column=0, row=0, sticky='NESW')

        self.mf_ntb.bind("<<NotebookTabChanged>>", self._tabchanged)

    def select_tab(self, index):
        self.mf_ntb.select(index)

    def _tabchanged(self, event=None):
        sel_tb = self.mf_ntb.tab('current')
        self.sb.lb_left['text'] = "Current Tab: " + sel_tb['text']
        _name = sel_tb['text']

        if _name == 'Creditors':
            focus(self.t_creditors.creditors_main)

        elif _name == 'Accruals':
            focus(self.t_accruals.accruals_main)
