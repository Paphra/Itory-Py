import tkinter as tk
from tkinter import ttk


class Contacts:

    def __init__(self):
        self.contacts = ttk.Frame(self.note_book)
        self.mf_contacts = ttk.Frame(self.contacts)

        self.contacts_works()

    def contacts_works(self):
        self.note_book.add(self.contacts, text='Contacts')
        self.mf_contacts.grid(column=0, row=0, sticky='NESW')
