
import tkinter as tk
from tkinter import ttk
from ui.ui_main.tabs.commons.main import Main


class TExpenses:

    def __init__(self, nt_book, s_bar, insts):
        self.ntb = nt_book
        self.sb = s_bar
        self.exp_inst = insts['accounts'].expenses
        self.t_expenses = ttk.Frame(self.ntb)
        self.mf_expenses = ttk.Frame(self.t_expenses)
        self.expenses_main = Main(self.mf_expenses, self.sb, self.exp_inst,
                                  'Expenses')
        
        self.t_work()

    def t_work(self):
        self.ntb.add(self.t_expenses, text='Expenses')
        self.mf_expenses.grid(column=0, row=0, padx=10, pady=10, sticky='NESW')
        self.mf_expenses.configure(width=750, height=500)
