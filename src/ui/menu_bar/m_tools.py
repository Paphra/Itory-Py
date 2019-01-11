from tkinter import Menu


class Mtools:

    def __init__(self, mb):
        self.m_b = mb
        self.m_tools = Menu(self.m_b, tearoff=0)

        self.m_tools_w()

    def m_tools_w(self):
        self.m_tools.add_command(label='Print', command=self._print)
        self.m_b.add_cascade(label='Tools', menu=self.m_tools)

    def _print(self):
        pass
