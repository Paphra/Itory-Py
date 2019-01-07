
import tkinter as tk
from tkinter import Menu
from .m_file import Mfile
from .m_view import Mview
from .m_tools import Mtools
from .m_security import Msecurity
from .m_help import Mhelp

class MBmain():

    def __init__(self, uimain, s_bar, root):
        self.rt = root
        self.sb = s_bar
        self.uim = uimain
        self.menu_bar = Menu(self.rt)

        self.m_file = Mfile(self.rt, self.menu_bar)
        self.m_view  = Mview(self.menu_bar, self.uim, self.sb, self.rt)
        self.m_tools  = Mtools(self.menu_bar)
        self.m_security  = Msecurity(self.menu_bar)
        self.m_help  = Mhelp(self.menu_bar)

        self.mb_w()

    def mb_w(self):
        self.rt.config(menu=self.menu_bar)

