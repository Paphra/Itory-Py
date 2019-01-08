
import tkinter as tk
from tkinter import ttk
from src.ui.structures.table import Table


class SalesAll:

    def __init__(self):
        self.f_sales = ttk.Frame(self.mf_sales)
        self.main_table = Table(self.f_sales)
        self.main_table.create()
        self.main_table.add_rows()

        self.sales_all_w()

    def sales_all_w(self):
        self.f_sales.grid(column=0, row=1, sticky='NEWS')

    def fill_sales(self, sales_list):
        pass
