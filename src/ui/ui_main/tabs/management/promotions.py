import tkinter as tk
from tkinter import ttk


class Promotions:

    def __init__(self):
        self.promo = ttk.Frame(self.note_book)
        self.mf_promo = ttk.Frame(self.promo)

        self.promo_works()

    def promo_works(self):
        self.note_book.add(self.promo, text='Promotions')
        self.mf_promo.grid(column=0, row=0, sticky='NESW')
