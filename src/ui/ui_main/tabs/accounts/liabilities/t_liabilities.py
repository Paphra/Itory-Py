
from tkinter import ttk
from .creditors.t_creditors import TCreditors
from .drawings.t_drawings import TDrawings


class TLiabilities:

    def __init__(self, container, s_bar, insts):

        self.host = container
        self.sb = s_bar

        self.t_liabs = ttk.Frame(self.host)
        self.mf_ntb = ttk.Notebook(self.t_liabs)

        # tabs
        self.t_drawings = TDrawings(self.mf_ntb, self.sb, insts)
        self.t_creditors = TCreditors(self.mf_ntb, self.sb, insts)

        self._works()

    def _works(self):
        self.host.add(self.t_liabs, text='Liabilities')
        self.mf_ntb.grid(column=0, row=0, sticky='NESW')
