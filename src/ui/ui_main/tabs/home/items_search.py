
import tkinter as tk
from tkinter import ttk


class ItemSearch:

    """Class that searches

        If you want to search    
    """

    def __init__(self, item_list_inst, container):
        self.hostl = container
        self.mlf = ttk.LabelFrame(self.hostl)
        self.sbox = ttk.Entry(self.mlf)
        self.item_list_inst = item_list_inst
        self.items = self.item_list_inst.get_list()

        self.si_w()

    def si_w(self):
        self.sbox.grid(column=0, row=0)
        self.sbox.configure(width=20)

        # events binding to the entry text
        self.sbox.bind('<Return>', self._search)
        self.sbox.bind('<KeyRelease>', self._search)

        self.mlf.configure(text="Search --- ")
        self.mlf.grid(column=0, row=0)

        self.sbox.focus()

    def _search(self, event=None):
        stxt = self.sbox.get()
        if len(stxt) == 0:
            self.item_list_inst.set_items(self.items)
        else:
            its = []
            for it in self.items:
                item = it['name']
                if stxt.lower() in item.lower():
                    its.append(it)
            self.item_list_inst.set_items(its)
