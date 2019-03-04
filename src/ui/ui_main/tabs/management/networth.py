import tkinter as tk
from tkinter import ttk


class NetWorth:

    def __init__(self):
        self.net_worth = ttk.Frame(self.note_book)
        self.mf_net_worth = ttk.Frame(self.net_worth)

        self.net_worth_works()

    def net_worth_works(self):
        self.note_book.add(self.net_worth, text='Net Worth')
        self.mf_net_worth.grid(column=0, row=0, sticky='NESW')
