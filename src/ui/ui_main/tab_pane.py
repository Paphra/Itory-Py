
from tkinter import ttk
from .tabs.home.t_home import THome
from .tabs.items.t_items import TItems
from .tabs.sales.t_sales import TSales
from .tabs.purchases.t_purchases import TPurchases
from .tabs.accounts.t_accounts import TAccounts
from .tabs.graphs.t_graphs import TGraphs
from .tabs.management.t_management import TManagement
from data.items import Items
from data.sales import Sales


class NtBook:

    def __init__(self, s_bar, root):
        self.rt = root
        self.sb = s_bar
        
        self.ntb = ttk.Notebook(self.rt)
        self.items_inst = Items()
        self.sales_inst = Sales()

        # tabs
        self.t_home = THome(self.ntb, self.sb, self.items_inst, self.sales_inst)
        self.t_items = TItems(self.ntb, self.sb, self.items_inst)
        self.t_sales = TSales(self.ntb, self.sb, self.sales_inst)
        self.t_purchases = TPurchases(self.ntb, self.sb)
        self.t_accounts = TAccounts(self.ntb, self.sb)
        self.t_graphs = TGraphs(self.ntb, self.sb)
        self.t_management = TManagement(self.ntb, self.sb)

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
            self.t_items.i_main.all_items_works()
