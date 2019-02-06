import tkinter as tk
from tkinter import ttk

from src.data.works import check


class ItemList:

    def __init__(self):

        self.ht = 26
        self.wt = 25

        self.f_items_list = ttk.Frame(self.mf_all_items_list)
        self.all_items_listbox = self.scroll_list_box. \
            new(self.f_items_list, width=35, height=26)

        self.lbox_w()

    def lbox_w(self):
        self.f_items_list.grid(column=0, row=1, sticky='NESW', padx=5, pady=5)
        self.f_items_list.configure(width=230, height=400)

        self.all_items_listbox.bind("<ButtonRelease-1>", self._list_selection)
        self.set_items(self.items_inst.get_all())

    def _list_selection(self, event=None):
        cur = self.all_items_listbox.curselection()
        if self.all_items_listbox.get(0) != 'No Items Found!':
            self._select(cur)

    def _select(self, cur):
        for ind in cur:
            sl = self.all_items_listbox.get(ind)
            sl_l = sl.split("  \t\t  ")
            item_name = sl_l[0][1:]

            num = self.selected_items_listbox.size()
            if num > 0:
                list_box_lines = self.selected_items_listbox.get(0, (num - 1))
                line_names = []
                for _line in list_box_lines:
                    split_line = _line.split("-")
                    line_names.append(split_line[1])
                if item_name in line_names:
                    break
            n_i = "1-" + item_name

            for item in self.items_inst.get_all():
                if item['name'] == item_name:
                    typ = item['type']
                    qty = 1
                    sell_unit = item['sell_unit']
                    amt = sell_unit

                    my_item = {
                            'name': item_name,
                            'type': typ,
                            'sell_unit': sell_unit,
                            'qty': qty,
                            'amount': amt
                    }
                    self.c_selected_items.add_item(my_item)

            self.selected_items_listbox.insert(num, n_i)
            self.selected_items_listbox.activate(num)

            self.selected_items_listbox.event_generate("<Button-1>")
            self.selected_items_listbox.event_generate("<ButtonRelease-1>")
            self.selected_items_listbox.event_generate("<KeyRelease>")
            self._put()
            self._selections()

            self.total_amount = self.c_selected_items.get_total_amount()
            self.update_amount_customer()

    def set_items(self, items):
        """Set Items on to the list.
        :type: items: list list of items to be set on the list of items."""

        _msg_empty = 'No Items Found!'
        _return = {'name': _msg_empty, 'type': '',
                   'qty': 0, 'sell_unit': 0}
        _items = check.if_empty(items, _return)

        self.all_items_listbox.configure(state='normal')
        l_num = self.all_items_listbox.size()
        if l_num > 0:
            self.all_items_listbox.delete(0, (l_num - 1))

        if _items[0]['name'] == _msg_empty:
            self.all_items_listbox.insert(tk.END, _items[0]['name'])
            self.all_items_listbox.configure(state='disabled')
            return True

        for item in _items:
            if item['qty'] > 0:
                i_nm = ' ' + item['name'] + '  \t\t  ' + str(item['qty'])
                self.all_items_listbox.insert(tk.END, i_nm)

        self.total_amount = self.c_selected_items.get_total_amount()
        self.update_amount_customer()

    def get_list(self):
        return self.items_inst.get_all()
