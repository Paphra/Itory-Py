from tkinter import ttk

from ui.ui_main.tabs.commons.main import Main


class TSalesRet:

    def __init__(self, nt_book, s_bar, insts):
        self.ntb = nt_book
        self.sb = s_bar
        self.sales_ret_inst = insts['accounts'].returns.sales
        self.t_sales = ttk.Frame(self.ntb)
        self.mf_sales = ttk.Frame(self.t_sales)
        self.sales_main = Main(self.mf_sales, self.sb,
                               self.sales_ret_inst,
                               'Sales Returns')

        self.t_work()

    def t_work(self):
        self.ntb.add(self.t_sales, text='Sales Returns')
        self.mf_sales.grid(column=0, row=0, padx=10, pady=10, sticky='NESW')
        self.mf_sales.configure(width=750, height=500)
