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
        for i in range(30):
            self.mock_rows.append({
                'col1': 'value of col 1 row ' + str(i + 1),
                'col2': 'value of col 2 row ' + str(i + 1),
                'col3': 'value of col 3 row ' + str(i + 1),
                'col4': 'value of col 4 row ' + str(i + 1)}, )

        self.list_canvas = tk.Canvas(self.host)

    def create(self, titles: list = None, width: int = None,
               height: int = None):
        """
        This function creates the actual table structure
        :param titles: The titles of the table to put on the top of the table
        :param width: integer indicating the width
        :param height: integer indicating the height
        :return: None
        """
        self._width = width
        if self._width is None: self._width = 200
        self._height = height
        if self._height is None: self._height = 300

        self.titles = titles
        if self.titles is None:
            self.titles = [
                {'text': 'Column 1', 'width': 15},
                {'text': 'Column 2', 'width': 15},
                {'text': 'Column 3', 'width': 15},
                {'text': 'Column 4', 'width': 15}
            ]

        self.host.grid(column=0, row=0, sticky='NESW')

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
                                   width=self._width,
                                   height=self._height)

        self.v_scr.grid(column=(self.cols_ws - 1), row=1, sticky='NS', rowspan=3)
        self.h_scr.grid(column=0, row=4, sticky='WE', columnspan=(self.cols_ws - 1))

        self.v_scr['command'] = self.list_canvas.yview
        self.h_scr['command'] = self.list_canvas.xview

        self.rows_list = None
        self._keys_ = None

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

    def _check_rows(self):
        if not self.rows_list:
            self.no_rows = {}
            for t in self.titles:
                if self.titles.index(t) == 0:
                    self.no_rows[self._keys_[0]] = 'Nothing is Found!'
                else:
                    self.no_rows[self._keys_[self.titles.index(t)]] = ''

    def add_rows(self, rows_list: list = None, _keys_: list = None):
        if self.rows_list is None and self._keys_ is None:
            self.rows_list = rows_list
            self._keys_ = _keys_
            if rows_list is None:
                self.rows_list = self.mock_rows
            if self._keys_ is None: self._keys_ = ['col1', 'col2', 'col3', 'col4']
            self._check_rows()

        for w in self.list_canvas.winfo_children():
            w.destroy()
            del w

        num_rows = len(self.rows_list)
        scr_v = num_rows * 27
        scr_h = 0

        # for title in self.titles
        #     scr_h = scr_h + title['width']

        self.list_canvas['scrollregion'] = (0, 0, scr_h, scr_v)

        self.y_cord = 0
        for i in range(len(self.rows_list)):
            n_i = i + 1
            llb = 'frame' + str(i)
            llb = ttk.Frame(self.list_canvas)

            lb_list = []
            lb_sn = ttk.Label(llb, text=str(n_i), width=4)
            lb_list.append(lb_sn)
            for key in self._keys_:
                lb = ttk.Label(llb, text=str(self.rows_list[i][key]),
                               width=self.titles[self._keys_
                               .index(key)]['width'])
                lb_list.append(lb)

            self._sep_work(llb, lb_list)

            sep11 = ttk.Separator(llb, orient='horizontal')
            sep11.grid(column=0, row=2, sticky='WE', columnspan=self.cols_ws)

            if n_i > 1: self.y_cord = self.y_cord + 26

            self.list_canvas.create_window(-1, self.y_cord, window=llb,
                                           anchor=tk.NW)

            for ww in llb.winfo_children():
                ww.bind('<ButtonRelease-1>', self._click)

    def add_row(self, row_data: dict):
        self.rows_list.append(row_data)
        self.add_rows()

    def _click(self, event):
        self.selected_w = None
        self.selected_w_text = None

        self.parent_name = event.widget.winfo_parent()
        self._selection()

    def _selection(self):
        self.sel_ind = 0
        counts = 0
        for win_ in self.list_canvas.winfo_children():
            w_name = win_.winfo_name()
            if str(w_name) in str(self.parent_name):
                self._select(win_)

                self.sel_ind = counts

            else:
                win_.configure(relief='', borderwidth=0)
                self._shade(win_.winfo_children())

            counts = counts + 1

    def _select(self, widget):
        win_ = widget
        win_.configure(relief='sunken', borderwidth=1)
        w_ch = win_.winfo_children()
        self.selected_w = win_
        self.selected_w_text = w_ch[1]['text']
        self._shade(w_ch, 'grey')

    def _select_new_after_delete(self):
        counts = 0
        list_ = self.list_canvas.winfo_children()
        for win_ in list_:
            if counts == len(list_):
                self.selected_w = None
                self.selected_w_text = None
                break
            if counts == self.sel_ind:
                self._select(win_)

                self.sel_ind = counts
            counts = counts + 1

    def _shade(self, wl: list, color: str = None):
        if color is None: color = ''
        for w in wl:
            if isinstance(w, type(ttk.Label())):
                w['background'] = color

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

            for row in self.rows_list:
                if row[self._keys_[0]] == self.selected_w_text:
                    self.rows_list.remove(row)
            self.selected_w.destroy()

            self.add_rows()
            self._select_new_after_delete()
            return self.selected_w_text
        return None

    def get_selected(self):
        return self.selected_w_text
