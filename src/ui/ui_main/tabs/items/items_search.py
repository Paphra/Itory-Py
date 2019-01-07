
import tkinter as tk
from tkinter import ttk


class ItemsSearch:

    def __init__(self):
        self.v_search = tk.StringVar()
        self.e_search = ttk.Entry(self.f_items_search)

        self.search_works()

    def search_works(self):

        self.e_search.grid(column=0, row=0, sticky='ENS', padx=10, pady=5)
        self.e_search.configure(width=25,
                                textvariable=self.v_search)
        self.e_search.bind("<KeyRelease>", self._search_items_list)

    def _search_items_list(self, event=None):
        txt = self.v_search.get()
        if len(txt) > 0:
            items_list = []
            for item in self.all_items_list:
                if txt.lower() in item['name'].lower() \
                        or txt.lower() in item['type'].lower():
                    items_list.append(item)

            self.fill_list(items_list)

        else:
            self.all_items_works()

