"""App module.
   It initializes the entire Application"""

import tkinter as tk

from src.ui.menu_bar.mb_main import MBmain
from src.ui.ui_main.s_bar import Sbar
from src.ui.ui_main.ui import UImain


class App:
    """App class, to be instantiated under the main running of the module."""

    def __init__(self):
        """Initializes the class"""
        self.root = tk.Tk()
        self.sb = Sbar(self.root)
        self.uim = UImain(self.root)
        self.mb = MBmain(self.uim, self.sb, self.root)

        self.root_w()

    def root_w(self):
        """Creates the root."""
        self.root.title("Itory Business Operator")
        self.root['width'] = 800
        self.root['height'] = 600
        self.root.resizable(0, 0)

        self.root.iconbitmap(r'C:/Users/Paphra/AppData/Local/Programs/Python/Python37-32/DLLs/pyc.ico')


if __name__ == '__main__':
    i_app = App()
    i_app.root.mainloop()
