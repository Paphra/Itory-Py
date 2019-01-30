import tkinter as tk
from tkinter import ttk
from .graph_list import GraphList
from .graph_top_options import GraphTopOptions
from .graph_bottom_options import GraphBottomOptions
from .graph import Graph
from src.data.works import sort
from datetime import datetime
import numpy as np
from src.data.works import convert


class GraphMain(GraphTopOptions, GraphBottomOptions, GraphList,
                Graph):

    def __init__(self, container, s_bar, insts):
        """

        :type insts: dict
        :type caller: dict
        """
        self.sb = s_bar
        self.host = container
        self.insts = insts

        self.sales_inst = self.insts['sales']
        self.pur_inst = self.insts['purchases']
        self.acc_inst = self.insts['accounts']

        self.list_pane = ttk.LabelFrame(self.host, text='All Graphs')
        self.top_host = ttk.Labelframe(self.host, text='Period')
        self.lf_year = ttk.Labelframe(self.top_host, text='Year')
        self.lf_month = ttk.LabelFrame(self.top_host, text='Month')

        self.graph_canvas = tk.Canvas(self.host)

        self._current_month = None
        self._current_year = None
        self.current_selection = None
        self.years = []
        self.months = []
        self.days = []
        self._list = []

        self.caller = None
        self._inst = None
        self.x_label = 'Days of the Month'
        self.y_label = 'Sales [000] (UGX)'
        self.amounts = {}
        self.periods = {}
        self.x_values = []
        self.y_values = []

        self.work_on_years_and_months()
        GraphTopOptions.__init__(self)
        self.graph_title = None
        GraphBottomOptions.__init__(self)
        GraphList.__init__(self)
        Graph.__init__(self)

        self._worker()

        self.graph_it()

    def _worker(self):

        self.top_host.grid(column=0, row=0, sticky='NES', columnspan=2)
        self.top_host.configure(width=525)
        self.lf_year.grid(column=0, row=0, sticky='NES', padx=5)
        self.lf_month.grid(column=1, row=0, sticky='NES', padx=5)

        self.list_pane.grid(column=0, row=1, sticky='WNS')
        self.list_pane.configure(width=300, height=500)

        self.graph_canvas.grid(column=1, row=1, sticky='NESW',
                               pady=10, padx=5)
        self.graph_canvas.configure(width=630, height=450)

    def work_on_years_and_months(self, year_=None,
                                 month_=None):
        """

        :type month_: str
        :type year_: str
        :type inst_: object
        :type caller: dict
        """
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

        if self._inst is None:
            self._inst = self.sales_inst

        if self.caller is None:
            self.caller = {'name': 'sales',
                           'date_key': 'sale_date',
                           'amo_key': 'amount_paid'}

        self.years.append(self._current_year)
        self.months.append('All')
        self.months.append(self._current_month)
        for row in self._inst.get_all():
            _s_date = row[self.caller['date_key']].split('|')[0]
            _s_year = _s_date.split('-')[0]
            _s_month = _s_date.split('-')[1]
            _s_day = _s_date.split('-')[2]

            self._y_m_d(_s_year, _s_month, _s_day)

        if self._current_year == _y and self._current_month == _m and \
                _d not in self.days:
            self.days.append(_d)

        self.years.sort(reverse=True)
        self.months.sort(reverse=True)
        self.days.sort(reverse=True)

    def _y_m_d(self, _s_year, _s_month, _s_day):
        if _s_year not in self.years:
            self.years.append(_s_year)
        if self._current_year == _s_year and _s_month not in self.months:
            self.months.append(_s_month)
        if self._current_year == _s_year and \
                self._current_month == _s_month and \
                _s_day not in self.days:
            self.days.append(_s_day)

    def work_on_period(self, year_=None, month_=None):
        """

        :type month_: int
        :type year_: int
        :type inst_: object
        :type caller: dict
        """
        _dt = datetime.now()

        if year_ is None:
            year_ = str(_dt.year).zfill(4)

        self.work_on_years_and_months(year_=year_)
        self.year_combo.current(self.years.index(year_))

        if month_ is None:
            month_ = str(_dt.month).zfill(2)

        self.work_on_years_and_months(year_, month_)
        self.month_combo.current(self.months.index(month_))

        if self._inst is None:
            self._inst = self.sales_inst

        if self.caller is None:
            self.caller = {'name': 'sales',
                           'date_key': 'sale_date',
                           'amo_key': 'amount_paid'}

        self._list[:] = []

        for row in self._inst.get_all():
            _s_date = row[self.caller['date_key']].split('|')[0]
            _s_year = _s_date.split('-')[0]
            _s_month = _s_date.split('-')[1]

            if _s_year == str(year_) and \
                    row not in self._list and \
                    (str(month_) == 'All' or _s_month == str(month_)):
                self._list.append(row)

        sort.rows(self._list, self.caller['date_key'])
        self.make_xy()

    def make_xy(self):
        self.amounts = {}
        if self._current_month != 'All':
            for n in range(0, 31):
                dat = self._current_year + '-' + self._current_month + \
                      '-' + str(n+1).zfill(2)
                self.amounts[dat] = 0

            for item in self._list:
                _s_date = item[self.caller['date_key']].split('|')[0]
                self.amounts[_s_date] = self.amounts[_s_date] + \
                    int(item[self.caller['amo_key']])

            self.x_values[:] = []
            for n in range(0, 31):
                self.x_values.append(n + 1)
        else:
            for n in range(0, 12):
                dat = self._current_year + '-' + str(n+1).zfill(2)
                self.amounts[dat] = 0

            for item in self._list:
                _s_date = item[self.caller['date_key']].split('|')[0]
                _s_ym = _s_date[:-3]
                self.amounts[_s_ym] = self.amounts[_s_ym] + \
                    int(item[self.caller['amo_key']])

            self.x_values = ['Jan',  'Feb', 'Mar', 'Apr', 'May', 'Jun',
                             'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

        dd = []
        for key in self.amounts:
            dd.append(key)

        dd.sort()
        self.y_values[:] = []
        for d in dd:
            self.y_values.append(self.amounts[d]/1000)

    def graph_it(self, year=None, month=None):
        self.work_on_years_and_months(year_=year, month_=month)
        self.work_on_period(year_=year, month_=month)

        if self.current_selection is not None:
            self.y_label = self.current_selection + ' [000] (UGX)'
            if self._current_month == 'All':
                self.graph_title = self.current_selection + \
                    ' For The Year ' + self._current_year
                self.x_label = 'Months Of ' + self._current_year
            else:
                self.graph_title = self.current_selection + ' For ' + \
                    convert.month(self._current_month) + \
                    ' - ' + self._current_year
                self.x_label = 'Days of ' + convert.month(self._current_month)

        else:
            if self._current_month == 'All':
                self.graph_title = 'Sales For The Year ' + self._current_year
                self.x_label = 'Months Of ' + self._current_year
            else:
                self.graph_title = 'Sales For ' + \
                    convert.month(self._current_month) + \
                    ' - ' + self._current_year
                self.x_label = 'Days of ' + convert.month(self._current_month)

        self.plot_it()
