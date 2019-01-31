from tkinter import ttk

from src.ui.ui_main.tabs.commons.main import Main


class TAccruals:

    def __init__(self, nt_book, s_bar, insts):
        self.ntb = nt_book
        self.sb = s_bar
        self.accr_inst = insts['accounts'].liabilities.accruals
        self.t_accruals = ttk.Frame(self.ntb)
        self.mf_accruals = ttk.Frame(self.t_accruals)
        self.accruals_main = Main(self.mf_accruals, self.sb, self.accr_inst,
                                  'Accruals')

        self.t_work()

    def t_work(self):
        self.ntb.add(self.t_accruals, text='Accruals')
        self.mf_accruals.grid(column=0, row=0, padx=10, pady=10, sticky='NESW')
        self.mf_accruals.configure(width=750, height=500)
