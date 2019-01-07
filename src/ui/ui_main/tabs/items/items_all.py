
import tkinter as tk
from tkinter import ttk
from ui.structures.table import Table


class ItemsAll:

    def __init__(self):
        self._padx = 4
        self._pady = 2
        self.table = Table(master=self.f_items_list)

        self.row_keys = ['name', 'type', 'qty', 'sell_unit']

        self.titles_works()
        self.all_items_works()

    def titles_works(self):
        self.titles_list = [{'text': 'Item Name', 'width': 19},
                            {'text': 'Item Type', 'width': 15},
                            {'text': 'Quantity', 'width': 8},
                            {'text': 'Unit Price', 'width': 9}]
        self.dimensions = {'width': 500, 'height': 360, 'x': 250, 'y': 25}
        self.table.create(self.titles_list, self.dimensions)

    def all_items_works(self):
        self.table.add_rows(rows_list=self.all_items_list,
                            _keys_=self.row_keys)

    def fill_list(self, items_list):
        self.table.add_rows(rows_list=items_list,
                            _keys_=self.row_keys)
