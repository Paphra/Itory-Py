import tkinter as tk


class Lists:

    def __init__(self, container):
        self.hoste = container
        self.lb = tk.Listbox(self.hoste)


class ScrollList(Lists):

    def __init__(self, cont):
        self.hostp = cont
        Lists.__init__(self, self.hostp)

        self.y = tk.Scrollbar(self.hostp, orient='vertical')
        self.x = tk.Scrollbar(self.hostp, orient='horizontal')

        self.w()

    def w(self):
        self.lb.grid(column=0, row=0, sticky='NESW', padx=5, pady=5)
        self.y.grid(column=1, row=0, sticky='NS')
        self.x.grid(column=0, row=1, sticky='EW')

        self.lb.configure(xscrollcommand=self.x.set, yscrollcommand=self.y.set,
                          height=13, width=20)

        self.x['command'] = self.lb.xview
        self.y['command'] = self.lb.yview

    def get_sl(self):
        return self.lb
