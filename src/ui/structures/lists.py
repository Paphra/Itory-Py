import tkinter as tk


class Lists:

    def __init__(self):
        self.list_box = tk.Listbox(self.master)


class ScrollListBox(Lists):

    def __init__(self, master: any, width: int = None, height: int = None):
        self.master = master
        Lists.__init__(self)

        self._width = width
        if width is None:
            self._width = 30

        self._height = height
        if height is None:
            self._height = 15

        self.y = tk.Scrollbar(self.master, orient='vertical')
        self.x = tk.Scrollbar(self.master, orient='horizontal')

        self.list_box_works()

    def new(self, master: any, width: int = None, height: int = None):
        self.__init__(master, width, height)
        return self.get()

    def list_box_works(self):
        self.list_box.grid(column=0, row=0, sticky='NESW', padx=5, pady=5)
        self.y.grid(column=1, row=0, sticky='NS')
        self.x.grid(column=0, row=1, sticky='EW')

        self.list_box.configure(xscrollcommand=self.x.set,
                                yscrollcommand=self.y.set,
                                height=self._height, width=self._width)

        self.x['command'] = self.list_box.xview
        self.y['command'] = self.list_box.yview

    def get(self):
        return self.list_box
