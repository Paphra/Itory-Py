
from tkinter import Menu

class Mview():

    def __init__(self, mb, uimain, s_bar, root):
        self.m_b = mb
        self.sb = s_bar
        self.rt = root
        self.uim = uimain
        self.m_view = Menu(self.m_b)

        self.m_view_w()

    def m_view_w(self):
        self.m_view.add_command(label='Home', command=self._vhome)
        self.m_view.add_command(label='Items', command=self._vitems)
        self.m_view.add_command(label='Sales', command=self._vsales)
        self.m_view.add_command(label='Purchases', command=self._vpurchases)
        self.m_view.add_command(label='Accounts', command=self._vaccounts)
        self.m_view.add_command(label='Graphs', command=self._vgraphs)
        self.m_view.add_command(label='Management', command=self._vmanagement)

        self.m_b.add_cascade(label='View', menu=self.m_view)

    def _vhome(self, event=None):
        self.sel_tab(0)
    
    def _vitems(self, event=None):
        self.sel_tab(1)

    def _vsales(self):
        self.sel_tab(2)

    def _vpurchases(self):
        self.sel_tab(3)

    def _vaccounts(self):
        self.sel_tab(4)

    def _vgraphs(self):
        self.sel_tab(5)

    def _vmanagement(self):
        self.sel_tab(6)
    
    def sel_tab(self, index):
        self.uim.ntbk.select_tab(index)
