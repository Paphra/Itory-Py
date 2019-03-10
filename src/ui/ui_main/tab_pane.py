
from tkinter import ttk

from data.accounts import Accounts
from data.items import Items
from data.purchases import Purchases
from data.sales import Sales
from data.management import Management
from ui.routine.f_make import focus
from .tabs.accounts.t_accounts import TAccounts
from .tabs.graphs.t_graphs import TGraphs
from .tabs.home.t_home import THome
from .tabs.items.t_items import TItems
from .tabs.management.t_management import TManagement
from .tabs.purchases.t_purchases import TPurchases
from .tabs.sales.t_sales import TSales


class NtBook:

    def __init__(self, s_bar, root):
        self.rt = root
        self.sb = s_bar

        self.ntb = ttk.Notebook(self.rt)
        self.items_inst = Items()
        self.sales_inst = Sales()
        self.purchases_inst = Purchases()
        self.acc_inst = Accounts()
        self.management = Management()
        self.insts = {'items': self.items_inst,
                      'sales': self.sales_inst,
                      'purchases': self.purchases_inst,
                      'accounts': self.acc_inst,
                      'management': self.management}

        # tabs
        self.t_home = THome(self.ntb, self.sb, self.insts)
        self.t_items = TItems(self.ntb, self.sb, self.insts)
        self.t_sales = TSales(self.ntb, self.sb, self.insts)
        self.t_purchases = TPurchases(self.ntb, self.sb, self.insts)
        self.t_accounts = TAccounts(self.ntb, self.sb, self.insts)
        self.t_graphs = TGraphs(self.ntb, self.sb, self.insts)
        self.tabs_inst = {
            'main': self.ntb,
            'home': self.t_home,
            'items': self.t_items,
            'sales': self.t_sales,
            'purchases': self.t_purchases,
            'accounts': self.t_accounts,
            'graphs': self.t_graphs
        }
        self.t_management = TManagement(self.ntb, self.sb, self.insts,
                                        self.tabs_inst)

        self.ntb_w()

    def ntb_w(self):
        self.ntb.grid(column=0, row=0, sticky='NESW')
        self.ntb.bind("<<NotebookTabChanged>>", self._tabchanged)

    def select_tab(self, index):
        self.ntb.select(index)

    def _tabchanged(self, event=None):
        sel_tb = self.ntb.tab('current')
        self.sb.lb_left['text'] = "Current Tab: " + sel_tb['text']

        _name = sel_tb['text']
        if _name == 'Home':
            self.t_home.i_c.set_items(self.items_inst.get_all())
            self.t_home.i_c.clear_all_items()

        elif _name == 'Items':
            self.t_items.i_main.all_items_works()

        elif _name == 'Sales':
            focus(self.t_sales.sales_main)

        elif _name == 'Purchases':
            focus(self.t_purchases.p_main)

        elif _name == 'Accounts':
            self.t_accounts.a_main.acc_ntb.select(0)
            self.t_accounts.a_main.t_assets.mf_ntb.select(0)
            focus(self.t_accounts.a_main.t_assets.t_debtors.debtors_main)

        elif _name == 'Graphs':
            self.t_graphs.g_main.selection()
            self.t_graphs.g_main.graph_it()
