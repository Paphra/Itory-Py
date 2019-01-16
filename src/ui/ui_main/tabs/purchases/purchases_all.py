from tkinter import ttk

from src.data.works.check import check_rows
from src.ui.structures.table import Table


class PurchasesAll:

    def __init__(self):
        self.f_purchases = ttk.Frame(self.mf_purchases)
        self.main_table = Table(self.f_purchases)
        self._keys = ['purchase_date',
                      'item',
                      'details',
                      'amount']

        self.titles = [{'text': 'Date', 'width': 20, 'type': 'l'},
                       {'text': "Item", 'width': 35, 'type': 'l'},
                       {'text': "Details", 'width': 40, 'type': 'l'},
                       {'text': 'Amount', 'width': 25, 'type': 'l'}]

        self.main_table.create(titles=self.titles, height=370)

        self.purchases_all_w()
        self.all_purchases_fill()

    def purchases_all_w(self):
        self.f_purchases.grid(column=0, row=1, sticky='NEWS')

    def all_purchases_fill(self):
        self.fill_purchases(self.purchases_list)

    def fill_purchases(self, purchases_list: list):
        self.main_table.add_rows(
                rows_list=check_rows(purchases_list, self.titles, self._keys),
                _keys_=self._keys)
