
import tkinter as tk
from tkinter import ttk


class GraphList:

    def __init__(self):
        self.f_minor = ttk.Frame(self.list_pane)
        self.btn_sales = tk.Button(self.f_minor, text='Sales')
        self.btn_purch = tk.Button(self.f_minor, text='Purchases')
        self.btn_inc = tk.Button(self.f_minor, text='Income')
        self.btn_debt = tk.Button(self.f_minor, text='Debtors')
        self.btn_cred = tk.Button(self.f_minor, text='Creditors')
        self.btn_rtin = tk.Button(self.f_minor, text='Returns In')
        self.btn_rtout = tk.Button(self.f_minor, text='Returns Out')
        self.btn_exp = tk.Button(self.f_minor, text='Expenses')
        self.btn_prof_loss = tk.Button(self.f_minor, text='Profits')
        self.btn_fixed_ass = tk.Button(self.f_minor, text='Fixed Assets')
        self.btn_curr_ass = tk.Button(self.f_minor, text='Current Assets')
        self.btn_long_liabs = tk.Button(self.f_minor, text='Long Term Liabilities')
        self.btn_current_liabs = tk.Button(self.f_minor, text='Current Liabilities')

        self.btn_list = [self.btn_sales, self.btn_inc, self.btn_purch,
                         self.btn_exp, self.btn_prof_loss, self.btn_debt,
                         self.btn_cred, self.btn_rtin, self.btn_rtout,
                         self.btn_curr_ass, self.btn_fixed_ass,
                         self.btn_current_liabs, self.btn_long_liabs]

        self._works()

    def _works(self):
        self.f_minor.grid(column=0, row=0, sticky='NEWS', pady=5, padx=10)
        self.f_minor.configure(width=50, height=525)

        for btn in self.btn_list:
            btn.grid(column=0, row=self.btn_list.index(btn), sticky='E',
                     padx=20, pady=4, ipadx=5, ipady=2)
            btn.bind('<Button-1>', self.selection)
            if self.btn_list.index(btn) == 0:
                btn.configure(background='green')
            else:
                btn.configure(background='lightgrey')

    def selection(self, event=None):
        _btn = event.widget
        self.current_selection = _btn['text']
        for btn in self.btn_list:
            if btn is _btn:
                btn.configure(background='green')
            else:
                btn.configure(background='lightgrey')

        self.plot_it()
