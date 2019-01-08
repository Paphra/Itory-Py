from tkinter import ttk
from .items_add import ItemsAdd
from .items_all import ItemsAll
from data.works.search import Search
from .items_options import ItemsOptions


class ItemsMain(ItemsAll, ItemsAdd, Search, ItemsOptions):

    def __init__(self, container, all_items_inst, s_bar):
        self.host = container
        self.sb = s_bar
        self.all_items_inst = all_items_inst
        self.all_items_list = all_items_inst.get_all_items()

        self.mf_items_add = ttk.LabelFrame(self.host)
        self.mf_all_items = ttk.LabelFrame(self.host)
        self.f_items_list = ttk.Frame(self.mf_all_items)
        self.f_items_search = ttk.LabelFrame(self.mf_all_items)
        self.f_items_options = ttk.Frame(self.host)

        self.add_w()
        self.all_w()
        self.list_w()
        self.search_w()
        self.options_w()

        ItemsAll.__init__(self)
        ItemsAdd.__init__(self)
        self._use = ['name', 'type']
        Search.__init__(self, self.f_items_search, self.fill_list,
                        self.all_items_list, self._use, sticky='ENS')
        ItemsOptions.__init__(self)

    def add_w(self):
        self.mf_items_add.grid(column=0, row=0, sticky='WE')
        self.mf_items_add.configure(width=250, height=450, text='Add New Item')

    def all_w(self):
        self.mf_all_items.grid(column=1, row=0, sticky='WENS', padx=3)
        self.mf_all_items.configure(width=20, height=10,
                                    text='All Items In Store')

    def search_w(self):
        self.f_items_search.grid(column=1, row=1, sticky='NES')
        self.f_items_search.configure(height=50, width=40, text='Search ...')

    def list_w(self):
        self.f_items_list.grid(column=0, row=2, sticky='WE', columnspan=2)
        self.f_items_list.configure(width=20, height=10)

    def options_w(self):
        self.f_items_options.grid(column=0, row=1, sticky='NES', columnspan=2)
        self.f_items_options.configure()
