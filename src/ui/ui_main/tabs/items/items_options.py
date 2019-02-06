from tkinter import ttk

from src.ui.routine.widget_works import *


class ItemsOptions:

    def __init__(self):

        self.btn_edit_item = ttk.Button(self.f_items_options,
                                        text='Edit Item')
        self.btn_delete_item = ttk.Button(self.f_items_options,
                                          text='Delete Item')
        self.edit_wo()
        self.delete_wo()

    def edit_wo(self):
        self.btn_edit_item.grid(column=0, row=0, sticky='NES',
                                padx=10, pady=5)

        def _edit_item():
            row = self.table.get_selected()
            if row is not None:
                self.editing = True
                disable([self.e_serial, self.e_name])

                self.v_serial.set(row['serial'])
                self.v_name.set(row['name'])
                self.v_qty.set(str(row['qty']))
                self.v_type.set(row['type'])

                buy = int(row['qty']) * int(row['buy_unit'])
                self.v_buy_amount.set(str(buy))
                self.v_sell_unit.set((row['sell_unit']))

            del row

        self.btn_edit_item.configure(command=_edit_item)

    def delete_wo(self):
        self.btn_delete_item.grid(column=1, row=0, sticky='NES',
                                  padx=10, pady=5)

        def _delete_item():
            row = self.table.delete_row()
            self.items_inst.delete_item(row)
            for pur in self.purchases_inst.get_all():
                if row['item_date'] == pur['purchase_date']:
                    self.purchases_inst.delete_purchase(pur)

        self.btn_delete_item.configure(command=_delete_item)
