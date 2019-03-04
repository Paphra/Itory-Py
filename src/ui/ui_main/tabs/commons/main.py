from datetime import datetime
from tkinter import ttk

from data.works import sort
from data.works.search import Search
from ui.routine.date_works import split_date
from .all import All
from .keys import Keys
from .options_bottom import OptionsBottom
from .options_top import OptionsTop


class Main(Keys, All, Search, OptionsTop, OptionsBottom):

    def __init__(self, container, s_bar, _inst, _caller):
        self.host = container
        if _caller == 'Debtors':
            self._inst = _inst[0]
            self.inc_inst = _inst[1]
        else:
            self._inst = _inst
        self.sb = s_bar
        self.caller = _caller

        self._use = []
        self._date_key = None
        self._amo_key = None
        self._bal_key = None
        self._keys = []
        self.titles = []
        self.height = None

        Keys.__init__(self)

        self.mf = ttk.LabelFrame(master=self.host, text=self.caller)
        self.top_row = ttk.Frame(self.host)
        self.lf_year = ttk.LabelFrame(self.top_row, text='Year')
        self.lf_month = ttk.LabelFrame(self.top_row, text='Month')
        self.lf_day = ttk.LabelFrame(self.top_row, text='Day')
        self.f_search = ttk.LabelFrame(self.top_row, text='Search ...')
        self.bottom_row = ttk.Frame(self.host)

        self._list = []

        self._works()

        self.years = []
        self.months = []
        self.days = []

        OptionsTop.__init__(self)
        OptionsBottom.__init__(self)
        All.__init__(self, self.height)
        Search.__init__(self, self.f_search, self.fill,
                        self._inst, self._use, width=40)

        self._current_month = None
        self._current_year = None
        self._current_day = None

        self.all_fill()

    def _works(self):
        self._main_frame_w()
        self._year_month_day_w()
        self._search_w()

    def work_on_years_months_days(self, year_=None, month_=None, day_=None):
        self.months[:] = []
        self.years[:] = []
        self.days[:] = []
        _dt = datetime.now()
        _y = str(_dt.year).zfill(4)
        _m = str(_dt.month).zfill(2)
        _d = str(_dt.day).zfill(2)

        if year_ is None:
            self._current_year = _y
        else:
            self._current_year = year_
        if month_ is None:
            self._current_month = _m
        else:
            self._current_month = month_
        if day_ is None:
            self._current_day = _d
        else:
            self._current_day = day_

        self.years.append(self._current_year)
        self.months.append('All')
        if self._current_month not in self.months:
            self.months.append(self._current_month)
        self.days.append('All')
        if self._current_day not in self.days:
            self.days.append(self._current_day)
        for row in self._inst.get_all():
            _date = split_date(row[self._date_key])
            _year = _date['year']
            _month = _date['month']
            _day = _date['day']

            self._y_m_d(_year, _month, _day)

        if self._current_year == _y and self._current_month == _m and \
                _d not in self.days:
            self.days.append(_d)

        self.years.sort(reverse=True)
        self.months.sort(reverse=True)
        self.days.sort(reverse=True)

        self.set_years_months_days()

        self.year_combo.current(self.years.index(self._current_year))
        self.month_combo.current(self.months.index(self._current_month))
        self.day_combo.current(self.days.index(self._current_day))

        self._list[:] = []

        self._set_period()

        sort.rows(self._list, self._date_key)

    def _set_period(self):
        for row in self._inst.get_all():
            _date = split_date(row[self._date_key])
            _year = _date['year']
            _month = _date['month']
            _day = _date['day']

            if _year == self._current_year and \
                    row not in self._list and \
                    (self._current_month == 'All' or
                     _month == self._current_month) and \
                    (self._current_day == 'All' or
                     _day == self._current_day):
                self._list.append(row)

    def set_years_months_days(self):
        self.year_combo['values'] = self.years
        self.month_combo['values'] = self.months
        self.day_combo['values'] = self.days

    def _y_m_d(self, _year, _month, _day):
        if _year not in self.years:
            self.years.append(_year)
        if self._current_year == _year and _month not in self.months:
            self.months.append(_month)
        if self._current_year == _year and \
                self._current_month == _month and \
                _day not in self.days:
            self.days.append(_day)

    def _main_frame_w(self):
        self.mf.grid(column=0, row=1, sticky='WENS')
        self.mf.configure(width=790, height=500)

        self.top_row.grid(column=0, row=0, sticky='NES', pady=5)
        self.bottom_row.grid(column=0, row=2, sticky='NES')

    def _search_w(self):
        self.f_search.grid(column=3, row=0, sticky='ENS', padx=10)

    def _year_month_day_w(self):
        self.lf_year.grid(column=0, row=0, sticky='ENS', padx=10)
        self.lf_month.grid(column=1, row=0, sticky='ENS', padx=10)
        self.lf_day.grid(column=2, row=0, sticky='ENS', padx=10)
