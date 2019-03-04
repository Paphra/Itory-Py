
import tkinter as tk
from tkinter import ttk
from ui.ui_main.tabs.commons.main import Main


class TIncome:

    def __init__(self, nt_book, s_bar, insts):
        self.ntb = nt_book
        self.sb = s_bar
        self.inc_inst = insts['accounts'].statistics.income
        self.t_income = ttk.Frame(self.ntb)
        self.mf_income = ttk.Frame(self.t_income)
        self.income_main = Main(self.mf_income, self.sb, self.inc_inst,
                                'Income')
        
        self.t_work()

    def t_work(self):
        self.ntb.add(self.t_income, text='Income')
        self.mf_income.grid(column=0, row=0, padx=10, pady=10, sticky='NESW')
        self.mf_income.configure(width=750, height=500)
