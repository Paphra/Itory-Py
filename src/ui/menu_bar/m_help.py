from tkinter import Menu


class Mhelp:

    def __init__(self, mb):
        self.m_b = mb
        self.m_help = Menu(self.m_b, tearoff=0)

        self.m_help_w()

    def m_help_w(self):
        self.m_help.add_command(label='Help?', command=self._help)
        self.m_help.add_command(label='About', command=self._about)

        self.m_b.add_cascade(label='Help', menu=self.m_help)

    def _help(self):
        pass

    def _about(self):
        pass
