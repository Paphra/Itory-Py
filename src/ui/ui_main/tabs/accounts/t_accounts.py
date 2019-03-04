from tkinter import ttk

from ui.routine.f_make import focus
from .acc_main import AccMain


class TAccounts:

    def __init__(self, nt_book, s_bar, insts):
        self.ntb = nt_book
        self.sb = s_bar
        self.t_accounts = ttk.Frame(self.ntb)
        self.f_t = ttk.Frame(self.t_accounts)
        self.a_main = AccMain(self.t_accounts, self.sb, insts)
        self.t_work()

    def t_work(self):
        self.ntb.add(self.t_accounts, text='Accounts')
        self.f_t.grid(column=0, row=0, padx=10, pady=10, sticky='NESW')
        self.f_t.configure(width=825, height=525)

        self.a_main.acc_ntb.bind("<<NotebookTabChanged>>", self._tabchanged)

    def select_tab(self, index):
        self.a_main.acc_ntb.select(index)

    def _tabchanged(self, event=None):
        sel_tb = self.a_main.acc_ntb.tab('current')
        self.sb.lb_left['text'] = "Current Tab: " + sel_tb['text']
        _name = sel_tb['text']

        if _name == 'Assets':
            self.a_main.t_assets.mf_ntb.select(0)
            focus(self.a_main.t_assets.t_debtors.debtors_main)

        elif _name == 'Expenses':
            focus(self.a_main.t_expenses.expenses_main)

        elif _name == 'Drawings':
            focus(self.a_main.t_drawings.drawings_main)

        elif _name == 'Statistics':
            self.a_main.t_statistics.mf_ntb.select(0)
            focus(self.a_main.t_statistics.t_income.income_main)

        elif _name == 'Returns':
            self.a_main.t_returns.mf_ntb.select(0)
            focus(self.a_main.t_returns.t_sales_ret.sales_main)

        elif _name == 'Liabilities':
            self.a_main.t_liabilities.mf_ntb.select(0)
            focus(self.a_main.t_liabilities.t_accruals.accruals_main)
