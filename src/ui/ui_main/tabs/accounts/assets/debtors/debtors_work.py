from tkinter import ttk

from src.ui.routine.entry_validate import Validate
from src.ui.routine.f_make import *
from src.ui.routine.widget_works import *


class DebtorsWork:

    def __init__(self):

        self.debtors_work()

    def debtors_work(self):
        self.btn_edit.grid(column=9, row=1, padx=5, ipadx=5,
                           sticky='S')

        self.lf_edit_row.grid(column=1, row=3, sticky='NES',
                              padx=10, pady=5, columnspan=10)
        self.lf_edit_amo = ttk.Labelframe(self.lf_edit_row,
                                          text='Amount Paid')
        self.lf_edit_name = ttk.Labelframe(self.lf_edit_row,
                                           text='Customer')
        self.lf_edit_tel = ttk.Labelframe(self.lf_edit_row,
                                          text='Tel No.')
        self.lf_edit_email = ttk.Labelframe(self.lf_edit_row,
                                            text='Email')
        self.btn_save = ttk.Button(self.lf_edit_row, text='Save')
        self.btn_cancel = ttk.Button(self.lf_edit_row, text='Cancel')
        self.lf_edit_name.grid(column=0, row=0, padx=5)
        self.lf_edit_tel.grid(column=1, row=0, padx=5)
        self.lf_edit_email.grid(column=2, row=0, padx=5)
        self.lf_edit_amo.grid(column=3, row=0, padx=5)

        self.btn_save.grid(column=4, row=0, sticky='S',
                           padx=5, ipadx=5)
        self.btn_cancel.grid(column=5, row=0, sticky='S',
                             padx=5, ipadx=5)

        self.e_edit_amo = ttk.Entry(self.lf_edit_amo,
                                    textvariable=self.v_edit_amo)
        self.e_edit_name = ttk.Entry(self.lf_edit_name,
                                     textvariable=self.v_edit_name)
        self.e_edit_tel = ttk.Entry(self.lf_edit_tel,
                                    textvariable=self.v_edit_tel)
        self.e_edit_email = ttk.Entry(self.lf_edit_email,
                                      textvariable=self.v_edit_email)

        self.e_edit_amo.grid(column=0, row=0)
        self.e_edit_name.grid(column=0, row=0)
        self.e_edit_tel.grid(column=0, row=0)
        self.e_edit_email.grid(column=0, row=0)
        disable([self.e_edit_name, self.e_edit_tel, self.e_edit_email,
                 self.e_edit_amo, self.btn_save, self.btn_cancel])

        self.btn_edit.configure(command=self._edit)

    def _edit(self, event=None):
        row = self.main_table.get_selected()
        if row is not None:
            enable([self.e_edit_amo, self.e_edit_name,
                    self.e_edit_tel, self.e_edit_email])

            self.e_edit_name.focus()

            amo_p = row['paid']
            tt_amo = int(row['balance']) + int(amo_p)

            val_amo = Validate(var_=self.v_edit_amo, entry_=self.e_edit_amo)
            val_amo.int_(min_=0, min_len_=1)
            self.v_edit_amo.set(str(amo_p))
            self.v_edit_name.set(row['name'])
            self.v_edit_tel.set(row['tel'])
            self.v_edit_email.set(row['email'])

            def _cancel(event=None):
                clear([self.v_edit_amo, self.v_edit_name,
                       self.v_edit_tel, self.v_edit_email])
                disable([self.e_edit_amo, self.e_edit_name,
                         self.e_edit_tel, self.e_edit_email,
                         self.btn_save, self.btn_cancel])

            def _save(event=None):
                new_p = self.v_edit_amo.get()
                new_b = tt_amo - int(new_p)
                self._inst.work.edit(row, 'debt_date', 'paid', new_p)
                self._inst.work.edit(row, 'debt_date', 'balance', new_b)
                self._inst.work.edit(row, 'debt_date', 'name',
                                     self.v_edit_name.get())
                self._inst.work.edit(row, 'debt_date', 'tel',
                                     self.v_edit_tel.get())
                self._inst.work.edit(row, 'debt_date', 'email',
                                     self.v_edit_email.get())
                increment = int(new_p) - int(amo_p)
                if increment:
                    income = {'from': 'Debtors',
                              'details': row['name'],
                              'income_date': make_date(),
                              'amount': int(new_p) - int(amo_p)}
                    self.inc_inst.work.add(income)

                self.all_fill()
                _cancel()

            self.btn_save.configure(command=_save, state='enabled')
            self.btn_cancel.configure(command=_cancel,
                                      state='enabled')
