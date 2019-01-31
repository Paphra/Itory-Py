from tkinter import ttk

from src.ui.ui_main.tabs.accounts.assets.t_assets import TAssets
from src.ui.ui_main.tabs.accounts.drawings.t_drawings import TDrawings
from src.ui.ui_main.tabs.accounts.liabilities.t_liabilities import TLiabilities
from src.ui.ui_main.tabs.accounts.returns.t_returns import TReturns
from src.ui.ui_main.tabs.accounts.statistics.t_statistics import TStatistics
from .expenses.t_expenses import TExpenses


class AccMain:

    def __init__(self, container, s_bar, insts):
        self.host = container
        self.sb = s_bar

        self.acc_ntb = ttk.Notebook(self.host)

        # tabs
        self.t_assets = TAssets(self.acc_ntb, self.sb, insts)
        self.t_expenses = TExpenses(self.acc_ntb, self.sb, insts)
        self.t_drawings = TDrawings(self.acc_ntb, self.sb, insts)
        self.t_liabilities = TLiabilities(self.acc_ntb, self.sb, insts)
        self.t_returns = TReturns(self.acc_ntb, self.sb, insts)
        self.t_statistics = TStatistics(self.acc_ntb, self.sb, insts)

        self._works()

    def _works(self):
        self.acc_ntb.grid(column=0, row=0, sticky='NESW',
                          padx=5, pady=5)
