import tkinter as tk
from datetime import datetime
from tkinter import messagebox as msg, ttk


class ItemsAdd:

    def __init__(self):
        # variables
        self.v_name = tk.StringVar()
        self.v_type = tk.StringVar()
        self.v_qty = tk.StringVar()
        self.v_buy_amount = tk.StringVar()
        self.v_sell_unit = tk.StringVar()
        self.v_serial = tk.StringVar()

        self.e_serial = ttk.Entry(self.mf_items_add,
                                  textvariable=self.v_serial,
                                  width=15)
        self.e_name = ttk.Entry(self.mf_items_add, textvariable=self.v_name,
                                width=15)
        self.e_type = ttk.Entry(self.mf_items_add, textvariable=self.v_type,
                                width=15)
        self.e_qty = ttk.Entry(self.mf_items_add, textvariable=self.v_qty,
                               width=15)
        self.e_buy_amount = ttk.Entry(self.mf_items_add,
                                      textvariable=self.v_buy_amount,
                                      width=15)
        self.e_sell_unit = ttk.Entry(self.mf_items_add,
                                     textvariable=self.v_sell_unit,
                                     width=15)

        self.btn_clear_all = ttk.Button(self.mf_items_add, text='Clear All',
                                        command=self._clear_all)
        self.btn_save = ttk.Button(self.mf_items_add, text='Save',
                                   command=self._save_item)

        self.add_works()
        self._clear_all()

    def add_works(self):
        _padx = 5
        _pady = 10
        lb_serial = ttk.Label(self.mf_items_add, text='Serial Number:')
        lb_serial.grid(column=0, row=1, sticky='E', padx=_padx, pady=_pady)
        self.e_serial.grid(column=1, row=1, sticky='W', padx=_padx, pady=_pady)

        lb_name = ttk.Label(self.mf_items_add, text='Item Name:')
        lb_name.grid(column=0, row=2, sticky='E', padx=_padx, pady=_pady)
        self.e_name.grid(column=1, row=2, sticky='W', padx=_padx, pady=_pady)

        lb_type = ttk.Label(self.mf_items_add, text='Item Type:')
        lb_type.grid(column=0, row=3, sticky='E', padx=_padx, pady=_pady)
        self.e_type.grid(column=1, row=3, sticky='W', padx=_padx, pady=_pady)

        lb_qtty = ttk.Label(self.mf_items_add, text='Quantity:')
        lb_qtty.grid(column=0, row=4, sticky='E', padx=_padx, pady=_pady)
        self.e_qty.grid(column=1, row=4, sticky='W', padx=_padx, pady=_pady)
        self.e_qty.bind('<KeyPress>', self._prev)
        self.e_qty.bind('<KeyRelease>', self._qty_ver)

        lb_buy_amount = ttk.Label(self.mf_items_add, text='Buying Amount:')
        lb_buy_amount.grid(column=0, row=5, sticky='E', padx=_padx, pady=_pady)
        self.e_buy_amount.grid(column=1, row=5, sticky='W', padx=_padx, pady=_pady)
        self.e_buy_amount.bind('<KeyPress>', self._prev)
        self.e_buy_amount.bind('<KeyRelease>', self._b_amo_ver)

        lb_sell_unit = ttk.Label(self.mf_items_add, text='Sell Unit Price:')
        lb_sell_unit.grid(column=0, row=6, sticky='E', padx=_padx, pady=_pady)
        self.e_sell_unit.grid(column=1, row=6, sticky='W', padx=_padx, pady=_pady)
        self.e_sell_unit.bind('<KeyPress>', self._prev)
        self.e_sell_unit.bind('<KeyRelease>', self._s_unit_ver)

        sep000 = ttk.Separator(self.mf_items_add, orient='horizontal')
        sep000.grid(column=0, row=7, sticky='WE', columnspan=2, pady=10)
        self.btn_clear_all.grid(column=0, row=8, sticky='E', padx=_padx,
                                pady=_pady)
        self.btn_save.grid(column=1, row=8, sticky='W', padx=_padx,
                           pady=_pady)

    def _prev(self, event):
        self._prev_val = event.widget.get()

    def _qty_ver(self, event):
        self._verify(self.v_qty)

    def _b_amo_ver(self, event):
        self._verify(self.v_buy_amount)

    def _s_unit_ver(self, event):
        self._verify(self.v_sell_unit)

    def _verify(self, v_):
        _new_val = v_.get()

        def _ver_(n_val):
            try:
                int('0' + n_val)
                return True
            except (TypeError, ValueError):
                return False

        if not _ver_(_new_val):
            v_.set(self._prev_val)

    def _clear_all(self):
        self.v_serial.set('')
        self.v_name.set('')
        self.v_type.set('')
        self.v_qty.set('0')
        self.v_buy_amount.set('0')
        self.v_sell_unit.set('0')

        self.all_items_works()

    def _save_item(self):

        serial = self.v_serial.get()
        name = self.v_name.get()
        _type = self.v_type.get()
        qty = int(self.v_qty.get())
        buy_amount = int(self.v_buy_amount.get())
        sell_unit = int(self.v_sell_unit.get())

        if len(name) > 0 and len(_type) > 0 and qty > 0 and \
                buy_amount > 0 and sell_unit > 0 and \
                msg.askquestion('Itory: Save Item Confirmation',
                                'Confirm Item Saving?') == u'yes':
            buy_unit = buy_amount / qty

            for item_ in self.all_items_list:
                o_name = item_['name']
                o_serial = item_['serial']
                if o_name.lower() == name.lower() or \
                        o_serial.lower() == serial.lower():
                    n_qty = item_['qty'] + qty
                    self.all_items_inst.edit_type_given_name(o_name,
                                                             new_type=_type)
                    self.all_items_inst.edit_qty_given_name(o_name,
                                                            new_qty=n_qty)
                    self.all_items_inst.edit_unit_given_name(
                            o_name,
                            new_sell_unit=sell_unit)
                    self.all_items_inst.edit_buy_unit_given_name(
                            o_name,
                            new_buy_unit=buy_unit)

                    self._clear_all()
                    return True

            _dt = datetime.now()
            dt_str = self.vd_year.get() + '-' + self.vd_month.get() + \
                     '-' + self.vd_day.get() + '|' + str(_dt.hour).zfill(2) + \
                     ':' + str(_dt.minute).zfill(2) + ':' + str(_dt.second).zfill(2)

            item = {'serial': serial,
                    'name': name, 'type': _type,
                    'qty': qty, 'buy_unit': buy_unit,
                    'sell_unit': sell_unit}

            purchase = {'purchase_date': dt_str,
                        'item': name,
                        'serial': serial,
                        'details': str(qty) + '-' + _type,
                        'buy_unit': buy_unit,
                        'amount': buy_amount}

            self.all_items_inst.add_full_item(item)
            self.purchases_inst.add_pur_given_pur(purchase)

            self._clear_all()
