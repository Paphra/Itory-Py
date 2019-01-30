from tkinter import ttk
import tkinter as tk
from datetime import datetime
from src.ui.routine.entry_validate import Validate
from src.ui.routine.widget_works import *


class GeneralBottom:

    def __init__(self):
        self.general_work()

    def general_work(self):
        self.btn_add.grid(column=9, row=1, sticky='S',
                          padx=1, ipadx=1)

        self.lf_add_row.grid(column=1, row=3, sticky='NES',
                             padx=5, pady=1, columnspan=10)
        self.lf_edit_amo = ttk.Labelframe(self.lf_add_row,
                                          text='Amount')
        if self.caller == 'Expenses':
            name = 'Person Responsible'
        else:    # income
            name = 'From'

        self.lf_edit_name = ttk.Labelframe(self.lf_add_row,
                                           text=name)
        self.lf_add_details = ttk.Labelframe(self.lf_add_row,
                                             text='Details')

        self.btn_save = ttk.Button(self.lf_add_row, text='Save')
        self.btn_cancel = ttk.Button(self.lf_add_row, text='Cancel')

        self.lf_edit_name.grid(column=0, row=0, padx=2)
        self.lf_add_details.grid(column=1, row=0, padx=2)
        self.lf_edit_amo.grid(column=2, row=0, padx=2)

        self.btn_save.grid(column=4, row=0, sticky='S',
                           padx=2, ipadx=2)
        self.btn_cancel.grid(column=5, row=0, sticky='S',
                             padx=2, ipadx=2)

        self.e_edit_amo = ttk.Entry(self.lf_edit_amo, textvariable=self.v_edit_amo)
        self.e_edit_name = ttk.Entry(self.lf_edit_name, textvariable=self.v_edit_name)
        self.e_add_details = ttk.Entry(self.lf_add_details, textvariable=self.v_add_details)

        self.e_edit_amo.grid(column=0, row=0)
        self.e_edit_name.grid(column=0, row=0)
        self.e_edit_name.configure(width=25)
        self.e_add_details.grid(column=0, row=0)
        self.e_add_details.configure(width=40)
        disable([self.e_edit_name, self.e_add_details, self.ed_year,
                 self.e_edit_amo, self.btn_save, self.btn_cancel,
                 self.cb_month, self.ed_day])

        self.btn_add.configure(command=self._add)

    def _add(self):
        enable([self.e_edit_amo, self.e_edit_name, self.e_add_details,
                self.cb_month, self.ed_day, self.ed_year])
        val_amo = Validate(var_=self.v_edit_amo, entry_=self.e_edit_amo)
        val_amo.int_(min_=0, min_len_=1)

        def _cancel(event=None):
            clear([self.v_edit_amo, self.v_edit_name, self.v_add_details])
            disable([self.e_edit_amo, self.e_edit_name, self.e_add_details,
                     self.btn_save, self.btn_cancel,
                     self.cb_month, self.ed_day, self.ed_year])

        def _save(event=None):
            _dt = datetime.now()
            dt_str = self.ed_year.get() + '-' + self.vd_month.get() + \
                '-' + self.ed_day.get() + '|' + str(_dt.hour).zfill(2) + \
                ':' + str(_dt.minute).zfill(2) + ':' + str(_dt.second).zfill(2)
            amo = int(self.v_edit_amo.get())
            name = self.v_edit_name.get()
            det = self.v_add_details.get()
            if self.caller == 'Expenses':
                row = {'exp_date': dt_str,
                       'responsible': name,
                       'details': det,
                       'amount': amo}
            else:    # income
                row = {'income_date': dt_str,
                       'from': name,
                       'details': det,
                       'amount': amo}

            self._inst.work.add(row)
            self.work_on_years_and_months()
            self.set_years_months_days()
            self.work_on_period()
            self.all_fill()
            _cancel()

        self.btn_save.configure(command=_save, state='enabled')
        self.btn_cancel.configure(command=_cancel, state='enabled')
