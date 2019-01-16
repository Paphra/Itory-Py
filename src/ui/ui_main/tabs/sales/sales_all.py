from tkinter import ttk

from src.data.works.check import check_rows
from src.ui.structures.table import Table


class SalesAll:

    def __init__(self):
        self.f_sales = ttk.Frame(self.mf_sales)
        self.main_table = Table(self.f_sales)
        self._keys = ['sale_date',
                      'customer_name',
                      'customer_contact',
                      'amount_paid',
                      'balance',
                      'items']

        self.titles = [{'text': 'Date', 'width': 20, 'type': 'l'},
                       {'text': "Customer", 'width': 20, 'type': 'l'},
                       {'text': "Contact", 'width': 23, 'type': 'l'},
                       {'text': 'Paid', 'width': 15, 'type': 'l'},
                       {'text': 'Balance', 'width': 15, 'type': 'l'},
                       {'text': 'Items Sold', 'width': 25, 'type': 'c'}]

        self.main_table.create(titles=self.titles, height=370)

        self.sales_all_w()
        self.all_sales_fill()

    def sales_all_w(self):
        self.f_sales.grid(column=0, row=1, sticky='NEWS')

    def all_sales_fill(self):
        self.fill_sales(self.sales_list)

    def fill_sales(self, sales_list: list):
        self.main_table.add_rows(
                rows_list=check_rows(sales_list, self.titles, self._keys),
                _keys_=self._keys)
