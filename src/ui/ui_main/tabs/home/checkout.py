"""
Module containing class for checking out the selected items
in the store
"""
import tkinter as tk
from datetime import datetime
from tkinter import messagebox as msg, ttk

from ui.routine.entry_validate import Validate


def es_pw(es):
    for _i in es:
        _i.configure(width=25)


def entry_works(els, col, s):
    _ii = 0
    for _e in range(len(els)):
        if _e > 0:
            _ii = _ii + 2
        else:
            _ii = _ii + 1
        els[_e].grid(column=col, row=_ii, padx=10, pady=5, sticky=s)
        els[_e].configure(width=30)


def es_cw(es):
    entry_works(es, 0, 'w')


def label_works(els, col, s):
    _ii = 0
    for _i in range(len(els)):
        if _i > 0:
            _ii = _ii + 2
        els[_i].grid(column=col, row=_ii, padx=10, sticky=s)


def lbs_cw(lbs):
    label_works(lbs, 0, 'W')


class Checkout:

    def __init__(self):

        l_nm = ttk.Label(self.cus_host, text='Name')
        l_tel = ttk.Label(self.cus_host, text='Telephone No.')
        l_eml = ttk.Label(self.cus_host, text='Email Address')

        lbs_c = [l_nm, l_tel, l_eml]
        lbs_cw(lbs_c)

        self.v_nm = tk.StringVar()
        self.v_tel = tk.StringVar()
        self.v_eml = tk.StringVar()

        self.e_nm = ttk.Entry(self.cus_host, textvariable=self.v_nm)
        self.e_tel = ttk.Entry(self.cus_host, textvariable=self.v_tel)
        self.e_eml = ttk.Entry(self.cus_host, textvariable=self.v_eml)

        es_c = [self.e_nm, self.e_tel, self.e_eml]
        es_cw(es_c)

        sep = ttk.Separator(self.cus_host, orient='vertical')
        sep.grid(column=1, row=0, rowspan=7, sticky='NS', padx=5)

        sep2 = ttk.Separator(self.cus_host, orient='vertical')
        sep2.grid(column=3, row=0, rowspan=7, sticky='NS', padx=5)

        l_tt = ttk.Label(self.cus_host, text='Total Amount (UGX)')
        l_tt.grid(column=2, row=0, sticky='E')
        l_dis = ttk.Label(self.cus_host, text='Discount (UGX)')
        l_dis.grid(column=4, row=0, sticky='W')
        l_mo_tbp = ttk.Label(self.cus_host, text='Amount To Be Paid (UGX)')
        l_mo_tbp.grid(column=2, row=2, sticky='E')
        l_mo_p = ttk.Label(self.cus_host, text='Amount Paid (UGX)')
        l_mo_p.grid(column=4, row=2, sticky='W')
        l_bl = ttk.Label(self.cus_host, text='Balance (UGX)')
        l_bl.grid(column=2, row=4, sticky='E')

        self.v_tt = tk.StringVar()
        self.v_dis = tk.StringVar()
        self.v_mo_tbp = tk.StringVar()
        self.v_mo_p = tk.StringVar()
        self.v_bl = tk.StringVar()

        self.e_tt = ttk.Entry(self.cus_host, textvariable=self.v_tt, state='readonly')
        self.e_dis = ttk.Entry(self.cus_host, textvariable=self.v_dis)
        self.e_mo_tbp = ttk.Entry(self.cus_host, textvariable=self.v_mo_tbp, state='readonly')
        self.e_mo_p = ttk.Entry(self.cus_host, textvariable=self.v_mo_p)
        self.e_bl = ttk.Entry(self.cus_host, textvariable=self.v_bl, state='readonly')

        es_p = [self.e_tt, self.e_dis, self.e_mo_tbp, self.e_mo_p, self.e_bl]
        es_pw(es_p)
        self.cus_entries_w()

        self.btn_checkout = ttk.Button(self.cus_host, text='Check Out')
        self.btn_cw()

    def cus_entries_w(self):
        self.e_tt.grid(column=2, row=1, sticky='E')
        self.e_dis.grid(column=4, row=1, sticky='W')
        dis = Validate(self.v_dis, self.e_dis)
        dis.int_(min_=0)
        self.e_dis.bind('<KeyRelease>', self._dis_w, True)
        self.e_mo_tbp.grid(column=2, row=3, sticky='E')
        self.e_mo_p.grid(column=4, row=3, sticky='W')
        paid = Validate(self.v_mo_p, self.e_mo_p)
        paid.int_(min_=0)
        self.e_mo_p.bind('<KeyRelease>', self._mo_p_w, True)
        self.e_bl.grid(column=2, row=5, sticky='E')

    def _dis_w(self, event=None):

        if int('0' + str(self.v_dis.get())) > 0:
            tbp = int(self.total_amount) - int(self.v_dis.get())
            self.v_mo_tbp.set(str(tbp))
            self.v_bl.set(str(tbp))
            self.v_mo_p.set(str(0))
        else:
            self.v_mo_tbp.set(str(self.total_amount))
            self.v_mo_p.set(str(0))
            self.v_bl.set(str(self.total_amount))

    def _mo_p_w(self, event):

        if int('0' + str(self.v_mo_p.get())) > 0:
            _bl = int(self.v_mo_tbp.get()) - int(self.v_mo_p.get())
            self.v_bl.set(str(_bl))
        else:
            self.v_bl.set(str(self.v_mo_tbp.get()))

    def btn_cw(self):
        self.btn_checkout.grid(column=4, row=5, padx=5, sticky='SE')
        self.btn_checkout.bind("<Button-1>", self._checkout)

    def _checkout(self, event=None):
        if msg.askquestion('Itory: Checkout Confirmation',
                           'Confirm the Sale?') == u'yes':
            cus_name = self.v_nm.get()
            cus_tel = self.v_tel.get()
            cus_email = self.v_eml.get()

            amo_pd = self.v_mo_p.get()
            bal = self.v_bl.get()

            _dt = datetime.now()
            dt_str = self.vd_year.get().zfill(4) + '-' + \
                     self.vd_month.get().zfill(2) + \
                     '-' + self.vd_day.get().zfill(2) + '|' + \
                     str(_dt.hour).zfill(2) + \
                     ':' + str(_dt.minute).zfill(2) + ':' + \
                     str(_dt.second).zfill(2)
            selected_items = self.selected_items_list[:]
            names = []
            for item in selected_items:
                names.append(str(item['qty']) + '-' + item['name'])

            sale = {'customer_name': cus_name,
                    'customer_contact': cus_tel + ',' + cus_email,
                    'amount_paid': amo_pd,
                    'balance': bal,
                    'items': names,
                    'sale_date': dt_str}

            income = {'from': 'Sales', 'income_date': dt_str,
                      'details': names,
                      'amount': amo_pd}

            self.sales_inst.add(sale)
            self.inc_inst.work.add(income)

            for item in self.selected_items_list:
                for _item in self.items_inst.get_all():
                    if item['name'] == _item['name']:
                        new_qty = _item['qty'] - item['qty']
                        self.items_inst.edit_qty(_item['name'], new_qty)
            self.set_items(self.items_inst.get_all())

            if int(bal) > 0:
                debtor = {'name': cus_name,
                          'tel': cus_tel,
                          'email': cus_email,
                          'paid': amo_pd,
                          'balance': bal,
                          'details': names,
                          'debt_date': dt_str}
                self.debt_inst.work.add(debtor)

            self.clear_all_items()
            self.clear_cus()

    def clear_cus(self):
        self.v_nm.set('')
        self.v_tel.set('')
        self.v_eml.set('')
