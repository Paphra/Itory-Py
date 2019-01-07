
import tkinter as tk
from tkinter import ttk
from datetime import datetime
from data.sales import Sales


class Checkout:

    def __init__(self):

        l_nm = ttk.Label(self.cus_host, text='Name')
        l_tel = ttk.Label(self.cus_host, text='Telephone No.')
        l_eml = ttk.Label(self.cus_host, text='Email Address')

        lbs_c = [l_nm, l_tel, l_eml]
        self.lbs_cw(lbs_c)

        self.v_nm = tk.StringVar()
        self.v_tel = tk.StringVar()
        self.v_eml = tk.StringVar()

        self.e_nm = ttk.Entry(self.cus_host, textvariable=self.v_nm)
        self.e_tel = ttk.Entry(self.cus_host, textvariable=self.v_tel)
        self.e_eml = ttk.Entry(self.cus_host, textvariable=self.v_eml)
        
        es_c = [self.e_nm, self.e_tel, self.e_eml]
        self.es_cw(es_c)

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
        self.es_pw(es_p)
        self.cus_entries_w()

        self.btn_checkout = ttk.Button(self.cus_host, text='Check Out')
        self.btn_cw()

    def cus_entries_w(self):
        self.e_tt.grid(column=2, row=1, sticky='E')

        self.e_dis.grid(column=4, row=1, sticky='W')
        self.e_dis.bind('<FocusIn>', self._focus_in)
        self.e_dis.bind('<FocusOut>', self._focus_out)
        self.e_dis.bind("<KeyPress>", self._dis_wp)
        self.e_dis.bind("<KeyRelease>", self._dis_w)

        self.e_mo_tbp.grid(column=2, row=3, sticky='E')

        self.e_mo_p.grid(column=4, row=3, sticky='W')
        self.e_mo_p.bind('<FocusIn>', self._focus_in)
        self.e_mo_p.bind('<FocusOut>', self._focus_out)
        self.e_mo_p.bind("<KeyPress>", self._mo_p_wp)
        self.e_mo_p.bind("<KeyRelease>", self._mo_p_w)

        self.e_bl.grid(column=2, row=5, sticky='E')

    def _dis_wp(self, event):
        self._dis = self.v_dis.get()

    def _mo_p_wp(self, event):
        self._mo_p = self.v_mo_p.get()

    def _dis_w(self, event):
        if not self._val(self.v_dis.get()):
            self.v_dis.set(self._dis)

        if int('0' + str(self.v_dis.get())) > 0:
            tbp = int(self.total_amount) - int(self.v_dis.get())
            self.v_mo_tbp.set(str(tbp))
        else:
            self.v_mo_tbp.set(str(self.total_amount))

    def _mo_p_w(self, event):
        if not self._val(self.v_mo_p.get()):
            self.v_mo_p.set(self._mo_p)
        
        if int('0' + str(self.v_mo_p.get())) > 0:
            bl = int(self.v_mo_tbp.get()) - int(self.v_mo_p.get())
            self.v_bl.set(str(bl))
        else:
            self.v_bl.set(str(self.v_mo_tbp.get()))

    def label_works(self, els, col, s):
        ii = 0
        for i in range(len(els)):
            if i > 0:
                ii = ii+2
            els[i].grid(column=col, row=ii, padx=10, sticky=s)

    def lbs_cw(self, lbs):
        self.label_works(lbs, 0, 'W')

    def entry_works(self, els, col, s):
        ii = 0
        for e in range(len(els)):
            if e > 0:
                ii = ii+2
            else:
                ii = ii+1
            els[e].grid(column=col, row=ii, padx=10, pady=5, sticky=s)

    def es_cw(self, es):
        self.entry_works(es, 0, 'w')

    def es_pw(self, es):
        for i in es:
            i.configure(width=17)

    def btn_cw(self):
        self.btn_checkout.grid(column=4, row=5, padx=5, sticky='SE')
        self.btn_checkout.bind("<Button-1>", self._checkout)

    def _checkout(self, event=None):
        cus_name = self.v_nm.get()
        cus_tel = self.v_tel.get()
        cus_email = self.v_eml.get()

        amo_pd = self.v_mo_p.get()
        bal = self.v_bl.get()

        _dt = datetime.now()
        dt_str = str(_dt.year) + '-' + str(_dt.month) + '-' \
            + str(_dt.day) + '|' + str(_dt.hour) + ':'      \
            + str(_dt.minute) + ':' + str(_dt.second)

        sale = {
            'customer_name': cus_name,
            'customer_contact': cus_tel + ',' + cus_email,
            'amount_paid': amo_pd,
            'balance': bal,
            'items': self.selected_items_list,
            'sale_date': dt_str
        }

        self.sales_inst.add_sale_given_sale(sale)

        for item in self.selected_items_list:
            for _item in self.all_items_list:
                if item['name'] == _item['name']:
                    new_qty = _item['qty'] - item['qty']
                    self.items_inst.edit_qty_given_name(_item['name'], new_qty)
        self.set_items(self.all_items_list)

        self.clear_all_items()
