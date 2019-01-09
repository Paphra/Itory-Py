"""
Displays all the items in the store
"""
from src.data.works import check
from src.ui.structures.table import Table


class ItemsAll:
    """
    Class that displays the items in the store
    """

    def __init__(self):
        self._padx = 4
        self._pady = 2
        self.table = Table(master=self.f_items_list)

        self.row_keys = ['name', 'type', 'qty', 'sell_unit']

        self.titles_works()
        self.all_items_works()

    def titles_works(self):
        """

        :return:
        """
        self.titles_list = [{'text': 'Item Name', 'width': 19},
                            {'text': 'Item Type', 'width': 15},
                            {'text': 'Quantity', 'width': 8},
                            {'text': 'Unit Price', 'width': 9}]
        self.table.create(self.titles_list, width=500, height=360)

    def all_items_works(self):
        """

        :return:
        """
        _msg_empty = 'No Items Found!'
        self._return = {'name': _msg_empty, 'type': '',
                        'qty': 0, 'sell_unit': 0}
        _items = check.if_empty(self.all_items_list, self._return)
        self.table.add_rows(rows_list=_items,
                            _keys_=self.row_keys)

    def fill_list(self, items_list: list):
        """

        :param items_list:
        :return:
        """
        _items = check.if_empty(items_list, self._return)
        self.table.add_rows(rows_list=_items,
                            _keys_=self.row_keys)
