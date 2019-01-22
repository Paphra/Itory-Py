
import tkinter as tk
from tkinter import ttk
from .income.t_income import TIncome
from .balance_sheet.t_balance_sheet import TBalanceSheet
from .creditors.t_creditors import TCreditors
from .debtors.t_debtors import TDebtors
from .expenses.t_expenses import TExpenses
from .income_statement.t_income_statement import TIncomeStatement


class AccMain:

    def __init__(self, container, s_bar, sales_inst, pur_inst, acc_inst):
        self.host = container
        self.sb = s_bar

        self.acc_ntb = ttk.Notebook(self.host)

        # tabs
        self.t_inc = TIncome(self.acc_ntb, self.sb, acc_inst)
        self.t_exp = TExpenses(self.acc_ntb, self.sb, acc_inst)
        self.t_debt = TDebtors(self.acc_ntb, self.sb, acc_inst)
        self.t_cred = TCreditors(self.acc_ntb, self.sb, acc_inst)

        self.t_bal_sheet = TBalanceSheet(self.acc_ntb, self.sb, sales_inst,
                                         pur_inst, acc_inst)
        self.t_inc_stmt = TIncomeStatement(self.acc_ntb, self.sb, sales_inst,
                                           pur_inst, acc_inst)

        self._works()

    def _works(self):
        self.acc_ntb.grid(column=0, row=0, sticky='NESW',
                          padx=5, pady=5)
