from tkinter import ttk
from .acc_main import AccMain


class TAccounts:

    def __init__(self, nt_book, s_bar, insts):
        self.ntb = nt_book
        self.sb = s_bar
        self.t_accounts = ttk.Frame(self.ntb)
        self.f_t = ttk.Frame(self.t_accounts)
        self.a_main = AccMain(self.t_accounts, self.sb, insts)
        self.t_work()

    def t_work(self):
        self.ntb.add(self.t_accounts, text='Accounts')
        self.f_t.grid(column=0, row=0, padx=10, pady=10, sticky='NESW')
        self.f_t.configure(width=825, height=525)
