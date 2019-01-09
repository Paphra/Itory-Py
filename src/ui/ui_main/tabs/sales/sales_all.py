from tkinter import ttk

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
        self.titles = [{'text': 'Date', 'width': 15},
                       {'text': "Customer's Name", 'width': 15},
                       {'text': "Contact", 'width': 15},
                       {'text': 'Paid', 'width': 9},
                       {'text': 'Balance', 'width': 9},
                       {'text': 'Items Sold', 'width': 17}]

        self.main_table.create(titles=self.titles, height=350)

        self.sales_all_w()

    def sales_all_w(self):
        self.f_sales.grid(column=0, row=1, sticky='NEWS')

    def all_sales_fill(self):
        self.fill_sales(self.all_sales_list)

    def fill_sales(self, sales_list: list):
        self.main_table.add_rows(rows_list=sales_list, _keys_=self._keys)
