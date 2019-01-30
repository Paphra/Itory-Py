
from tkinter import ttk
from .income_statement.t_income_statement import TIncomeStatement
from .income.t_income import TIncome
from .balance_sheet.t_balance_sheet import TBalanceSheet
from src.ui.routine.f_make import focus


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
        self.mf_ntb.bind("<<NotebookTabChanged>>", self._tabchanged)

    def select_tab(self, index):
        self.mf_ntb.select(index)

    def _tabchanged(self, event=None):

        sel_tb = self.mf_ntb.tab('current')
        self.sb.lb_left['text'] = "Current Tab: " + sel_tb['text']
        s_tb_name = sel_tb['text']

        if s_tb_name == 'Income':
            focus(self.t_income.income_main)

