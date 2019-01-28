from tkinter import ttk

from data.works.search import Search

from .items_add import ItemsAdd
from .items_all import ItemsAll
from .items_options import ItemsOptions
from threading import Thread


class ItemsMain(ItemsAll, ItemsAdd, Search, ItemsOptions):

    def __init__(self, container, s_bar, insts):
        self.host = container
        self.sb = s_bar
        self.purchases_inst = insts['purchases']
        self.items_inst = insts['items']
        self.all_items_list = self.items_inst.get_all()

        self.mf_items_add = ttk.LabelFrame(self.host)
        self.mf_all_items = ttk.LabelFrame(self.host)
        self.f_items_list = ttk.LabelFrame(self.host)
        self.f_items_search = ttk.LabelFrame(self.host)
        self.f_items_options = ttk.Frame(self.host)
        self.date_host = ttk.Frame(self.mf_items_add)

        self.add_w()
        self.list_w()
        self.search_w()
        self.options_w()

        ItemsAdd.__init__(self)
        ItemsOptions.__init__(self)
        ItemsAll.__init__(self)
        self._use = ['name', 'type']
        Search.__init__(self, self.f_items_search, self.fill_list,
                        self.all_items_list, self._use, sticky='ENS',
                        width=35)

    def add_w(self):
        self.mf_items_add.grid(column=0, row=0, sticky='WE', rowspan=3,
                               padx=15, pady=20)
        self.mf_items_add.configure(text='Add New Item')
        self.date_host.grid(column=0, row=0, columnspan=2, sticky='NES',
                            pady=5)

    def search_w(self):
        self.f_items_search.grid(column=1, row=0, sticky='NES', padx=5)
        self.f_items_search.configure(text='Search ...')

    def list_w(self):
        self.f_items_list.grid(column=1, row=1, sticky='WENS', padx=5)
        self.f_items_list.configure(text='All Items In Store')

    def options_w(self):
        self.f_items_options.grid(column=1, row=2, sticky='NES', columnspan=2,
                                  padx=5)
        self.f_items_options.configure()
