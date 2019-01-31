from tkinter import ttk

from src.ui.ui_main.tabs.commons.main import Main


class TDrawings:

    def __init__(self, nt_book, s_bar, insts):
        self.ntb = nt_book
        self.sb = s_bar
        self.draw_inst = insts['accounts'].drawings
        self.t_drawings = ttk.Frame(self.ntb)
        self.mf_drawings = ttk.Frame(self.t_drawings)
        self.drawings_main = Main(self.mf_drawings, self.sb, self.draw_inst,
                                  'Drawings')

        self.t_work()

    def t_work(self):
        self.ntb.add(self.t_drawings, text='Drawings')
        self.mf_drawings.grid(column=0, row=0, padx=10, pady=10, sticky='NESW')
        self.mf_drawings.configure(width=750, height=500)
