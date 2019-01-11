"""
Module containing class for checking out the selected items
in the store
"""
import tkinter as tk
from datetime import datetime
from tkinter import ttk


class Checkout:
    """
	Class for checking out the selected items in the store to
	a customer.
	"""

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
        """
		Working on the customer entries fields
		:return: None
		"""
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

    def _dis_wp(self, event=None):
        """
		Pressing the key while in the discount entry
		:param event: event that occurs
		:return: None
		"""
        self._dis = self.v_dis.get()

    def _mo_p_wp(self, event=None):
        """
		Pressing the key while in the amount paid entry
		:param event: event that occurs
		:return: None
		"""
        self._mo_p = self.v_mo_p.get()

    def _dis_w(self, event=None):
        """

		:param event:
		:return:
		"""
        if not self._val(self.v_dis.get()):
            self.v_dis.set(self._dis)

        if int('0' + str(self.v_dis.get())) > 0:
            tbp = int(self.total_amount) - int(self.v_dis.get())
            self.v_mo_tbp.set(str(tbp))
        else:
            self.v_mo_tbp.set(str(self.total_amount))

    def _mo_p_w(self, event):
        """
        Button release within the amount paid entry
        :param event: event of the entry
        :return: None
        """

        if not self._val(self.v_mo_p.get()):
            self.v_mo_p.set(self._mo_p)

        if int('0' + str(self.v_mo_p.get())) > 0:
            _bl = int(self.v_mo_tbp.get()) - int(self.v_mo_p.get())
            self.v_bl.set(str(_bl))
        else:
            self.v_bl.set(str(self.v_mo_tbp.get()))

    def label_works(self, els, col, s):
        _ii = 0
        for _i in range(len(els)):
            if _i > 0:
                _ii = _ii + 2
            els[_i].grid(column=col, row=_ii, padx=10, sticky=s)

    def lbs_cw(self, lbs):
        """
		Working on labels
		:param lbs: list of labels to be worked upon
		:return: None
		"""
        self.label_works(lbs, 0, 'W')

    def entry_works(self, els, col, s):
        """
		Working on the entries
		:param els: entries list
		:param col: column
		:param s: separators
		:return: None
		"""
        _ii = 0
        for _e in range(len(els)):
            if _e > 0:
                _ii = _ii + 2
            else:
                _ii = _ii + 1
            els[_e].grid(column=col, row=_ii, padx=10, pady=5, sticky=s)

    def es_cw(self, es):
        """
		Working on the entries
		:param es: entries list
		:return: None
		"""
        self.entry_works(es, 0, 'w')

    def es_pw(self, es):
        """
		Working on the entries
		:param es: entries list
		:return: None
		"""
        for _i in es:
            _i.configure(width=17)

    def btn_cw(self):
        """
		Working on Buttons
		:return: None
		"""
        self.btn_checkout.grid(column=4, row=5, padx=5, sticky='SE')
        self.btn_checkout.bind("<Button-1>", self._checkout)

    def _checkout(self, event=None):
        """
		Performing the checkout action from the button
		:param event:
		:return:
		"""
        cus_name = self.v_nm.get()
        cus_tel = self.v_tel.get()
        cus_email = self.v_eml.get()

        amo_pd = self.v_mo_p.get()
        bal = self.v_bl.get()

        _dt = datetime.now()
        dt_str = self.vd_year.get() + '-' + self.vd_month.get() + \
                 '-' + self.vd_day.get() + '|' + str(_dt.hour).zfill(2) + \
                 ':' + str(_dt.minute).zfill(2) + ':' + str(_dt.second).zfill(2)
        selected_items = self.selected_items_list[:]
        names = []
        for item in selected_items:
            names.append(str(item['qty']) + '-' + item['name'])

        sale = {
                'customer_name': cus_name,
                'customer_contact': cus_tel + ',' + cus_email,
                'amount_paid': amo_pd,
                'balance': bal,
                'items': names,
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
        self.clear_cus()

    def clear_cus(self):
        """
		Clearing the customer details
		:return: None
		"""
        self.v_nm.set('')
        self.v_tel.set('')
        self.v_eml.set('')
