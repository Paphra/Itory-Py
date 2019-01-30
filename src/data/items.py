
from random import randint as rdi


class Items:

    def __init__(self):
        self.all_items = []

        self.db_fetch()

    def get_all(self):
        return self.all_items

    def db_fetch(self):
        self.delete_all()

        # this is just the mock items in the list but it shall be the items from the database
        for i in range(40):
            item = {'serial': str(rdi(0, 9)) + str(rdi(0, 9)) +
                    str(rdi(0, 9)) + str(rdi(0, 9)) + str(rdi(0, 9)),
                    'name': "Item no. " + str(i + 1),
                    'qty': rdi(1, 31),
                    'type': 'Automatic ' + str(i + 1),
                    'sell_unit': rdi(1, 30) * 1000,
                    'buy_unit': ((rdi(1, 30) * 1000) - 500),
                    'item_date': '2019-01-20|09:20:03'}
            self.add_item(item)

    def add_item(self, item=None):
        self.all_items.append(item)

    def get_item(self, name):
        for item in self.all_items:
            if item['name'] == name:
                return item

    def delete_item(self, item):
        for _item in self.all_items:
            if item == _item:
                self.all_items.remove(_item)

    def delete_all(self):
        self.all_items[:] = []

    def edit_type(self, name, new_type):
        for item in self.all_items:
            if item['name'] == name:
                item['type'] = new_type

    def edit_qty(self, name, new_qty):
        for item in self.all_items:
            if item['name'] == name:
                item['qty'] = new_qty

    def edit_unit(self, name, new_sell_unit):
        for item in self.all_items:
            if item['name'] == name:
                item['sell_unit'] = new_sell_unit

    def edit_buy_unit(self, name, new_buy_unit):
        for item in self.all_items:
            if item['name'] == name:
                item['buy_unit'] = new_buy_unit

    def edit_date(self, name, new_date):
        for item in self.all_items:
            if item['name'] == name:
                item['item_date'] = new_date
