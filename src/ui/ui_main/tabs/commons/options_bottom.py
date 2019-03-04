import tkinter as tk
from tkinter import ttk

from ui.structures.date import Date
from ui.ui_main.tabs.accounts.assets.debtors.debtors_work import DebtorsWork
from .options_bottom_general import GeneralBottom


class OptionsBottom(Date, DebtorsWork, GeneralBottom):
    def __init__(self):

        self.label = self.caller
        if self.label[-1] == 's':
            self.label = self.label[:-1]

        self.lf_total = ttk.LabelFrame(self.bottom_row,
                                       text='Total ' + self.caller)
        self.lf_edit_row = ttk.Labelframe(self.bottom_row,
                                          text='Edit ' + self.label)
        self.lf_add_row = ttk.Labelframe(self.bottom_row,
                                         text='Add ' + self.label)
        self.date_host = ttk.Labelframe(self.bottom_row,
                                        text="Add " + self.label + "'s Date")

        Date.__init__(self)

        self.btn_save = None
        self.btn_cancel = None
        self.btn_add = None
        self.e_edit_amo = None
        self.e_edit_name = None
        self.e_edit_tel = None
        self.e_edit_email = None
        self.e_add_details = None
        self.v_add_details = tk.StringVar()
        self.v_edit_amo = tk.StringVar()
        self.v_edit_name = tk.StringVar()
        self.v_edit_tel = tk.StringVar()
        self.v_edit_email = tk.StringVar()
        self.lf_edit_amo = None
        self.lf_edit_name = None
        self.lf_edit_tel = None
        self.lf_edit_email = None
        self.lf_add_details = None

        self.v_total = tk.StringVar()
        self.e_total_ = ttk.Entry(self.lf_total, textvariable=self.v_total)
        if self.caller == 'Sales':
            self.lf_bal = ttk.LabelFrame(self.bottom_row,
                                         text='Total Balance')
            self.v_bal = tk.StringVar()
            self.e_total_bal = ttk.Entry(self.lf_bal,
                                         textvariable=self.v_bal)
        if self.caller in ['Debtors']:
            self.btn_edit = ttk.Button(self.bottom_row,
                                       text='Edit ' + self.label)
        if self.caller in self.list_of_commons:
            self.btn_add = ttk.Button(self.bottom_row,
                                      text='Add ' + self.label)
        self.btn_delete = ttk.Button(self.bottom_row,
                                     text='Delete ' + self.label)
        self._total_wo()
        self._delete_wo()

        if self.caller in ['Debtors']:
            DebtorsWork.__init__(self)

        elif self.caller in self.list_of_commons:
            GeneralBottom.__init__(self)

    def _works_btm(self):
        for _i in [0, 2]:
            sep_h = ttk.Separator(self.bottom_row, orient='horizontal')
            sep_h.grid(column=0, row=_i, sticky='WE', columnspan=10)

    def _total_wo(self):
        self.lf_total.grid(column=7, row=1, sticky='S', padx=5, pady=2)
        self.e_total_.grid(column=0, row=0, sticky='S', padx=5, pady=2)
        self.e_total_.configure(state='readonly')

        if self.caller == 'Sales':
            self.lf_bal.grid(column=8, row=1, sticky='S', padx=5, pady=2)
            self.e_total_bal.grid(column=0, row=0, sticky='S', padx=5, pady=2)
            self.e_total_bal.configure(state='readonly')

        if self.caller in self.list_of_commons:
            self.date_host.grid(column=5, row=1, sticky='NES', padx=10)

    def _delete_wo(self):
        self.btn_delete.grid(column=10, row=1, padx=10, ipadx=5,
                             sticky='S')
        self.btn_delete.configure(command=self._delete)

    def _delete(self):
        row = self.main_table.delete_row()
        if row is not None:
            self.calculate_totals()

            _new_c = ['Debtors']
            _new_c.extend(self.list_of_commons)

            if self.caller == 'Sales':
                self._inst.delete(row)
            elif self.caller in _new_c:
                self._inst.work.delete(row, self._date_key)
        del row
