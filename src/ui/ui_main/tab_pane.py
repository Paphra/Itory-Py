
from tkinter import ttk

from src.data.items import Items
from src.data.purchases import Purchases
from src.data.sales import Sales
from src.data.accounts import Accounts
from .tabs.accounts.t_accounts import TAccounts
from .tabs.graphs.t_graphs import TGraphs
from .tabs.home.t_home import THome
from .tabs.items.t_items import TItems
from .tabs.management.t_management import TManagement
from .tabs.purchases.t_purchases import TPurchases
from .tabs.sales.t_sales import TSales
from threading import Thread


class NtBook:

    def __init__(self, s_bar, root):
        self.rt = root
        self.sb = s_bar

        self.ntb = ttk.Notebook(self.rt)
        self.items_inst = Items()
        self.sales_inst = Sales()
        self.purchases_inst = Purchases()
        self.acc_inst = Accounts()
        self.insts = {'items': self.items_inst,
                      'sales': self.sales_inst,
                      'purchases': self.purchases_inst,
                      'accounts': self.acc_inst}

        # tabs
        self.t_home = THome(self.ntb, self.sb, self.insts)
        self.t_items = TItems(self.ntb, self.sb, self.insts)
        self.t_sales = TSales(self.ntb, self.sb, self.insts)
        self.t_purchases = TPurchases(self.ntb, self.sb, self.insts)
        self.t_accounts = TAccounts(self.ntb, self.sb, self.insts)
        self.t_graphs = TGraphs(self.ntb, self.sb, self.insts)
        self.t_management = TManagement(self.ntb, self.sb, self.insts)

        self.ntb_w()

    def ntb_w(self):
        self.ntb.grid(column=0, row=0, sticky='NESW')
        self.ntb.bind("<<NotebookTabChanged>>", self._tabchanged)

    def select_tab(self, index):
        self.ntb.select(index)

    def _tabchanged(self, event=None):
        sel_tb = self.ntb.tab('current')
        self.sb.lb_left['text'] = "Current Tab: " + sel_tb['text']

        s_tb_name = sel_tb['text']
        if s_tb_name == 'Home':
            self.t_home.i_c.set_items(self.t_items.i_main.all_items_list)
            self.t_home.i_c.clear_all_items()

        elif s_tb_name == 'Items':
            Thread(target=self.t_items.i_main.all_items_works()).start()

        elif s_tb_name == 'Sales':
            self.t_sales.sales_main.work_on_years_and_months()
            self.t_sales.sales_main.set_years_months_days()
            self.t_sales.sales_main.work_on_period()
            self.t_sales.sales_main.all_fill()

        elif s_tb_name == 'Purchases':
            self.t_purchases.p_main.work_on_years_and_months()
            self.t_purchases.p_main.set_years_months_days()
            self.t_purchases.p_main.work_on_period()
            self.t_purchases.p_main.all_fill()
