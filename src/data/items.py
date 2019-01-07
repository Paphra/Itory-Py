
from random import randint as rdi
import mysql.connector as mysql


class Items:

    def __init__(self):
        self.all_items = []

        self.fetch_db_items()

    def get_all_items(self):
        return self.all_items

    def fetch_db_items(self):
        self.delete_all_items()

        # this is just the mock items in the list but it shall be the items from the database
        for i in range(40):
            item = {'serial': str(rdi(0, 9)) + str(rdi(0, 9)) +
                    str(rdi(0, 9)) + str(rdi(0, 9)) + str(rdi(0, 9)),
                    'name': "Item no. " + str(i + 1),
                    'qty': rdi(1, 31),
                    'type': 'Automatic ' + str(i + 1),
                    'sell_unit': rdi(1, 30) * 1000,
                    'buy_unit': ((rdi(1, 30) * 1000) - 500)}
            self.add_full_item(item)

    def add_item_with_details(self, serial, name, _type, qty, sell_unit, buy_unit):
        item = {'serial': serial,
                'name': name,
                'type': _type,
                'qty': qty,
                'sell_unit': sell_unit,
                'buy_unit': buy_unit}
        self.add_full_item(item)

    def add_full_item(self, item=None):
        self.all_items.append(item)

    def get_item(self, name):
        for item in self.all_items:
            if item['name'] == name:
                return item

    def delete_item_given_name(self, name):
        for item in self.all_items:
            if item['name'] == name:
                self.all_items.remove(item)

    def delete_item_given_item(self, item):
        for _item in self.all_items:
            if item == _item:
                self.all_items.remove(_item)

    def delete_all_items(self):
        self.all_items[:] = []

    def edit_qty_given_name(self, name, new_qty):
        for item in self.all_items:
            if item['name'] == name:
                item['qty'] = new_qty

    def edit_unit_given_name(self, name, new_sell_unit):
        for item in self.all_items:
            if item['name'] == name:
                item['sell_unit'] = new_sell_unit

    def edit_buy_unit_given_name(self, name, new_buy_unit):
        for item in self.all_items:
            if item['name'] == name:
                item['buy_unit'] = new_buy_unit

    def edit_buy_unit_given_item(self, item_, new_buy_unit):
        for item in self.all_items:
            if item == item_:
                item['buy_unit'] = new_buy_unit

    def edit_qty_given_item(self, item, new_qty):
        for _item in self.all_items:
            if item == _item:
                _item['qty'] = new_qty

    def edit_unit_given_item(self, item, new_sell_unit):
        for _item in self.all_items:
            if _item == item:
                _item['sell_unit'] = new_sell_unit
