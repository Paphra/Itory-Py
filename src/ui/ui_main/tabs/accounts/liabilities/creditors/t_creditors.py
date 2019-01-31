from tkinter import ttk

from src.ui.ui_main.tabs.commons.main import Main


class TCreditors:

    def __init__(self, nt_book, s_bar, insts):
        self.ntb = nt_book
        self.sb = s_bar
        self.cred_inst = insts['accounts'].liabilities.creditors
        self.t_creditors = ttk.Frame(self.ntb)
        self.mf_creditors = ttk.Frame(self.t_creditors)
        self.creditors_main = Main(self.mf_creditors, self.sb, self.cred_inst,
                                   'Creditors')

        self.t_work()

    def t_work(self):
        self.ntb.add(self.t_creditors, text='Creditors')
        self.mf_creditors.grid(column=0, row=0, padx=10, pady=10, sticky='NESW')
        self.mf_creditors.configure(width=750, height=500)
