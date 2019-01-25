from tkinter import ttk
from .graph_main import GraphMain


class TGraphs:

    def __init__(self, nt_book, s_bar, insts):
        self.ntb = nt_book
        self.sb = s_bar
        self.t_graphs = ttk.Frame(self.ntb)
        self.mf = ttk.Frame(self.t_graphs)
        self.g_main = GraphMain(self.mf, self.sb, insts=insts)
        self.t_work()

    def t_work(self):
        self.ntb.add(self.t_graphs, text='Graphs')
        self.mf.grid(column=0, row=0, padx=10, pady=10, sticky='NESW')
        self.mf.configure(width=825, height=525)
