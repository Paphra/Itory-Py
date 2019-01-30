
from tkinter import ttk
from .debtors.t_debtors import TDebtors
from .fixed_assets.t_fixed_assets import TFixedAssets
from src.ui.routine.f_make import focus


class TAssets:

    def __init__(self, container, s_bar, insts):

        self.host = container
        self.sb = s_bar

        self.t_assets = ttk.Frame(self.host)
        self.mf_ntb = ttk.Notebook(self.t_assets)

        # tabs
        self.t_debtors = TDebtors(self.mf_ntb, self.sb, insts)
        self.t_fixed_assets = TFixedAssets(self.mf_ntb, self.sb, insts)

        self._works()

    def _works(self):
        self.host.add(self.t_assets, text='Assets')
        self.mf_ntb.grid(column=0, row=0, sticky='NESW')

        self.mf_ntb.bind("<<NotebookTabChanged>>", self._tabchanged)

    def select_tab(self, index):
        self.mf_ntb.select(index)

    def _tabchanged(self, event=None):
        sel_tb = self.mf_ntb.tab('current')
        self.sb.lb_left['text'] = "Current Tab: " + sel_tb['text']

        s_tb_name = sel_tb['text']
        if s_tb_name == 'Debtors':
            focus(self.t_debtors.debtors_main)

        elif s_tb_name == 'Fixed Assets':
            pass

