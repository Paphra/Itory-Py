import tkinter as tk
from tkinter import ttk


class Employees:

    def __init__(self):
        self.employees = ttk.Frame(self.note_book)
        self.mf_employees = ttk.Frame(self.employees)

        self.employees_works()

    def employees_works(self):
        self.note_book.add(self.employees, text='Employees')
        self.mf_employees.grid(column=0, row=0, sticky='NESW')
