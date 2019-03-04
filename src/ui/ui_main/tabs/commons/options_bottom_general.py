from datetime import datetime
from tkinter import messagebox as msg, ttk

from ui.routine.entry_validate import Validate
from ui.routine.widget_works import *


class GeneralBottom:

    def __init__(self):
        self.general_work()

    def general_work(self):
        self.btn_add.grid(column=9, row=1, sticky='S', padx=1, ipadx=1)
        self.lf_add_row.grid(column=1, row=3, sticky='NES',
                             padx=5, pady=1, columnspan=10)
        self.lf_edit_amo = ttk.Labelframe(self.lf_add_row, text='Amount')
        self.lf_edit_name = ttk.Labelframe(self.lf_add_row, text=self.name)
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

        self.e_edit_name.focus()

        def _cancel(event=None):
            clear([self.v_edit_amo, self.v_edit_name, self.v_add_details])
            disable([self.e_edit_amo, self.e_edit_name, self.e_add_details,
                     self.btn_save, self.btn_cancel,
                     self.cb_month, self.ed_day, self.ed_year])

        def _save(event=None):
            if msg.askquestion('Itory: Saving Confirmation',
                               'Confirm the Saving?') == u'yes':
                _dt = datetime.now()
                dt_str = self.ed_year.get().zfill(4) + '-' + \
                         self.vd_month.get().zfill(2) + \
                         '-' + self.ed_day.get().zfill(2) + '|' + \
                         str(_dt.hour).zfill(2) + \
                         ':' + str(_dt.minute).zfill(2) + ':' + \
                         str(_dt.second).zfill(2)
                amo = int(self.v_edit_amo.get())
                name = self.v_edit_name.get()
                det = self.v_add_details.get()

                _k, _name_k = 'exp_date', 'responsible'  # catering for expenses
                if self.caller == 'Drawings':
                    _k = 'draw_date'
                elif self.caller == 'Purchases':
                    details = det.split(',')
                    del det
                    det =[]
                    for _dtl in details:
                        det.append(_dtl.strip())
                    _k, _name_k = 'purchase_date', 'supplier'
                elif self.caller == 'Income':
                    details = det.split(',')
                    del det
                    det =[]
                    for _dtl in details:
                        det.append(_dtl.strip())
                    _k, _name_k = 'income_date', 'from'
                elif self.caller == 'Sales Returns':
                    _k, _name_k = 'retin_date', 'customer'
                elif self.caller == 'Purchases Returns':
                    _k, _name_k = 'retout_date', 'supplier'
                elif self.caller == 'Fixed Assets':
                    _k, _name_k = 'fixed_assets_date', 'name'
                elif self.caller == 'Creditors':
                    _k, _name_k = 'cred_date', 'creditor'
                elif self.caller == 'Accruals':
                    _k, _name_k = 'accr_date', 'accruer'

                row = {_k: dt_str, _name_k: name, 'details': det,
                       'amount': amo}

                self._inst.work.add(row)

            self.all_fill()
            _cancel()

        self.btn_save.configure(command=_save, state='enabled')
        self.btn_cancel.configure(command=_cancel, state='enabled')
