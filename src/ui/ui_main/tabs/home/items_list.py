
import tkinter as tk
from tkinter import ttk
from .items_search import ItemSearch


class ItemList:

    def __init__(self):

        self.ht = 26
        self.wt = 25
        
        self.f_items_list = ttk.Frame(self.mf_all_items_list)
        self.all_items_listbox = tk.Listbox(self.f_items_list)

        self.item_search = ItemSearch(self, self.mf_all_items_list)
        self.x = tk.Scrollbar(self.f_items_list, orient='horizontal')
        self.y = tk.Scrollbar(self.f_items_list, orient='vertical')

        self.lbox_w()

    def lbox_w(self):
        self.f_items_list.grid(column=0, row=1, sticky='NESW', padx=5, pady=5)
        self.f_items_list.configure(width=230, height=400)

        self.all_items_listbox.grid(column=0, row=0, sticky='NESW', padx=5, pady=5)
        self.y.grid(column=1, row=0, sticky='NS')
        self.x.grid(column=0, row=1, sticky='EW')

        self.all_items_listbox.configure(xscrollcommand=self.x.set,
                                         yscrollcommand=self.y.set,
                                         width=28, height=26)

        self.x['command'] = self.all_items_listbox.xview
        self.y['command'] = self.all_items_listbox.yview
    
        self.all_items_listbox.bind("<ButtonRelease-1>", self._list_selection)        
        self.set_items(self.all_items_list)

    def _list_selection(self, event=None):
        cur = self.all_items_listbox.curselection()
        if len(cur) > 0:
            self._select(cur)

    def _select(self, cur):
        for ind in cur:
            sl = self.all_items_listbox.get(ind)
            sl_l = sl.split("  \t\t  ")
            item_name = sl_l[0]

            num = self.selected_items_listbox.size()
            if num > 0:
                sil_cos = self.selected_items_listbox.get(0, (num - 1))
                sil_icos = []
                for li in sil_cos:
                    i = li.split("-")
                    sil_icos.append(i[1])
                if item_name in sil_icos:
                    break
            n_i = "1-" + item_name

            for item in self.all_items_list:
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
        l_num = self.all_items_listbox.size()
        if l_num > 0:
            self.all_items_listbox.delete(0, (l_num - 1))
            
        if items[0] == 'No Items Found!':
            self.all_items_listbox.insert(tk.END, items[0])
            return True

        for item in items:
            if item['qty'] > 0:
                i_nm = item['name'] + '  \t\t  ' + str(item['qty'])
                self.all_items_listbox.insert(tk.END, i_nm)

        self.total_amount = self.c_selected_items.get_total_amount()
        self.update_amount_customer()

    def get_list(self):
        return self.all_items_list
