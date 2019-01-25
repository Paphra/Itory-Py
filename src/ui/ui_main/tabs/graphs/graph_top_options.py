
import tkinter as tk
from tkinter import ttk


class GraphTopOptions:

    def __init__(self):
        self.v_year = tk.StringVar()
        self.v_month = tk.StringVar()
        self.year_combo = ttk.Combobox(self.lf_year)
        self.month_combo = ttk.Combobox(self.lf_month)

        self._y_m_work()

    def _y_m_work(self):
        self.year_combo.grid(column=0, row=0, sticky='ENS', padx=5)
        self.year_combo.configure(state='readonly', values=self.years,
                                  width=10, textvariable=self.v_year)
        self.year_combo.current(0)
        self.year_combo.bind('<<ComboboxSelected>>', self._year_selection)

        self.month_combo.grid(column=0, row=0, sticky='ENS', padx=5)
        self.month_combo.configure(state='readonly', values=self.months,
                                   width=10, textvariable=self.v_month)
        self.month_combo.current(0)
        self.month_combo.bind('<<ComboboxSelected>>', self._month_selection)

    def set_years_months_days(self):
        self.year_combo['values'] = self.years
        self.month_combo['values'] = self.months

    def _year_selection(self, event=None):
        _year = self.v_year.get()
        self.work_on_years_and_months(year_=_year)
        self.month_combo['values'] = self.months
        self.month_combo.current(0)
        _month = self.v_month.get()
        self.work_on_years_and_months(year_=_year, month_=_month)
        self.work_on_period(year_=_year, month_=_month)
        self.plot_it()

    def _month_selection(self, event=None):
        _month = self.v_month.get()
        _year = self.v_year.get()
        self.work_on_years_and_months(year_=_year, month_=_month)
        self.work_on_period(year_=_year, month_=_month)
        self.plot_it()
