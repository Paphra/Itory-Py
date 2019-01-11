from tkinter import ttk


class ItemsOptions:

    def __init__(self):
        self.btn_delete_item = ttk.Button(self.f_items_options,
                                          text='Delete Item')
        self.delete_wo()

    def delete_wo(self):
        _col = 0
        for _i in range(2):
            if _i > 0:
                _col = _col + 2
            sep_v = 'sep' + str(_i)
            sep_v = ttk.Separator(self.f_items_options, orient='vertical')
            sep_v.grid(column=_col, row=0, sticky='NS')
        self.btn_delete_item.grid(column=1, row=0, sticky='NES',
                                  padx=10, pady=5)
        sep02 = ttk.Separator(self.f_items_options, orient='horizontal')
        sep02.grid(column=0, row=1, sticky='WE', columnspan=5)

        def _delete_item():
            result = self.table.delete_row()
            del result

        self.btn_delete_item.configure(command=_delete_item)
