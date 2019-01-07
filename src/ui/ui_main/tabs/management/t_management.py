
import tkinter as tk
from tkinter import ttk


class TManagement():

    def __init__(self, nt_book, s_bar):
        self.ntb = nt_book
        self.sb = s_bar
        self.t_management = ttk.Frame(self.ntb)
        self.f_t = ttk.Frame(self.t_management)
        self.t_work()

    def t_work(self):
        self.ntb.add(self.t_management, text='Management')
        self.f_t.grid(column=0, row=0, padx=10, pady=10, sticky='NESW')
        self.f_t.configure(width=780, height=500)
    