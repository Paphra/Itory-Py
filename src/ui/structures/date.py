import tkinter as tk
from datetime import datetime
from tkinter import ttk

from ui.routine.entry_validate import Validate


class Date:

    def __init__(self, master: any = None, y_width: int = None,
                 m_width: int = None, d_width: int = None,
                 orient: str = None):
        self.vd_day = None
        self.vd_month = None
        self.vd_year = None

        if master is not None:
            self.date_host = master
        if y_width is None:
            self.y_width = 10
        else:
            self.y_width = y_width
        if m_width is None:
            self.m_width = 10
        else:
            self.m_width = m_width
        if d_width is None:
            self.d_width = 10
        else:
            self.d_width = d_width
        if orient is None:
            self.orient = 'horizontal'
        else:
            self.orient = orient

        self.pad_x = 10
        self.pad_y = 5

        self.vd_year = tk.StringVar()
        self.vd_month = tk.StringVar()
        self.vd_day = tk.StringVar()

        self.lf_year = ttk.LabelFrame(self.date_host, text='Year')
        self.lf_month = ttk.LabelFrame(self.date_host, text='Month')
        self.lf_day = ttk.LabelFrame(self.date_host, text='Day')

        self.ed_year = ttk.Entry(self.lf_year, textvariable=self.vd_year)
        self.cb_month = ttk.Combobox(self.lf_month,
                                     textvariable=self.vd_month)
        self.ed_day = ttk.Entry(self.lf_day, textvariable=self.vd_day)

        self._c_date_w()

    def _c_date_w(self):
        if self.orient != 'horizontal':
            self.lf_year.grid(column=0, row=0, padx=self.pad_x,
                              pady=self.pad_y)
            self.lf_month.grid(column=0, row=1, padx=self.pad_x,
                               pady=self.pad_y)
            self.lf_day.grid(column=0, row=2,  padx=self.pad_x,
                             pady=self.pad_y)
        else:
            self.lf_year.grid(column=0, row=0,  padx=self.pad_x,
                              pady=self.pad_y)
            self.lf_month.grid(column=1, row=0,  padx=self.pad_x,
                               pady=self.pad_y)
            self.lf_day.grid(column=2, row=0,  padx=self.pad_x,
                             pady=self.pad_y)

        self._dt = datetime.now()
        _year = str(self._dt.year).zfill(4)
        _month = str(self._dt.month).zfill(2)
        _day = str(self._dt.day).zfill(2)

        self.ed_year.grid(column=0, row=0, padx=5)
        self.ed_year.configure(width=self.y_width)
        self.vd_year.set(_year)

        self.val_year = Validate(self.vd_year, self.ed_year)
        self.val_year.int_(max_=int(_year), min_=1900, max_len_=4)

        self.ed_year.bind('<KeyRelease>', self._y_sel, True)
        self.ed_year.bind('<FocusOut>', self._y_sel, True)

        _months = []
        for i in range(int(_month)):
            _months.append(str(i + 1).zfill(2))
        self.cb_month.grid(column=0, row=0, padx=5)
        self.cb_month.configure(width=self.m_width, values=_months,
                                state='readonly')
        self.cb_month.current(int(_month) - 1)
        self.cb_month.bind('<<ComboboxSelected>>', self._m_sel, True)

        self.ed_day.grid(column=0, row=0, padx=5)
        self.ed_day.configure(width=self.d_width)
        self.vd_day.set(_day)

        self.val_day = Validate(self.vd_day, self.ed_day)
        self.val_day.int_(max_=int(_day), min_=1, max_len_=2, min_len_=2)

    def _y_sel(self, event=None):
        _months = []
        if len(self.vd_year.get()) > 0 and \
                int(self.vd_year.get()) < self._dt.year:
            for i in range(12):
                _months.append(str(i + 1).zfill(2))
            self.cb_month['values'] = _months
            self.cb_month.current(11)

            self._m_sel()
        else:
            for i in range(self._dt.month):
                _months.append(str(i + 1).zfill(2))
            self.cb_month['values'] = _months
            self.cb_month.current(self._dt.month - 1)
            self._m_sel()

    def _m_sel(self, event=None):
        _cur = int(self.vd_month.get())

        def _leap():
            _y = int(self.vd_year.get())
            if _y % 4 == 0 and _y % 2 == 0:
                return 29
            else:
                return 28

        _dic = {1: 31, 2: _leap(), 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30,
                10: 31, 11: 30, 12: 31}
        _days = []
        if (len(self.vd_year.get()) > 0 and
            int(self.vd_year.get()) < self._dt.year) or \
                (len(self.vd_month.get()) > 0 and
                 int(self.vd_month.get()) < self._dt.month):
            self.val_day.int_(max_=_dic[_cur])
            self.vd_day.set(str(_dic[_cur]).zfill(2))
        else:
            for i in range(self._dt.day):
                _days.append(str(i + 1).zfill(2))
            self.val_day.int_(max_=self._dt.day)
            self.vd_day.set(str(self._dt.day))
