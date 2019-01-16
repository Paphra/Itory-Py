import tkinter as tk
from tkinter import ttk


class PurchasesOptionsBottom:

    def __init__(self):

        self.lf_total = ttk.LabelFrame(self.bottom_row,
                                       text='Total purchases')
        self.v_total = tk.StringVar()
        self.e_total_purchases = ttk.Entry(self.lf_total,
                                           textvariable=self.v_total)
        self.btn_delete = ttk.Button(self.bottom_row,
                                     text='Delete Purchase')
        # self._works_btm()
        self._total_wo()
        self._delete_wo()

    def _works_btm(self):
        _col = 0
        for _i in range(3):
            if _i > 0:
                _col = _col + 2
            sep_v = 'sep' + str(_i)
            sep_v = ttk.Separator(self.bottom_row, orient='vertical')
            sep_v.grid(column=_col, row=1, sticky='NS')

        for _i in [0, 2]:
            sep_h = 'sep' + str(_i)
            sep_h = ttk.Separator(self.bottom_row, orient='horizontal')
            sep_h.grid(column=0, row=_i, sticky='WE', columnspan=5)

    def _total_wo(self):
        self.lf_total.grid(column=1, row=1, sticky='NES', padx=10)
        self.e_total_purchases.grid(column=0, row=0, sticky='NES', padx=5, pady=2)
        self.e_total_purchases.configure(state='readonly')

    def _delete_wo(self):
        self.btn_delete.grid(column=5, row=1, sticky='NS',
                             padx=10, pady=2)

        def _delete_purchase():
            result = self.main_table.delete_row()
            if result is not None:
                self.calculate_totals()

                for purchase in self.purchases_inst.get_all_purchases():
                    if purchase['purchase_date'] == result:
                        self.purchases_inst.delete_purchase_given_purchase(purchase=purchase)

        self.btn_delete.configure(command=_delete_purchase)
