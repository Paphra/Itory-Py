
import tkinter as tk
from tkinter import ttk
from .graph_list import GraphList
from .graph_canvas import GraphCanvas
from .graph_top_options import GraphTopOptions
from .graph_bottom_options import GraphBottomOptions
from .graph import Graph
from src.data.works import sort
from datetime import datetime


class GraphMain(GraphTopOptions, GraphBottomOptions, GraphCanvas, GraphList,
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

        self.work_on_years_and_months()
        GraphTopOptions.__init__(self)
        GraphBottomOptions.__init__(self)
        GraphCanvas.__init__(self)
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

        self.graph_canvas.grid(column=1, row=1, sticky='NESW')
        self.graph_canvas.configure(width=630, height=450)

    def work_on_years_and_months(self, caller=None, inst_=None, year_=None,
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

        if inst_ is None:
            inst_ = self.sales_inst
        self._inst = inst_

        if caller is None:
            caller = {'name': 'sales',
                           'date_key': 'sale_date',
                           'amo_key': 'amount'}
        self.caller = caller

        self.years.append(self._current_year)
        self.months.append('All')
        self.months.append(self._current_month)
        for row in self._inst.get_all():
            _s_date = row[self.caller['date_key']].split('|')[0]
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

    def work_on_period(self, caller=None, inst_=None, year_=None,
                       month_=None):
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
            self.work_on_years_and_months(year_=year_, month_=month_)
            self.month_combo.current(self.months.index(month_))

        if inst_ is None:
            inst_ = self.sales_inst
        self._inst = inst_

        if caller is None:
            self.caller = {'name': 'sales',
                           'date_key': 'sale_date',
                           'amo_key': 'amount'}
        else:
            self.caller = caller

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

    def graph_it(self, caller=None, inst=None, year=None, month=None):
        self.work_on_years_and_months(caller=caller, inst_=inst, year_=year,
                                      month_=month)
        self.work_on_period(caller=caller, inst_=inst, year_=year,
                            month_=month)

        self.plot_it()
