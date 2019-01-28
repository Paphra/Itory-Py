from tkinter import ttk
from src.ui.ui_main.tabs.commons.main import Main


class TPurchases:

    def __init__(self, nt_book, s_bar, insts):

        self.ntb = nt_book
        self.sb = s_bar
        self.t_purchases = ttk.Frame(self.ntb)
        self.mf_purchases = ttk.Frame(self.t_purchases)
        self.p_main = Main(self.mf_purchases, self.sb, insts['purchases'],
                           'Purchases')

        self.t_work()

    def t_work(self):

        self.ntb.add(self.t_purchases, text='Purchases')
        self.mf_purchases.grid(column=0, row=0, padx=10, pady=10, sticky='NESW')
        self.mf_purchases.configure(width=750, height=500)
