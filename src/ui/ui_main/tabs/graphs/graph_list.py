from src.ui.routine.widget_works import *
import tkinter as tk
from tkinter import ttk
from datetime import datetime


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

        # not included
        self.btn_curr_ass = tk.Button(self.f_minor, text='Current Assets')
        self.btn_current_liabs = tk.Button(self.f_minor, text='Current Liabilities')
        self.btn_long_liabs = tk.Button(self.f_minor, text='Long Term Liabilities')

        self.btn_list = [self.btn_sales, self.btn_purch, self.btn_inc,
                         self.btn_exp, self.btn_prof_loss, self.btn_debt,
                         self.btn_cred, self.btn_rtin, self.btn_rtout,
                         self.btn_fixed_ass]

        self._works()

    def _works(self):
        self.f_minor.grid(column=0, row=0, sticky='NEWS', pady=5, padx=2)
        self.f_minor.configure(width=50, height=525)

        for btn in self.btn_list:
            btn.grid(column=0, row=self.btn_list.index(btn), sticky='E',
                     padx=5, pady=4, ipadx=5)
            btn.bind('<Button-1>', self.selection)
            if self.btn_list.index(btn) == 0:
                btn.configure(background='green')
            else:
                btn.configure(background='lightgrey')

    def selection(self, event=None):
        if event is None:
            self.current_selection = 'Sales'
        else:
            _btn = event.widget
            self.current_selection = _btn['text']
        for btn in self.btn_list:
            if btn['text'] == self.current_selection:
                btn.configure(background='green')
            else:
                btn.configure(background='lightgrey')

        if self.current_selection == 'Purchases':
            self.caller = {'name': 'purchases',
                           'date_key': 'purchase_date',
                           'amo_key': 'amount'}
            enable([self.month_combo])
            self._inst = self.pur_inst

        elif self.current_selection == 'Income':
            self.caller = {'name': 'income',
                           'date_key': 'income_date',
                           'amo_key': 'amount'}
            enable([self.month_combo])
            self._inst = self.acc_inst.statistics.income

        elif self.current_selection == 'Debtors':
            self.caller = {'name': 'debtors',
                           'date_key': 'debt_date',
                           'amo_key': 'balance'}
            enable([self.month_combo])
            self._inst = self.acc_inst.assets.current.debtors

        elif self.current_selection == 'Expenses':
            self.caller = {'name': 'expenses',
                           'date_key': 'exp_date',
                           'amo_key': 'amount'}
            enable([self.month_combo])
            self._inst = self.acc_inst.expenses

        elif self.current_selection == 'Profits':
            self.caller = {'name': 'profits',
                           'date_key': 'profit_date',
                           'amo_key': 'amount'}
            disable([self.month_combo])
            self._inst = self.acc_inst.assets.current.profits
            self.graph_it(month='All')
            return True

        else:
            self.caller = {'name': 'sales',
                           'date_key': 'sale_date',
                           'amo_key': 'amount_paid'}
            enable([self.month_combo])
            self._inst = self.sales_inst

        _dt = datetime.now()

        self.graph_it(year=str(_dt.year).zfill(4),
                      month=str(_dt.month).zfill(2))
