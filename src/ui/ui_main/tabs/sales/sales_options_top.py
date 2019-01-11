import tkinter as tk
from tkinter import ttk


class SalesOptionsTop:

    def __init__(self):
        self.v_year = tk.StringVar()
        self.v_month = tk.StringVar()
        self.v_day = tk.StringVar()
        self.year_combo = ttk.Combobox(self.lf_year)
        self.month_combo = ttk.Combobox(self.lf_month)
        self.day_combo = ttk.Combobox(self.lf_day)

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

        self.day_combo.grid(column=0, row=0, sticky='ENS', padx=5)
        self.day_combo.configure(state='readonly', values=self.days,
                                 width=10, textvariable=self.v_day)
        self.day_combo.bind('<<ComboboxSelected>>', self.day_selection_works)
        self.day_combo.current(0)

    def set_years_months_days(self):
        self.year_combo['values'] = self.years
        self.month_combo['values'] = self.months
        self.day_combo['values'] = self.days

    def _year_selection(self, event=None):
        _year = self.v_year.get()
        self.work_on_years_and_months(_year)
        self.month_combo['values'] = self.months
        self.month_combo.current(0)
        _month = self.v_month.get()
        self.work_on_years_and_months(_year, _month)
        self.day_combo['values'] = self.days
        self.day_combo.current(0)
        _day = self.v_day.get()
        self.work_on_period_sales(_year, _month, _day)
        self.all_sales_fill()

    def _month_selection(self, event=None):
        _month = self.v_month.get()
        _year = self.v_year.get()
        self.work_on_years_and_months(_year, _month)
        self.day_combo['values'] = self.days
        self.day_combo.current(0)
        _day = self.v_day.get()
        self.work_on_period_sales(_year=_year, _month=_month, _day=_day)
        self.all_sales_fill()

    def day_selection_works(self, event=None):
        _day = self.v_day.get()
        _month = self.v_month.get()
        _year = self.v_year.get()
        self.work_on_years_and_months(_year, _month)
        self.work_on_period_sales(_year, _month, _day)
        self.all_sales_fill()
