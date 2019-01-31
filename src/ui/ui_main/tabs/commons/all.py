from tkinter import ttk

from src.data.works.check import check_rows
from src.ui.structures.table import Table
from threading import Thread


class All:

    def __init__(self, height_=None):
        self._f_ = ttk.Frame(self.mf)
        if height_ is None:
            height_ = 370
        self.main_table = Table(self._f_, titles=self.titles, height=height_,
                                _keys_=self._keys)

        self._all_w()
        self.all_fill()

    def _all_w(self):
        self._f_.grid(column=0, row=1, sticky='NEWS')

    def all_fill(self, year=None, month=None, day=None):
        self.work_on_years_months_days(year, month, day)
        self.fill(self._list)

    def fill(self, _list):
        rows = check_rows(_list, self.titles, self._keys)
        Thread(target=self.main_table.add_rows(
                rows_list=rows), daemon=True).start()
        self.calculate_totals(rows)

    def calculate_totals(self, list_=None):
        if list_ is None:
            list_ = self._list

        _total_bal = 0
        _total = 0

        for _line in list_:
            amo_v = _line[self._amo_key]
            if amo_v == '':
                _total = _total + 0
            else:
                _total = _total + int(amo_v)
            if self._bal_key is not None:
                bal_v = _line[self._bal_key]
                if bal_v == '':
                    _total_bal = _total_bal + 0
                else:
                    _total_bal = _total_bal + int(bal_v)
                self.v_bal.set(_total_bal)

        self.v_total.set(_total)

