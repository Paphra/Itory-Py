
from tkinter import ttk
import tkinter as tk
from .items_checkout import ItemCheckout


class THome:

    def __init__(self, nt_book, s_bar, items_inst, sales_inst):
        self.ntb = nt_book
        self.sb = s_bar

        self.t_home = ttk.Frame(self.ntb)
        self.lf_ht = ttk.LabelFrame(self.t_home)
        self.i_c = ItemCheckout(self.lf_ht, items_inst, sales_inst, self.sb)

        self.thome_w()

    def thome_w(self):
        self.ntb.add(self.t_home, text='Home')

        self.lf_ht.grid(column=0, row=0, padx=10, pady=10, sticky='NESW')
        self.lf_ht.configure(width=780, height=500, text='Home: Select Items and Checkout.')
