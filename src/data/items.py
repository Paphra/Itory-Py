""" Items model module.
    Structuring the way how items are fetched from the
    database to the application."""

from datetime import datetime as dt

from .db_connection import Conn


class Items:
    """Items model class."""

    def __init__(self):
        """Initialize the class."""
        self.all_items = []
        db_con = Conn()
        self.collection = db_con.get_collection('col_items')
        self.db_fetch()

    def get_all(self):
        return self.all_items

    def db_fetch(self):
        self.all_items = []
        for item in self.collection.find({}).sort('name'):
            self.all_items.append(item)

    def add_item(self, item):
        item['_id'] = dt.now()
        self.collection.insert_one(item)
        self.db_fetch()

    def get_item(self, name):
        for item in self.all_items:
            if item['name'] == name:
                return item

    def delete_item(self, item):
        _query = {'name': item['name']}
        self.collection.delete_one(_query)

    def delete_all(self):
        self.collection.delete_many({})
        self.db_fetch()

    def edit_type(self, name, new_type):
        _query = {'name': name}
        _new_value = {'$set': {'type': new_type}}
        self.collection.update_one(_query, _new_value)
        self.db_fetch()

    def edit_qty(self, name, new_qty):
        _query = {'name': name}
        _new_value = {'$set': {'qty': new_qty}}
        self.collection.update_one(_query, _new_value)
        self.db_fetch()

    def edit_unit(self, name, new_sell_unit):
        _query = {'name': name}
        _new_value = {'$set': {'sell_unit': new_sell_unit}}
        self.collection.update_one(_query, _new_value)
        self.db_fetch()

    def edit_buy_unit(self, name, new_buy_unit):
        _query = {'name': name}
        _new_value = {'$set': {'buy_unit': new_buy_unit}}
        self.collection.update_one(_query, _new_value)
        self.db_fetch()

    def edit_date(self, name, new_date):
        _query = {'name': name}
        _new_value = {'$set': {'item_date': new_date}}
        self.collection.update_one(_query, _new_value)
        self.db_fetch()
