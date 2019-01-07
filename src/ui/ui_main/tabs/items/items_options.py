
import tkinter as tk
from tkinter import ttk


class ItemsOptions:

    def __init__(self):
        self.btn_delete_item = ttk.Button(self.f_items_options,
                                          text='Delete Item')

        self.delete_wo()

    def delete_wo(self):
        sep01 = ttk.Separator(self.f_items_options, orient='vertical')
        sep01.grid(column=1, row=0, sticky='NS')
        self.btn_delete_item.grid(column=2, row=0, sticky='NES',
                                  padx=20, pady=5)

        def _delete_item():
            result = self.table.delete_row()

            for item in self.all_items_list:
                if item['name'] == result:
                    self.all_items_inst.delete_item_given_item(item=item)

        self.btn_delete_item.configure(command=_delete_item)
