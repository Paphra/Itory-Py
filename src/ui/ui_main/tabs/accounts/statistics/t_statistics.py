
from tkinter import ttk
from .income_statement.t_income_statement import TIncomeStatement
from .income.t_income import TIncome
from .balance_sheet.t_balance_sheet import TBalanceSheet


class TStatistics:

    def __init__(self, container, s_bar, insts):

        self.host = container
        self.sb = s_bar

        self.t_stats = ttk.Frame(self.host)
        self.mf_ntb = ttk.Notebook(self.t_stats)

        # tabs
        self.t_income = TIncome(self.mf_ntb, self.sb, insts)
        self.t_bal_sheet = TBalanceSheet(self.mf_ntb, self.sb, insts)
        self.t_income_stmt = TIncomeStatement(self.mf_ntb, self.sb, insts)

        self._works()

    def _works(self):
        self.host.add(self.t_stats, text='Statistics')
        self.mf_ntb.grid(column=0, row=0, sticky='NESW',
                         padx=5, pady=5)
