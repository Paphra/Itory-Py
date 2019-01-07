
import tkinter as tk
from tkinter import ttk
from .sales_all import SalesAll
from .sales_search import SalesSearch
from .sales_options import SalesOptions


class SalesMain(SalesAll, SalesSearch, SalesOptions):

    def __init__(self, container, sales_inst, s_bar):
        self.host = container
        self.sales_inst = sales_inst
        self.sb = s_bar

        self.all_sales_list = self.sales_inst.get_all_sales()

        SalesAll.__init__(self)
        SalesSearch.__init__(self)
        SalesOptions.__init__(self)
