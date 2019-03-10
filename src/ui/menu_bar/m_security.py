from tkinter import Menu


class Msecurity:

    def __init__(self, mb, uim):
        self.m_b = mb
        self.uim = uim
        self.m_security = Menu(self.m_b, tearoff=0)

        self.m_security_w()

    def m_security_w(self):
        self.m_security.add_command(label="Login As",
                                    command=self._login)
        self.m_b.add_cascade(label='Security', menu=self.m_security)

    def _login(self):
        self.uim.ntbk.select_tab(6)
