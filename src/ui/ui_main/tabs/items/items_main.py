from tkinter import ttk

from data.works.search import Search

from src.ui.structures.date import Date
from .items_add import ItemsAdd
from .items_all import ItemsAll
from .items_options import ItemsOptions


class ItemsMain(ItemsAll, Date, ItemsAdd, Search, ItemsOptions):

    def __init__(self, container, all_items_inst, purchases_inst, s_bar):
        self.host = container
        self.sb = s_bar
        self.purchases_inst = purchases_inst
        self.all_items_inst = all_items_inst
        self.all_items_list = all_items_inst.get_all_items()

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

        ItemsAll.__init__(self)
        Date.__init__(self, y_width=7, m_width=7, d_width=7, orient='horizontal')
        ItemsAdd.__init__(self)
        self._use = ['name', 'type']
        Search.__init__(self, self.f_items_search, self.fill_list,
                        self.all_items_list, self._use, sticky='ENS',
                        width=35)
        ItemsOptions.__init__(self)

    def add_w(self):
        self.mf_items_add.grid(column=0, row=0, sticky='WE', rowspan=3)
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
