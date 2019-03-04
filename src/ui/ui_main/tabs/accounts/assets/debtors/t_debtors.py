
import tkinter as tk
from tkinter import ttk
from ui.ui_main.tabs.commons.main import Main


class TDebtors:

    def __init__(self, nt_book, s_bar, insts):
        self.ntb = nt_book
        self.sb = s_bar
        self.deb_inst = insts['accounts'].assets.current.debtors
        self.inc_inst = insts['accounts'].statistics.income
        self.t_debtors = ttk.Frame(self.ntb)
        self.mf_debtors = ttk.Frame(self.t_debtors)
        self.debtors_main = Main(self.mf_debtors, self.sb, [self.deb_inst,
                                 self.inc_inst],
                                 'Debtors')
        
        self.t_work()

    def t_work(self):
        self.ntb.add(self.t_debtors, text='Debtors')
        self.mf_debtors.grid(column=0, row=0, padx=10, pady=10, sticky='NESW')
        self.mf_debtors.configure(width=750, height=500)
