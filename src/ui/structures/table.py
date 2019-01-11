"""
This module creates a table form according to the specifications
from the designing developer
"""

import tkinter as tk  # importing tkinter as tk for easy reference
from tkinter import ttk  # importing the themed tkinter module


def _shade(wl_: list, color: str = None):
    """
    Shading a given row when selection occurs
    :param wl_: list of widgets on the row
    :param color: color to be used
    :return: None
    """
    if color is None:
        color = ''
    for _w in wl_:
        if isinstance(_w, type(ttk.Label())):
            _w['background'] = color


def _sep_work(cont: any, lb_list: list):
    """
     Create and Situate separators on a given container between widgets
    :param cont: container widget
    :param lb_list: list of widgets to be separated using the separators
    :return: None
    """
    _col = 0
    for _c in range(len(lb_list) + 1):
        if _c > 0:
            _col = _col + 2
        sep = 'sep' + str(_c) + cont.winfo_name()
        sep = ttk.Separator(cont, orient='vertical')
        sep.grid(column=_col, row=1, sticky='NS')

        if _c < len(lb_list):
            lb_list[_c].grid(column=(_col + 1), row=1, sticky='WE',
                             padx=2, pady=2)


class Table:
    """
    This class creates the table form as specified by the one designing the
    table. A master of any kind is passed in at initialization.
    Then a method called create is called to create the table. This method
    takes arguments: list of dictionaries for the titles with their text,
    width and type of the widget for each row cell.
    e.g {'text': 'Name of something', 'width': 30, 'type': 'l'}
    'l' is for ttk.Label(), 'c' is for ttk.Combobox(), 'e' is for ttk.Entry()
    """

    def __init__(self, master: any):
        """
        Initializes the Table creation
        :param master: the container to hold the table structure
        """
        self.host = ttk.Frame(master=master)
        self.title_pane = ttk.Frame(self.host)
        # the main canvas that is scrollable
        self.list_canvas = tk.Canvas(self.host)

        # instance variables
        self.sel_ind = None
        self.col_span = None
        self.titles = None
        self.rows_list = None
        self._keys_ = None
        self.selected_w = None
        self.mock_rows = []
        self.work_on_mock()

    def work_on_mock(self):
        """
        Filling the mock rows with mock data
        :return: None
        """
        for i in range(30):
            self.mock_rows.append({
                    'col1': 'value of col 1 row ' + str(i + 1),
                    'col2': 'value of col 2 row ' + str(i + 1),
                    'col3': 'value of col 3 row ' + str(i + 1),
                    'col4': 'value of col 4 row ' + str(i + 1)})

    def create(self, titles: list = None, width: int = None,
               height: int = None):
        """
        This function creates the actual table structure
        :param titles: The titles of the table to put on the top of the table
        :param width: integer indicating the width of the table
        :param height: integer indicating the height of the table
        :return: None
        """
        _width = width
        if _width is None:
            _width = 200
        _height = height
        if _height is None:
            _height = 300

        self.titles = titles
        # if the titles list is None, then a mock is created
        if self.titles is None:
            self.titles = [
                    {'text': 'Column 1', 'width': 15, 'type': 'l'},
                    {'text': 'Column 2', 'width': 15, 'type': 'l'},
                    {'text': 'Column 3', 'width': 15, 'type': 'l'},
                    {'text': 'Column 4', 'width': 15, 'type': 'l'}]

        # situating the host on the master
        self.host.grid(column=0, row=0, sticky='NSE')

        # situating the title_pane on the host/container
        self.title_pane.grid(column=0, row=0)
        cols = len(self.titles)
        self.col_span = (cols * 2) + 2

        # adding a separator at the top of the title pane
        titles_top = ttk.Separator(self.title_pane, orient='horizontal')
        titles_top.grid(column=0, row=0, sticky='WE', columnspan=self.col_span)

        # working on the titles
        self._titles_works()

        # adding 2 separators at the bottom of the title pane
        for i in range(2, 4):
            t_btm = 'titles_btm' + str(i)
            t_btm = ttk.Separator(self.title_pane, orient='horizontal')
            t_btm.grid(column=0, row=i, sticky='WE', columnspan=self.col_span)

        # scroll bars for te vertical and horizontal
        v_scr = tk.Scrollbar(self.host, orient='vertical')

        # situating the canvas and setting it up to be scrollable
        self.list_canvas.grid(column=0, row=1, sticky='WENS',
                              columnspan=(self.col_span - 1))
        self.list_canvas.configure(yscrollcommand=v_scr.set,
                                   width=_width,
                                   height=_height)

        v_scr.grid(column=(self.col_span - 1), row=1, sticky='NS', rowspan=3)

        v_scr['command'] = self.list_canvas.yview

    def _titles_works(self):
        """
        This method works on the titles. Positions the and sets the column widths
        :return: None
        """
        lb_list = [ttk.Label(self.title_pane, text='S/N', width=4)]

        for title in self.titles:
            _lb = title['text']
            _lb = ttk.Label(self.title_pane, text=title['text'],
                            width=title['width'])
            lb_list.append(_lb)

        _sep_work(cont=self.title_pane, lb_list=lb_list)
        return True

    def add_rows(self, rows_list: list = None, _keys_: list = None):
        """
        Add given rows on to the canvas of the table
        :param rows_list: list of rows[dictionaries] to be placed on the canvas
        :param _keys_: keys for the dictionaries contained in the rows_list
        :return: None
        """
        if rows_list is not None and _keys_ is not None:
            self.rows_list = rows_list
            self._keys_ = _keys_
        if self.rows_list is None:
            self.rows_list = self.mock_rows
        if self._keys_ is None:
            self._keys_ = ['col1', 'col2', 'col3', 'col4']

        for _w in self.list_canvas.winfo_children():
            _w.destroy()
            del _w

        num_rows = len(self.rows_list)
        scr_v = num_rows * 26

        self.list_canvas['scrollregion'] = (0, 0, 0, scr_v)

        y_cord = 0
        for i in range(len(self.rows_list)):
            _llb = 'frame' + str(i)
            _llb = ttk.Frame(self.list_canvas)

            lb_list = []
            lb_sn = ttk.Label(_llb, text=str(i + 1), width=4)
            lb_list.append(lb_sn)
            self._make_row_widgets(_llb, lb_list, i)

            _sep_work(_llb, lb_list)

            sep11 = ttk.Separator(_llb, orient='horizontal')
            sep11.grid(column=0, row=2, sticky='WE', columnspan=self.col_span)

            if i > 0:
                y_cord = y_cord + 26

            self.list_canvas.create_window(-1, y_cord, window=_llb,
                                           anchor=tk.NW)

            for _ww in _llb.winfo_children():
                _ww.bind('<ButtonRelease-1>', self._click)

    def _make_row_widgets(self, _llb, lb_list, _i):
        """
        Make the widgets for the row
        :param _llb: label, the row main widget
        :param lb_list: list of widgets. This is where the widgets are put
        :return: None
        """
        for key in self._keys_:
            _text = self.rows_list[_i][key]
            _type = self.titles[self._keys_.index(key)]['type']
            _width = self.titles[self._keys_.index(key)]['width']
            _w = None
            if self.titles[self._keys_.index(key)]['type'] == 'l':
                _w = ttk.Label(_llb, text=_text, width=_width)
            elif _type == 'c':
                _w = ttk.Combobox(_llb, values=_text, width=(_width - 2),
                                  state='readonly')
                if len(_text) > 0:
                    _w.current(0)
            elif _type == 'e':
                _v = tk.StringVar(value=_text)
                _w = ttk.Entry(_llb, textvariable=_v, width=_width,
                               state='readonly')

            lb_list.append(_w)

    def add_row(self, row_data: dict):
        """
        Adds a row of data tot the table
        :param row_data: dictionary of details of the row
        :return: None
        """
        self.rows_list.append(row_data)
        self.add_rows()

    def _click(self, event=None):
        """
        Work on the clicking event on a given row
        :param event: event of button
        :return: None
        """
        self.selected_w = None

        self._selection(event.widget.winfo_parent())

    def _selection(self, parent_name):
        self.sel_ind = 0
        counts = 0
        for win_ in self.list_canvas.winfo_children():
            w_name = win_.winfo_name()
            if str(w_name) in str(parent_name):
                self._select(win_)

                self.sel_ind = counts

            else:
                win_.configure(relief='', borderwidth=0)
                _shade(win_.winfo_children())
            counts = counts + 1

    def _select(self, widget):
        win_ = widget
        win_.configure(relief='sunken', borderwidth=1)
        _wch = win_.winfo_children()
        self.selected_w = win_
        _shade(_wch, 'grey')

    def _select_new_after_delete(self):
        """
        Perform the selection after the deleting action
        :return: None
        """
        counts = 0
        list_ = self.list_canvas.winfo_children()
        for win_ in list_:
            if counts == len(list_):
                self.selected_w = None
                break
            if counts == self.sel_ind:
                self._select(win_)
                self.sel_ind = counts
                break
            counts = counts + 1

    def delete_row(self):
        """
        Delete a selected row
        :return: None
        """
        if self.selected_w is not None:
            _sel_text = self.selected_w.winfo_children()[1]['text']
            for row in self.rows_list:
                if row[self._keys_[0]] == _sel_text:
                    self.rows_list.remove(row)
            self.selected_w.destroy()
            self.add_rows()
            self._select_new_after_delete()
            return _sel_text
        return None

    def get_selected(self):
        """
        Get the the text on the first widget of the selected row
        :return: str
        """
        return self.selected_w.winfo_children()[1]['text']
