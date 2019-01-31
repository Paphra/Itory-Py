from tkinter import ttk

from src.ui.ui_main.tabs.commons.main import Main


class TFixedAssets:

    def __init__(self, nt_book, s_bar, insts):
        self.ntb = nt_book
        self.sb = s_bar
        self.fixed_inst = insts['accounts'].assets.fixed
        self.t_fixed = ttk.Frame(self.ntb)
        self.mf_fixed = ttk.Frame(self.t_fixed)
        self.fixed_main = Main(self.mf_fixed, self.sb,
                               self.fixed_inst,
                               'Fixed Assets')

        self.t_work()

    def t_work(self):
        self.ntb.add(self.t_fixed, text='Fixed Assets')
        self.mf_fixed.grid(column=0, row=0, padx=10, pady=10, sticky='NESW')
        self.mf_fixed.configure(width=750, height=500)
