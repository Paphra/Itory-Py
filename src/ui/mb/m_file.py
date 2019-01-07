from tkinter import Menu

class Mfile():

    def __init__(self, root, mb):
        self.root = root
        self.mb = mb
        self.m_f = Menu(self.mb, tearoff=0)

        self.f_w()

    def f_w(self):
        self.m_f.add_command(label='Export', command=self._export)
        self.m_f.add_separator()
        self.m_f.add_command(label='Exit', command=self._exit)

        self.mb.add_cascade(menu=self.m_f, label='File')

    def _export(self):
        pass

    def _exit(self):
        self.root.quit()
        self.root.destroy()
        exit()
