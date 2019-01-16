"""
Displays all the items in the store
"""
from src.data.works.check import check_rows
from src.ui.structures.table import Table


class ItemsAll:
    """
    Class that displays the items in the store
    """

    def __init__(self):

        _msg_empty = 'No Items Found!'
        self._return = {'name': _msg_empty, 'type': '',
                        'qty': 0, 'sell_unit': 0}
        self.titles_list = [{'text': 'Item Name', 'width': 30, 'type': 'l'},
                            {'text': 'Item Type', 'width': 25, 'type': 'l'},
                            {'text': 'Quantity', 'width': 10, 'type': 'l'},
                            {'text': 'Unit Price', 'width': 10, 'type': 'l'}]
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
        self.table.create(self.titles_list, width=530, height=390)

    def all_items_works(self):
        """
        :return: None
        """
        self.fill_list(self.all_items_list)

    def fill_list(self, items_list: list):
        """
        :param items_list:
        :return:
        """
        self.table.add_rows(
            check_rows(items_list, self.titles_list, self.row_keys),
            _keys_=self.row_keys)
