
import tkinter as tk
from tkinter import ttk


class Search:

    def __init__(self, work_function, _list: list, _use: list, container):
        self.v_search = tk.StringVar()
        self.e_search = ttk.Entry(container)
        self.work_function = work_function
        self._list = _list
        self._use = _use

        self.search_works()

    def search_works(self):

        self.e_search.grid(column=0, row=0, sticky='ENS', padx=10, pady=5)
        self.e_search.configure(width=25,
                                textvariable=self.v_search)
        self.e_search.bind("<KeyRelease>", self._search_list)
        self.e_search.focus()

    def _search_list(self, event=None):
        txt = self.v_search.get()
        list_ = []
        if len(txt) > 0:
            for line in self._list:
                if txt.lower() in line[self._use[0]].lower() \
                        or txt.lower() in line[self._use[1]].lower():
                    list_.append(line)
        else:
            list_ = self._list
        self.work_function(list_)
