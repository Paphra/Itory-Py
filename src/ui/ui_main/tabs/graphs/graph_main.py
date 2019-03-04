import tkinter as tk
from tkinter import ttk
from .graph_list import GraphList
from .graph_top_options import GraphTopOptions
from .graph_bottom_options import GraphBottomOptions
from .graph import Graph
from data.works import sort
from datetime import datetime
import numpy as np
from data.works import convert
from ui.routine.date_works import split_date


class GraphMain(GraphTopOptions, GraphBottomOptions, GraphList,
                Graph):

    def __init__(self, container, s_bar, insts):
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
        self._list = []

        self.caller = None
        self._inst = None
        self.x_label = 'Days of the Month'
        self.y_label = 'Sales [000] (UGX)'
        self.amounts = {}
        self.x_values = []
        self.y_values = []

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

    def work_on_years_and_months(self, year_=None, month_=None):
        self.months[:] = []
        self.years[:] = []

        _dt = datetime.now()
        _y = str(_dt.year).zfill(4)
        _m = str(_dt.month).zfill(2)

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
        if self._current_month not in self.months:
            self.months.append(self._current_month)
        for row in self._inst.get_all():
            _date = split_date(row[self.caller['date_key']])
            _year = _date['year']
            _month = _date['month']

            self._y_m(_year, _month)

        self.years.sort(reverse=True)
        self.months.sort(reverse=True)

        self.set_years_months()

        self.year_combo.current(self.years.index(self._current_year))
        self.month_combo.current(self.months.index(self._current_month))
        self._list[:] = []

        for row in self._inst.get_all():
            _date = split_date(row[self.caller['date_key']])
            _year = _date['year']
            _month = _date['month']

            if _year == self._current_year and \
                    row not in self._list and \
                    (self._current_month == 'All' or
                     _month == self._current_month):
                self._list.append(row)

        sort.rows(self._list, self.caller['date_key'])
        self.make_xy()

    def set_years_months(self):
        self.year_combo['values'] = self.years
        self.month_combo['values'] = self.months

    def _y_m(self, _year, _month):
        if _year not in self.years:
            self.years.append(_year)
        if self._current_year == _year and _month not in self.months:
            self.months.append(_month)

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
