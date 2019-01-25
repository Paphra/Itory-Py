
from tkinter import ttk


class TFixedAssets:

    def __init__(self, container, s_bar, insts):

        self.host = container
        self.sb = s_bar

        self.t_fixed_assets = ttk.Frame(self.host)
        self.mf = ttk.Frame(self.t_fixed_assets)

        self._works()

    def _works(self):
        self.host.add(self.t_fixed_assets, text='Fixed Assets')
        self.mf.grid(column=0, row=0, sticky='NESW')
