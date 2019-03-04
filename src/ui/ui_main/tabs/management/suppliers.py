import tkinter as tk
from tkinter import ttk


class Suppliers:

    def __init__(self):
        self.suppliers = ttk.Frame(self.note_book)
        self.mf_suppliers = ttk.Frame(self.suppliers)

        self.suppliers_works()

    def suppliers_works(self):
        self.note_book.add(self.suppliers, text='Suppliers')
        self.mf_suppliers.grid(column=0, row=0, sticky='NESW')
