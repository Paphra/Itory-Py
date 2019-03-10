"""
Displays all the items in the store
"""
from data.works.check import check_rows
from ui.structures.table import Table


class ItemsAll:
    """
    Class that displays the items in the store
    """

    def __init__(self):

        _msg_empty = 'No Items Found!'
        self._return = {'name': _msg_empty, 'type': '',
                        'qty': 0, 'sell_unit': 0}
        self.titles_list = [{'text': 'Item Name', 'width': 27, 'type': 'l'},
                            {'text': 'Item Type', 'width': 23, 'type': 'l'},
                            {'text': 'Quantity', 'width': 10, 'type': 'l'},
                            {'text': 'Unit Price', 'width': 10, 'type': 'l'}]
        self._padx = 4
        self._pady = 2

        self.row_keys = ['name', 'type', 'qty', 'sell_unit']
        self.table = Table(self.f_items_list, titles=self.titles_list,
                           width=500, height=390, _keys_=self.row_keys)

        self.all_items_works()

    def all_items_works(self):
        """
        :return: None
        """
        self.fill_list(self.items_inst.get_all())

    def fill_list(self, items_list):
        """
        :param items_list:
        :return:
        """
        self.table.add_rows(
            check_rows(items_list, self.titles_list, self.row_keys))
