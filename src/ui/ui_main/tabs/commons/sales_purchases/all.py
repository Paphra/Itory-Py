from tkinter import ttk

from src.data.works.check import check_rows
from src.ui.structures.table import Table
from threading import Thread


class All:

    def __init__(self):
        self._f_ = ttk.Frame(self.mf)
        self.main_table = Table(self._f_)

        Thread(self.main_table.create(
            titles=self.titles, height=370), daemon=True).start()

        self._all_w()
        self.all_fill()

    def _all_w(self):
        self._f_.grid(column=0, row=1, sticky='NEWS')

    def all_fill(self):
        self.fill(self._list)

    def fill(self, _list: list):
        Thread(target=self.main_table.add_rows(
                rows_list=check_rows(_list, self.titles, self._keys),
                _keys_=self._keys), daemon=True).start()
