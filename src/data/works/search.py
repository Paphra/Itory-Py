
import tkinter as tk
from tkinter import ttk


class Search:

    def __init__(self, master: any, work_function, _list: list, _use: list,
                 width: int = None, sticky: str = None):
        self.v_search = tk.StringVar()
        self.e_search = ttk.Entry(master)
        self.work_function = work_function
        self._list = _list
        self._use = _use
        self._width = width
        if self._width is None:
            self._width = 25
        self._sticky = sticky
        if self._sticky is None:
            self._sticky = 'WENS'

        self.search_works()

    def search_works(self):

        self.e_search.grid(column=0, row=0, sticky=self._sticky, padx=10, pady=5)
        self.e_search.configure(width=self._width,
                                textvariable=self.v_search)
        self.e_search.bind("<KeyRelease>", self._search_list)
        self.e_search.focus()

    def _search_list(self, event=None):
        txt = self.v_search.get()
        _list_ = []
        if len(txt) > 0:
            for line in self._list:
                _c = False
                for _u in self._use:
                    if txt.lower() in str(line[_u]).lower():
                        _c = True
                if _c:
                    _list_.append(line)
        else:
            _list_ = self._list

        self.work_function(_list_)
