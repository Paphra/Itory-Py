
import tkinter as tk
from src.ui.menu_bar.mb_main import MBmain
from src.ui.ui_main.ui import UImain
from src.ui.ui_main.s_bar import Sbar


class App:

    def __init__(self):
        self.root = tk.Tk()
        self.sb = Sbar(self.root)
        self.uim = UImain(self.root)
        self.mb = MBmain(self.uim, self.sb, self.root)

        self.root_w()

    def root_w(self):
        self.root.title("Itory Business Operator")
        self.root['width'] = 800
        self.root['height'] = 600
        self.root.resizable(0, 0)
        self.root.iconbitmap(r'C:/Users/Paphra/AppData/Local/Programs/Python/Python37-32/DLLs/pyc.ico')


if __name__ == '__main__':
    i_app = App()
    i_app.root.mainloop()
