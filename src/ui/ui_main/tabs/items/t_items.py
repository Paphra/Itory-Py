from tkinter import ttk

from .items_main import ItemsMain


class TItems:

    def __init__(self, nt_book, s_bar, insts):
        self.ntb = nt_book
        self.sb = s_bar

        self.t_items = ttk.Frame(self.ntb)
        self.frame_items = ttk.Frame(self.t_items)
        self.i_main = ItemsMain(self.frame_items, self.sb, insts)

        self.t_items_w()

    def t_items_w(self):
        self.ntb.add(self.t_items, text='Items')
        self.frame_items.grid(column=0, row=0, padx=10, pady=10,
                              sticky='NESW')
        self.frame_items.configure(width=780, height=50)
