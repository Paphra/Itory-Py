from tkinter import ttk

from data.works.search import Search
from ui.structures.lists import ScrollListBox

from src.ui.structures.date import Date
from .checkout import Checkout
from .item_details import ItemDetails
from .items_list import ItemList


class ItemCheckout(ItemList, ItemDetails, Date, Checkout, Search):

    def __init__(self, container, s_bar, insts):
        self.host = container
        self.sb = s_bar
        self.items_inst = insts['items']
        self.sales_inst = insts['sales']
        self.acc_inst = insts['accounts']
        self.debt_inst = self.acc_inst.assets.current.debtors
        self.inc_inst = self.acc_inst.statistics.income
        self.all_items_list = self.items_inst.get_all()

        self.mf_item_checkout = ttk.LabelFrame(self.host)
        self.mf_all_items_list = ttk.Frame(self.host)
        self.f_items_search = ttk.LabelFrame(self.mf_all_items_list,
                                             text='Search')

        self.sl_f = ttk.Frame(self.mf_item_checkout)
        self.scroll_list_box = ScrollListBox(self.sl_f)
        self.selected_items_listbox = self.scroll_list_box.get()

        self.dls_host = ttk.LabelFrame(self.mf_item_checkout)
        self.date_host = ttk.LabelFrame(self.dls_host)
        self.cus_host = ttk.LabelFrame(self.mf_item_checkout)

        self.ic_w()
        self.si_w()
        self.dls_w()
        self._date_w()
        self.cus_w()
        self.all_items_w()

        Date.__init__(self)
        Checkout.__init__(self)
        ItemDetails.__init__(self)
        ItemList.__init__(self)
        self._use = ['name', 'type']
        Search.__init__(self, self.f_items_search, self.set_items,
                        self.all_items_list, self._use)

    def all_items_w(self):
        self.mf_all_items_list.grid(column=0, row=0, sticky='NS')
        self.f_items_search.grid(column=0, row=0)

    def ic_w(self):
        self.mf_item_checkout.grid(column=1, row=0, rowspan=2, sticky='NESW')
        self.mf_item_checkout.configure(width=570, height=40, text='Selected Items Checkout.')

    def si_w(self):
        self.sl_f.grid(column=0, row=0, padx=5, pady=5, sticky='NS')
        self.sl_f.configure(height=130, width=250)

    def dls_w(self):
        self.dls_host.grid(column=1, row=0, padx=5, pady=5, sticky='EW')
        self.dls_host.configure(height=220, width=250, text='Item Details')

    def _date_w(self):
        self.date_host.grid(column=0, row=5, columnspan=3, sticky='NES', pady=10)
        self.date_host.configure(width=550, text="Date")

    def cus_w(self):
        self.cus_host.grid(column=0, row=2, columnspan=2, sticky='NESW', pady=5)
        self.cus_host.configure(width=550, text="Customer's Information.")
