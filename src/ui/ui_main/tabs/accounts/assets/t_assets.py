
from tkinter import ttk
from .debtors.t_debtors import TDebtors
from .fixed_assets.t_fixed_assets import TFixedAssets


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
