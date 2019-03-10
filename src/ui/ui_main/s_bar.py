
import tkinter as tk
from tkinter import ttk


class Sbar:

    def __init__(self, root):
        self.root = root
        self.lf_main = ttk.LabelFrame(self.root)
        self.lb_left = ttk.Label(self.lf_main)
        self.lb_c1 = ttk.Label(self.lf_main)
        self.lb_right = ttk.Label(self.lf_main)

        self.sb_w()

    def sb_w(self):
        self.lf_main.grid(column=0, row=1, sticky='NESW', padx=5)
        self.lf_main.configure(text='Program Status')

        self.lb_left.grid(column=0, row=0, padx=2.5)
        sep1 = ttk.Separator(self.lf_main, orient='vertical')
        sep1.grid(column=1, row=0, sticky='NS')
        self.lb_c1.grid(column=2, row=0, padx=2.5)
        sep2 = ttk.Separator(self.lf_main, orient='vertical')
        sep2.grid(column=2, row=0, sticky='NS')
        self.lb_right.grid(column=4, row=0, padx=2.5,
                           sticky='E')

        lbs = [self.lb_left, self.lb_c1, self.lb_right]
        for lb_i in range(len(lbs)):
            lbs[lb_i].configure(width=35)
