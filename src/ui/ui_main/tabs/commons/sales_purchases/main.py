from datetime import datetime
from tkinter import ttk

from src.data.works import sort
from src.data.works.search import Search
from .all import All
from .options_top import OptionsTop
from .options_bottom import OptionsBottom


class Main(All, Search, OptionsTop, OptionsBottom):

    def __init__(self, container, _inst, s_bar, _caller):
        self.host = container
        self._inst = _inst
        self.sb = s_bar
        self.caller = _caller

        self._use = None
        self._date_key = None
        self._amo_key = None
        self._bal_key = None
        if self.caller == 'Purchases':
            self._use = ['purchase_date', 'item', 'details']
            self._date_key = 'purchase_date'
            self._amo_key = 'amount'

            self._keys = ['purchase_date',
                          'item',
                          'details',
                          'amount']

            self.titles = [{'text': 'Date', 'width': 20, 'type': 'l'},
                           {'text': "Item", 'width': 35, 'type': 'l'},
                           {'text': "Details", 'width': 40, 'type': 'l'},
                           {'text': 'Amount', 'width': 25, 'type': 'l'}]

        elif self.caller == 'Sales':
            self._use = ['sale_date', 'customer_name', 'customer_contact']
            self._date_key = 'sale_date'
            self._amo_key = 'amount_paid'
            self._bal_key = 'balance'

            self._keys = ['sale_date',
                          'customer_name',
                          'customer_contact',
                          'amount_paid',
                          'balance',
                          'items']

            self.titles = [{'text': 'Date', 'width': 20, 'type': 'l'},
                           {'text': "Customer", 'width': 20, 'type': 'l'},
                           {'text': "Contact", 'width': 23, 'type': 'l'},
                           {'text': 'Paid', 'width': 15, 'type': 'l'},
                           {'text': 'Balance', 'width': 15, 'type': 'l'},
                           {'text': 'Items Sold', 'width': 25, 'type': 'c'}]

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
        self.work_on_years_and_months()

        OptionsTop.__init__(self)
        OptionsBottom.__init__(self)
        self.work_on_period()
        All.__init__(self)
        Search.__init__(self, self.f_search, self.fill,
                        self._list, self._use, width=40)

        self._current_month = None
        self._current_year = None

    def _works(self):
        self._main_frame_w()
        self._year_month_day_w()
        self._search_w()

    def work_on_years_and_months(self, year_: str = None, month_: str = None):

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

        self.years.append(self._current_year)
        self.months.append('All')
        self.months.append(self._current_month)
        self.days.append('All')
        for row in self._inst.get_all():
            _s_date = row[self._date_key].split('|')[0]
            _s_year = _s_date.split('-')[0]
            _s_month = _s_date.split('-')[1]
            _s_day = _s_date.split('-')[2]
            if _s_year not in self.years:
                self.years.append(_s_year)
            if self._current_year == _s_year and _s_month not in self.months:
                self.months.append(_s_month)
            if self._current_year == _s_year and \
                    self._current_month == _s_month and \
                    _s_day not in self.days:
                self.days.append(_s_day)

        if self._current_year == _y and self._current_month == _m and \
                _d not in self.days:
            self.days.append(_d)

        self.years.sort(reverse=True)
        self.months.sort(reverse=True)
        self.days.sort(reverse=True)

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

    def work_on_period(self, _year: int = None, _month: int = None,
                       _day: int = None):
        _dt = datetime.now()

        if _year is None:
            _year = str(_dt.year).zfill(4)
            self.work_on_years_and_months(_year)
            self.year_combo.current(self.years.index(_year))
        if _month is None:
            _month = str(_dt.month).zfill(2)
            self.work_on_years_and_months(_year, _month)
            self.month_combo.current(self.months.index(_month))
        if _day is None:
            _day = str(_dt.day).zfill(2)
            self.work_on_years_and_months(_year, _month)
            self.day_combo.current(self.days.index(_day))

        self._list[:] = []

        for row in self._inst.get_all():
            _s_date = row[self._date_key].split('|')[0]
            _s_year = _s_date.split('-')[0]
            _s_month = _s_date.split('-')[1]
            _s_day = _s_date.split('-')[2]

            if _s_year == str(_year) and \
                    row not in self._list and \
                    (str(_month) == 'All' or _s_month == str(_month)) and \
                    (str(_day) == 'All' or _s_day == str(_day)):
                self._list.append(row)

        sort.rows(self._list, self._date_key)


def dt_split(_line):
    _s_datetime = _line[self._date_key].split('|')
    _date = _s_datetime[0]
    _dt = _date.split('-')
    _t = _s_datetime[1]
    return {'year': int(_dt[0]),
            'month': int(_dt[1]),
            'day': int(_dt[2]),
            'hour': int(_t[0]),
            'minute': int(_t[1]),
            'second': int(_t[2])}
