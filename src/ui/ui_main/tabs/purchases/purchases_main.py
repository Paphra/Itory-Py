from datetime import datetime
from tkinter import ttk

from src.data.works import sort
from src.data.works.search import Search
from .purchases_all import PurchasesAll
from .purchases_options_top import PurchasesOptionsTop
from .purchases_options_bottom import PurchasesOptionsBottom


class PurchasesMain(PurchasesAll, Search, PurchasesOptionsTop,
                    PurchasesOptionsBottom):

    def __init__(self, container, purchases_inst, s_bar):
        self.host = container
        self.purchases_inst = purchases_inst
        self.sb = s_bar

        self.mf_purchases = ttk.LabelFrame(master=self.host, text="Purchases")
        self.top_row = ttk.Frame(self.host)
        self.lf_year = ttk.LabelFrame(self.top_row, text='Year')
        self.lf_month = ttk.LabelFrame(self.top_row, text='Month')
        self.lf_day = ttk.LabelFrame(self.top_row, text='Day')
        self.f_search = ttk.LabelFrame(self.top_row, text='Search ...')
        self.bottom_row = ttk.Frame(self.host)

        self.purchases_list = []

        self._purchases_works()

        self.years = []
        self.months = []
        self.days = []
        self.work_on_years_and_months()

        PurchasesOptionsTop.__init__(self)
        PurchasesOptionsBottom.__init__(self)
        self.work_on_period_purchases()
        PurchasesAll.__init__(self)

        self._use = ['purchase_date', 'item', 'details']
        Search.__init__(self, self.f_search, self.fill_purchases,
                        self.purchases_list, self._use, width=40)

        self._current_month = None
        self._current_year = None

    def _purchases_works(self):
        self._main_frame_w()
        self._year_month_day_w()
        self._search_w()

    def work_on_years_and_months(self, year_: str = None, month_: str = None):

        self.months[:] = []
        self.years[:] = []
        self.days[:] = []
        _dt = datetime.now()
        if year_ is None:
            self._current_year = str(_dt.year).zfill(4)
        else:
            self._current_year = year_
        if month_ is None:
            self._current_month = str(_dt.month).zfill(2)
        else:
            self._current_month = month_

        self.years.append(self._current_year)
        self.months.append('All')
        self.months.append(self._current_month)
        self.days.append('All')
        self.days.append(str(_dt.day).zfill(2))
        for purchase in self.purchases_inst.get_all_purchases():
            _s_date = purchase['purchase_date'].split('|')[0]
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

        self.years.sort(reverse=True)
        self.months.sort(reverse=True)
        self.days.sort(reverse=True)

    def _main_frame_w(self):
        self.mf_purchases.grid(column=0, row=1, sticky='WENS')
        self.mf_purchases.configure(width=790, height=500)

        self.top_row.grid(column=0, row=0, sticky='NES', pady=5)
        self.bottom_row.grid(column=0, row=2, sticky='NES')

    def _search_w(self):
        self.f_search.grid(column=3, row=0, sticky='ENS', padx=10)

    def _year_month_day_w(self):
        self.lf_year.grid(column=0, row=0, sticky='ENS', padx=10)
        self.lf_month.grid(column=1, row=0, sticky='ENS', padx=10)
        self.lf_day.grid(column=2, row=0, sticky='ENS', padx=10)

    def work_on_period_purchases(self, _year: int = None, _month: int = None,
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

        self.purchases_list[:] = []

        for purchase in self.purchases_inst.get_all_purchases():
            _s_date = purchase['purchase_date'].split('|')[0]
            _s_year = _s_date.split('-')[0]
            _s_month = _s_date.split('-')[1]
            _s_day = _s_date.split('-')[2]

            if _s_year == str(_year) and \
                    purchase not in self.purchases_list and \
                    (str(_month) == 'All' or _s_month == str(_month)) and \
                    (str(_day) == 'All' or _s_day == str(_day)):
                self.purchases_list.append(purchase)

        sort.rows(self.purchases_list, 'purchase_date')
        self.calculate_totals()

    def calculate_totals(self, list_: list = None):
        if list_ is None:
            list_ = self.purchases_list

        _total_bal = 0
        _total_purchases = 0

        for _line in list_:
            _total_purchases = _total_purchases + int(_line['amount'])

        self.v_total.set(_total_purchases)


def dt_split(_line):
    _s_datetime = _line['purchase_date'].split('|')
    _date = _s_datetime[0]
    _dt = _date.split('-')
    _t = _s_datetime[1]
    return {'year': int(_dt[0]),
            'month': int(_dt[1]),
            'day': int(_dt[2]),
            'hour': int(_t[0]),
            'minute': int(_t[1]),
            'second': int(_t[2])}