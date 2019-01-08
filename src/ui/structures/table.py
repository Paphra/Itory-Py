"""
This module creates a table form according to the specifications
from the designing developer
"""

import tkinter as tk  # importing tkinter as tk for easy reference
from tkinter import ttk  # importing the themed tkinter module


class Table:
    """
    This class creates the table form as specified by the one designing the
    table
    """

    def __init__(self, master: any):
        """
        Initializes the Table creation
        :param master: the container to hold the table structure
        """
        self.host = ttk.Frame(master=master)
        self.title_pane = ttk.Frame(self.host)
        self._padx = 4
        self._pady = 2
        self.mock_rows = [
            {
                'col1': 'value of col 1 row 1', 'col2': 'value of col 2 row 1',
                'col3': 'value of col 3 row 1', 'col4': 'value of col 4 row 1',
            },
            {
                'col1': 'value of col 1 row 2', 'col2': 'value of col 2 row 2',
                'col3': 'value of col 3 row 2', 'col4': 'value of col 4 row 2',
            },
        ]

        self.list_canvas = tk.Canvas(self.host)

    def create(self, titles: list = None, dimensions: dict = None):
        """
        This function creates the actual table structure
        :param titles: The titles of the table to put on the top of the table
        :param dimensions: A dictionary containing the dimensions of the table
        to be created. It contains the width, height, x and y for canvas location
        :return: None
        """
        self.dims = dimensions
        if self.dims is None:
            self.dims = {
                'x': 285, 'y': 25,
                'width': 400, 'height': 200
            }

        self.titles = titles
        if self.titles is None:
            self.titles = [
                {'text': 'Column 1', 'width': 15},
                {'text': 'Column 2', 'width': 15},
                {'text': 'Column 3', 'width': 15},
                {'text': 'Column 4', 'width': 15}
            ]

        self.host.grid(column=0, row=0, sticky='NESW')
        self.canvas_x = self.dims['x']
        self.canvas_y = self.dims['y']

        self.title_pane.grid(column=0, row=0)
        self.cols = len(self.titles)
        self.cols_ws = (self.cols * 2) + 2

        titles_top = ttk.Separator(self.title_pane, orient='horizontal')
        titles_top.grid(column=0, row=0, sticky='WE', columnspan=self.cols_ws)

        self._titles_works(self.titles)

        titles_btm = ttk.Separator(self.title_pane, orient='horizontal')
        titles_btm.grid(column=0, row=2, sticky='WE', columnspan=self.cols_ws)

        self.v_scr = tk.Scrollbar(self.host, orient='vertical')
        self.h_scr = tk.Scrollbar(self.host, orient='horizontal')

        self.list_canvas.grid(column=0, row=1, sticky='WENS',
                              columnspan=(self.cols_ws - 1))
        self.list_canvas.configure(xscrollcommand=self.h_scr.set,
                                   yscrollcommand=self.v_scr.set,
                                   width=self.dims['width'],
                                   height=self.dims['height'])

        self.v_scr.grid(column=(self.cols_ws - 1), row=1, sticky='NS', rowspan=3)
        self.h_scr.grid(column=0, row=4, sticky='WE', columnspan=(self.cols_ws - 1))

        self.v_scr['command'] = self.list_canvas.yview
        self.h_scr['command'] = self.list_canvas.xview

    def _titles_works(self, titles: list):
        """
        This method works on the titles
        :param titles:
        :return:
        """
        lb_sn = ttk.Label(self.title_pane, text='S/N', width=4)
        lb_list = [lb_sn]

        for title in self.titles:
            t_text = title['text']
            t_width = title['width']
            lb = t_text
            lb = ttk.Label(self.title_pane, text=t_text, width=t_width)
            lb_list.append(lb)

        self._sep_work(cont=self.title_pane, lb_list=lb_list)
        return True

    def add_rows(self, rows_list: list = None, _keys_: list = None):
        self.rows_list = rows_list
        self._keys_ = _keys_
        if self.rows_list is None:
            self.rows_list = self.mock_rows
        if self._keys_ is None: self._keys_ = ['col1', 'col2', 'col3', 'col4']

        for w in self.list_canvas.winfo_children():
            w.destroy()
            del w

        num_rows = len(self.rows_list)
        scr_v = num_rows * 27
        scr_h = 0

        # for title in self.titles
        #     scr_h = scr_h + title['width']

        self.list_canvas['scrollregion'] = (0, 0, scr_h, scr_v)

        for i in range(len(self.rows_list)):
            n_i = i + 1
            llb = 'frame' + str(i)
            llb = ttk.Frame(self.list_canvas)

            lb_list = []
            lb_sn = ttk.Label(llb, text=str(n_i), width=4)
            lb_list.append(lb_sn)
            for key in self._keys_:
                lb = ttk.Label(llb, text=self.rows_list[i][key],
                               width=self.titles[self._keys_.index(key)]['width'])
                lb_list.append(lb)

            self._sep_work(llb, lb_list)

            sep11 = ttk.Separator(llb, orient='horizontal')
            sep11.grid(column=0, row=2, sticky='WE', columnspan=self.cols_ws)

            self.list_canvas.create_window(self.canvas_x, n_i * self.canvas_y,
                                           window=llb)

            for ww in llb.winfo_children():
                ww.bind('<ButtonRelease-1>', self._click)

    def add_row(self, row_data: dict):
        self.rows_list.append(row_data)
        self.add_rows()

    def _click(self, event):
        self.selected_w = None
        self.selected_w_name = None

        p_name = event.widget.winfo_parent()
        for win_ in self.list_canvas.winfo_children():
            w_name = win_.winfo_name()
            if str(w_name) in str(p_name):
                win_.configure(relief='ridge', borderwidth=5)
                w_ch = win_.winfo_children()
                self.selected_w = win_
                self.selected_w_name = w_ch[1]['text']

            else:
                win_.configure(relief='', borderwidth=0)

    def _sep_work(self, cont: any, lb_list: list):
        s_ = 0
        for s in range(len(lb_list) + 1):
            if s > 0:
                s_ = s_ + 2
            sep = 'sep' + str(s) + cont.winfo_name()
            sep = ttk.Separator(cont, orient='vertical')
            sep.grid(column=s_, row=1, sticky='NS')

            if s < len(lb_list):
                lb_list[s].grid(column=(s_ + 1), row=1, sticky='WE',
                                padx=self._padx, pady=self._pady)

    def delete_row(self):
        if self.selected_w is not None:

            for item in self.rows_list:
                if item['name'] == self.selected_w_name:
                    self.rows_list.remove(item)
            self.selected_w.destroy()

            self.add_rows()

            return self.selected_w_name
        return None
