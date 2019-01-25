
from tkinter import ttk


class TCreditors:

    def __init__(self, container, s_bar, insts):

        self.host = container
        self.sb = s_bar

        self.t_cred = ttk.Frame(self.host)
        self.mf = ttk.Frame(self.t_cred)

        self._works()

    def _works(self):
        self.host.add(self.t_cred, text='Creditors')
        self.mf.grid(column=0, row=0, sticky='NESW')
