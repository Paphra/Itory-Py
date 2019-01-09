import tkinter as tk
from tkinter import ttk


class SalesOptionsTop:

    def __init__(self):
        self.v_year = tk.StringVar()
        self.v_month = tk.StringVar()
        self.year_combo = ttk.Combobox(self.lf_year)
        self.month_combo = ttk.Combobox(self.lf_month)

        self._y_m_work()

    def _y_m_work(self):
        self.year_combo.grid(column=0, row=0, sticky='ENS')
        self.year_combo.configure(state='readonly', values=self.years,
                                  width=10, textvariable=self.v_year)
        self.year_combo.current(0)
        self.year_combo.bind('<<ComboboxSelected>>', self._year_selection)

        self.month_combo.grid(column=0, row=0, sticky='ENS')
        self.month_combo.configure(state='readonly', values=self.months,
                                   width=10, textvariable=self.v_month)
        self.month_combo.current(0)
        self.month_combo.bind('<<ComboboxSelected>>', self._month_selection)

    def _year_selection(self, event=None):
        print('year', self.v_year.get())

    def _month_selection(self, event=None):
        print('month', self.v_month.get())
