from datetime import datetime
from tkinter import ttk

from src.data.works.search import Search
from .sales_all import SalesAll
from .sales_options_bottom import SalesOptionsBottom
from .sales_options_top import SalesOptionsTop


class SalesMain(SalesAll, Search, SalesOptionsTop, SalesOptionsBottom):

    def __init__(self, container, sales_inst, s_bar):
        self.host = container
        self.sales_inst = sales_inst
        self.sb = s_bar

        self.all_sales_list = self.sales_inst.get_all_sales()
        self.mf_sales = ttk.LabelFrame(master=self.host, text="Sales")
        self.top_row = ttk.Frame(self.mf_sales)
        self.lf_year = ttk.LabelFrame(self.top_row, text='Year')
        self.lf_month = ttk.LabelFrame(self.top_row, text='Month')
        self.f_search = ttk.LabelFrame(self.top_row, text='Search ...')

        self.sales_list = []

        self._sales_works()

        self.years = []
        self.months = []
        self.work_on_years_and_months()
        self.work_on_period_sales()

        SalesOptionsTop.__init__(self)
        SalesOptionsBottom.__init__(self)
        SalesAll.__init__(self)
        self._use = ['sale_date', 'customer_name', 'customer_contact']
        Search.__init__(self, self.f_search, self.fill_sales,
                        self.sales_list, self._use, width=40)

    def _sales_works(self):
        self._main_frame_w()
        self._year_month_w()
        self._search_w()

    def work_on_years_and_months(self):
        self.months = []
        self.years = []
        _dt = datetime.now()
        self._current_year = str(_dt.year).zfill(4)
        self._current_month = str(_dt.month).zfill(2)

        self.years.append(_current_year)
        self.months.append(_current_month)
        for sale in self.all_sales_list:
            _s_date = sale['sale_date'].split('|')[0]
            _s_year = _s_date.split('-')[0]
            _s_month = _s_date.split('-')[1]
            if _s_year not in self.years: self.years.append(_s_year)
            if _s_month not in self.months: self.months.append(_s_month)

        self.years.sort(reverse=True)
        self.months.sort(reverse=True)

    def _main_frame_w(self):
        self.mf_sales.grid(column=0, row=0, sticky='WENS')
        self.mf_sales.configure(width=790, height=500)

        self.top_row.grid(column=0, row=0, sticky='NES', pady=5)

    def _search_w(self):
        self.f_search.grid(column=2, row=0, sticky='ENS', padx=10)

    def _year_month_w(self):
        self.lf_year.grid(column=0, row=0, sticky='ENS', padx=10)
        self.lf_month.grid(column=1, row=0, sticky='ENS', padx=10)

    def work_on_period_sales(self, _year: int = None, _month: int = None):
        if _year is None: _year = self.years[0]
        if _month is None: _month = self.months[0]
        self.sales_list = []

        for sale in self.all_sales_list:
            _s_date = sale['sale_date'].split('|')[0]
            _s_year = _s_date.split('-')[0]
            _s_month = _s_date.split('-')[1]

            if _s_year == str(_year) and _s_month == str(_month):
                self.sales_list.append(sale)
