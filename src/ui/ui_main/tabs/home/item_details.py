
import tkinter as tk
from tkinter import ttk


def lbs_w(lbs):
    for c in range(5):
        if c < 3:
            lbs[c].grid(column=c, row=0, sticky='W', padx=3)
        else:
            if c == 4:
                lbs[c].grid(column=(c-3), row=3, sticky='W', padx=3, columnspan=2)
            else:
                lbs[c].grid(column=(c-3), row=3, sticky='W', padx=3)


def es_w(es):
    for c in range(5):
        if c < 3:
            es[c].grid(column=c, row=1, sticky='W', padx=3, pady=3)
        else:
            if c == 4:
                es[c].grid(column=(c-3), row=4, sticky='W', padx=3, pady=3, columnspan=2)
            else:
                es[c].grid(column=(c-3), row=4, sticky='W', padx=3, pady=3)


def _val(txt):
    try:
        if len(txt) > 0:
            int(txt)
        return True
    except TypeError:
        return False


class ItemDetails:

    def __init__(self):
        self.c_selected_items = SelectedItems()

        self.selected_items_list = self.c_selected_items.get_all()
        self.selected_item_full = None
        self.total_amount = None

        self.v_qty = tk.StringVar()
        self.v_sell_unit = tk.StringVar()
        self.v_amt = tk.StringVar()

        self.l_nm = ttk.Label(self.dls_host)
        self.l_typ = ttk.Label(self.dls_host)
        self.e_qty = ttk.Entry(self.dls_host)
        self.e_sell_unit = ttk.Entry(self.dls_host)
        self.e_amt = ttk.Entry(self.dls_host)
        self.rm_btn = ttk.Button(self.dls_host, text='Remove')
        self.clr_btn = ttk.Button(self.dls_host, text='Clear All')

        self._put()

    def _put(self):

        self.selected_items_listbox.bind('<ButtonRelease-1>', self._selections)
        self.selected_items_listbox.bind('<KeyRelease>', self._selections)

        self.l_nm.configure(text='Name of Item')
        self.l_typ.configure(text='Type of Item')

        self.e_qty.bind('<FocusIn>', self._focus_in)
        self.e_qty.bind('<FocusOut>', self._focus_out)
        self.e_qty.bind('<KeyPress>', self._val_qtyp)
        self.e_qty.bind('<KeyRelease>', self._val_qtyr)
        self.e_qty.configure(textvariable=self.v_qty, width=10)

        self.e_sell_unit.bind('<FocusIn>', self._focus_in)
        self.e_sell_unit.bind('<FocusOut>', self._focus_out)
        self.e_sell_unit.bind('<KeyPress>', self._val_sell_unitp)
        self.e_sell_unit.bind('<KeyRelease>', self._val_sell_unitr)
        self.e_sell_unit.configure(textvariable=self.v_sell_unit, width=22)

        self.e_amt.configure(textvariable=self.v_amt, width=30)

        es_l = [self.l_nm, self.l_typ, self.e_qty,
                self.e_sell_unit, self.e_amt]

        l_nm = ttk.Label(self.dls_host, text='Name')
        l_typ = ttk.Label(self.dls_host, text='Type')
        l_qty = ttk.Label(self.dls_host, text='Quantity')
        l_sell_unit = ttk.Label(self.dls_host, text='Unit Price (UGX)')
        l_amt = ttk.Label(self.dls_host, text='Amount (UGX)')
        lbs_l = [l_nm, l_typ, l_qty, l_sell_unit, l_amt]

        sep1 = ttk.Separator(self.dls_host)
        sep1.grid(column=0, row=2, sticky='WE', pady=5, columnspan=3)

        self.rm_btn['state'] = 'disabled'
        self.e_amt['state'] = 'readonly'
        self.e_qty['state'] = 'disabled'
        self.e_sell_unit['state'] = 'disabled'

        lbs_w(lbs_l)
        es_w(es_l)
        self.btn_w()

    def btn_w(self):
        self.rm_btn.grid(column=2, row=6, sticky='E', padx=3, pady=3)
        self.rm_btn.configure(state='disabled')

        self.rm_btn.bind('<ButtonRelease-1>', self.remove_item)

        self.clr_btn.grid(column=0, row=6, sticky='E', padx=3, pady=3)
        self.clr_btn.configure(state='disabled')

        self.clr_btn.bind('<ButtonRelease-1>', self.clear_all_items)

    def remove_item(self, event=None):
        self.c_selected_items.delete_item(self.selected_item_full)
        self.selected_items_listbox.delete(self.cur_selection[0])
        self.c_selected_items.delete_item(self.selected_item_full)
        self.selected_items_listbox.event_generate("<Button-1>")
        self.selected_items_listbox.event_generate("<ButtonRelease-1>")
        self._selections()

        self.total_amount = self.c_selected_items.get_total_amount()
        self.update_amount_customer()

    def clear_all_items(self, event=None):
        self.selected_items_list[:] = []
        self.selected_items_listbox.delete(0, (self.selected_items_listbox.size()-1))
        self.c_selected_items.delete_all()
        self.selected_items_listbox.event_generate("<Button-1>")
        self.selected_items_listbox.event_generate("<ButtonRelease-1>")
        self._selections()

        self.total_amount = self.c_selected_items.get_total_amount()
        self.update_amount_customer()

    def _selections(self, event=None):
        self.cur_selection = self.selected_items_listbox.curselection()
        if self.cur_selection is None:
            return True
        n1 = len(self.cur_selection)
        if n1 > 0 and n1 == 1:
            self.selected_item_raw = self.selected_items_listbox.get(self.cur_selection[0])
            selected_item_split = self.selected_item_raw.split('-')
            self.selected_item_name = selected_item_split[1]

            self.get_selected_item_full()

            selected_item_qty = selected_item_split[0]
            selected_item_type = self.selected_item_full['type']
            selected_item_sell_unit = self.selected_item_full['sell_unit']
            for item in self.items_inst.get_all():
                if item['name'] == self.selected_item_name:
                    self.selected_item_max_qty = item['qty']
            self.selected_item_amount = int(selected_item_qty) * selected_item_sell_unit

            self.l_nm['text'] = self.selected_item_full['name']
            self.l_typ['text'] = selected_item_type
            self.v_qty.set(selected_item_qty)
            self.v_sell_unit.set(selected_item_sell_unit)
            self.v_amt.set(self.selected_item_amount)

            self.rm_btn['state'] = 'enabled'
            self.clr_btn['state'] = 'enabled'
            self.e_qty['state'] = 'enabled'
            self.e_sell_unit['state'] = 'enabled'
            self.btn_checkout['state'] = 'enabled'
        else:
            self.l_nm['text'] = 'Item Name'
            self.l_typ['text'] = 'Item Type'
            self.v_qty.set('')
            self.v_sell_unit.set('')
            self.v_amt.set('')

            self.rm_btn['state'] = 'disabled'
            self.clr_btn['state'] = 'disabled'
            self.e_qty['state'] = 'disabled'
            self.e_sell_unit['state'] = 'disabled'
            self.btn_checkout['state'] = 'disabled'

    def _focus_in(self, event):
        w = event.widget
        self._cfv = w.get()

    def _focus_out(self, event):
        w = event.widget
        v = w.get()
        if v == '':
            w.insert(0, str(self._cfv))

    def _val_qtyp(self, event=None):
        self.qty_ = self.v_qty.get()

    def _val_sell_unitp(self, event=None):
        self.sell_unit_ = self.v_sell_unit.get()

    def _val_qtyr(self, event=None):
        t = self.selected_item_max_qty
        if not _val(self.v_qty.get()):
            self.v_qty.set(self.qty_)

        v = self.v_qty.get()
        if int('0'+v) > t:
            self.v_qty.set(t)

        v = self.v_qty.get()
        if int('0'+v) > 0:
            u = int(self.v_sell_unit.get())
            q = int(v)
            tt = u * q
            self.v_amt.set(str(tt))
            self.c_selected_items.set_qty(self.selected_item_name, q)
            self.c_selected_items.set_sell_unit(self.selected_item_name, u)
            self.c_selected_items.set_amount(self.selected_item_name, tt)

            n_si_nm = v + '-' + self.selected_item_name
            self.selected_items_listbox.delete(self.cur_selection[0])
            self.selected_items_listbox.insert(self.cur_selection[0], n_si_nm)
            self.selected_items_listbox.activate(self.cur_selection[0])

        self.total_amount = self.c_selected_items.get_total_amount()
        self.update_amount_customer()

    def _val_sell_unitr(self, event=None):
        if not _val(self.v_sell_unit.get()):
            self.v_sell_unit.set(self.sell_unit_)

        v = self.v_sell_unit.get()
        if int('0'+v) > 0:
            u = int(self.v_sell_unit.get())
            q = int(self.v_qty.get())
            tt = u * q
            self.v_amt.set(str(tt))
            self.c_selected_items.set_sell_unit(self.selected_item_name, u)
            self.c_selected_items.set_amount(self.selected_item_name, tt)

        self.total_amount = self.c_selected_items.get_total_amount()
        self.update_amount_customer()

    def update_amount_customer(self):
        if int(self.total_amount) > 0:
            v1 = self.v_sell_unit.get()
            v2 = self.v_qty.get()
            if int('0'+v1) > 0 and int('0'+v2) > 0:
                u = int(self.v_sell_unit.get())
                q = int(self.v_qty.get())
                tt = u * q
                self.v_amt.set(str(tt))
                self.c_selected_items.set_sell_unit(self.selected_item_name, u)
                self.c_selected_items.set_amount(self.selected_item_name, tt)

            self.v_tt.set(str(self.total_amount))
            dis = int('0'+self.v_dis.get())
            amt_tbp = int(self.total_amount) - dis
            self.v_mo_tbp.set(str(amt_tbp))
            bl = int(self.v_mo_tbp.get()) - int('0'+self.v_mo_p.get())
            self.v_bl.set(str(bl))
        else:
            self.v_tt.set(str(self.total_amount))
            self.v_dis.set('0')
            self.v_mo_tbp.set('0')
            self.v_bl.set('0')
            self.v_mo_p.set('0')

    def get_selected_item_full(self):
        self.selected_item_full = self.c_selected_items.get_item(self.selected_item_name)


class SelectedItems:

    def __init__(self):
        self.name = None
        self.type_ = None
        self.sell_unit = None
        self.qty = None
        self.amount = None
        self.item = None
        self.all_selected_items = []

    def add_details(self, name, type_, qty, sell_unit, amount):
        self.name = name
        self.type_ = type_
        self.sell_unit = sell_unit
        self.qty = qty
        self.amount = amount

        self.item = {
            'name': self.name,
            'type': self.type_,
            'qty': self.qty,
            'sell_unit': self.sell_unit,
            'amount': self.amount}
        self.all_selected_items.append(self.item)

    def add_item(self, item):
        self.item = item
        self.all_selected_items.append(self.item)

    def get_item(self, name):
        if len(self.all_selected_items) > 0:
            for item in self.all_selected_items:
                if item['name'] == name:
                    return item
        return None

    def set_sell_unit(self, name, sell_unit):
        if len(self.all_selected_items) > 0:
            for item in self.all_selected_items:
                if item['name'] == name:
                    item['sell_unit'] = sell_unit
                    return True
        return False

    def set_qty(self, name, qty):
        if len(self.all_selected_items) > 0:
            for item in self.all_selected_items:
                if item['name'] == name:
                    item['qty'] = qty
                    return True
        return False

    def set_amount(self, name, amount):
        if len(self.all_selected_items) > 0:
            for item in self.all_selected_items:
                if item['name'] == name:
                    item['amount'] = amount
                    return True
        return False

    def delete_item_name(self, name):
        if len(self.all_selected_items) > 0:
            for item in self.all_selected_items:
                if item['name'] == name:
                    self.all_selected_items.remove(item)
                    return True
        return False

    def delete_item(self, item):
        if len(self.all_selected_items) > 0:
            for s_item in self.all_selected_items:
                if s_item == item:
                    self.all_selected_items.remove(item)
                    return True
        return False

    def delete_all(self):
        self.all_selected_items[:] = []

    def get_total_amount(self):
        total_amount = 0
        if len(self.all_selected_items) > 0:
            for s_item in self.all_selected_items:
                total_amount = total_amount + s_item['amount']
        return total_amount

    def get_all(self):
        return self.all_selected_items
