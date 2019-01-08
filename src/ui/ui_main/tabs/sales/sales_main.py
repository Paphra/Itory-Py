
import tkinter as tk
from tkinter import ttk
from .sales_all import SalesAll
from src.data.works.search import Search
from .sales_options import SalesOptions


class SalesMain(SalesAll, Search, SalesOptions):

    def __init__(self, container, sales_inst, s_bar):
        self.host = container
        self.sales_inst = sales_inst
        self.sb = s_bar

        self.all_sales_list = self.sales_inst.get_all_sales()
        self.mf_sales = ttk.LabelFrame(master=self.host, text="Sales")
        self.f_search = ttk.LabelFrame(self.mf_sales, text='Search ...')

        self.works()

        SalesAll.__init__(self)
        self._use = ['date', 'cus_name', 'cus_cont']
        Search.__init__(self, self.f_search, self.fill_sales,
                        self.all_sales_list, self._use,
                        width=50)
        SalesOptions.__init__(self)

    def works(self):
        self.main_frame_w()
        self.f_search_w()

    def main_frame_w(self):
        self.mf_sales.grid(column=0, row=0, sticky='WENS')
        self.mf_sales.configure(width=790, height=500)

    def f_search_w(self):
        self.f_search.grid(column=0, row=0, sticky='WE')
