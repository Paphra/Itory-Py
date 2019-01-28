import tkinter as tk
from tkinter import ttk
from src.data.works import validate


def enable(widgets):
    for widget in widgets:
        widget.configure(state='enabled')


def disable(widgets):
    for widget in widgets:
        widget.configure(state='disabled')


def clear(variables):
    for variable in variables:
        variable.set('')


class OptionsBottom:
    def __init__(self):

        self.lf_total = ttk.LabelFrame(self.bottom_row,
                                       text='Total ' + self.caller)
        self.lf_edit_row = ttk.Labelframe(self.bottom_row,
                                          text='Edit ' + self.caller[:-1])
        self.btn_save = None
        self.btn_cancel = None
        self.e_edit = None
        self.v_edit = tk.StringVar()
        self.lf_edit_p = None

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
                                       text='Edit' + self.caller[:-1])
        self.btn_delete = ttk.Button(self.bottom_row,
                                     text='Delete ' + self.caller[:-1])
        self._total_wo()
        self._edit_wo()
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
        self.e_total_.grid(column=0, row=0, sticky='NES', padx=5, pady=2)
        self.e_total_.configure(state='readonly')

        if self.caller == 'Sales':
            self.lf_bal.grid(column=3, row=1, sticky='NES', padx=10)
            self.e_total_bal.grid(column=0, row=0, sticky='NES', padx=5, pady=2)
            self.e_total_bal.configure(state='readonly')

    def _delete_wo(self):
        self.btn_delete.grid(column=5, row=1, sticky='NS',
                             padx=10, pady=2)

        def _delete():
            result = self.main_table.delete_row()
            if result is not None:
                self.calculate_totals()

                for row in self._inst.get_all():
                    if row[self._date_key] == result:
                        if self.caller == 'Purchases':
                            self._inst.delete_purchase(row)
                        elif self.caller == 'Sales':
                            self._inst.delete_sale(row)

        self.btn_delete.configure(command=_delete)

    def _edit_wo(self):
        if self.caller in ['Debtors']:
            self.btn_edit.grid(column=3, row=1, sticky='NS',
                               padx=10, pady=2)
            self.lf_edit_row.grid(column=1, row=3, sticky='NES',
                                  padx=10, pady=5, columnspan=5)
            self.lf_edit_p = ttk.Labelframe(self.lf_edit_row,
                                            text='Amount Paid')
            self.btn_save = ttk.Button(self.lf_edit_row, text='Save')
            self.btn_cancel = ttk.Button(self.lf_edit_row, text='Cancel')
            self.lf_edit_p.grid(column=0, row=0, padx=20)
            self.btn_save.grid(column=1, row=0, sticky='NS',
                               padx=10, pady=2)
            self.btn_cancel.grid(column=2, row=0, sticky='NS',
                                 padx=10, pady=2)
            self.e_edit = ttk.Entry(self.lf_edit_p, textvariable=self.v_edit)
            self.e_edit.grid(column=0, row=0)
            disable([self.e_edit, self.btn_save, self.btn_cancel])

            self.btn_edit.configure(command=self._edit)

    def _edit(self, event=None):
        result = self.main_table.get_selected()
        if result is not None:
            for row in self._inst.get_all():
                if row[self._date_key] == result:
                    if self.caller == 'Debtors':
                        self.e_edit.configure(state='enabled')

                        amo_p = row['paid']
                        tt_amo = int(row['balance']) + int(amo_p)
                        validate.int_(self.e_edit, self.v_edit)
                        self.v_edit.set(str(amo_p))

                        def _cancel(event=None):
                            clear([self.v_edit])
                            disable([self.e_edit, self.btn_save, self.btn_cancel])

                        def _save(event=None):
                            new_p = self.v_edit.get()
                            new_b = tt_amo - int(new_p)
                            self._inst.work.edit(row, 'paid', new_p)
                            self._inst.work.edit(row, 'balance', new_b)
                            self.all_fill()
                            _cancel()

                        self.btn_save.configure(command=_save, state='enabled')
                        self.btn_cancel.configure(command=_cancel, state='enabled')
