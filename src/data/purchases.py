""" Purchases model module
    Structuring the way how Purchases Data is fecthed from the database
    for the application usage."""

from .db_connection import Conn


class Purchases:

    def __init__(self):
        self.all_purchases = []
        db_con = Conn()
        self.collection = db_con.get_collection('col_purchases')
        self.db_fetch()

        self.work = Work(self.collection, self.db_fetch)

    def db_fetch(self):
        self.all_purchases[:] = []
        for purchase in self.collection.find({}).sort('purchase_date', -1):
            self.all_purchases.append(purchase)

    def get_all(self):
        return self.all_purchases

class Work:
    """docstring for Work."""
    def __init__(self, collection, db_fetch):
        self.collection = collection
        self.db_fetch = db_fetch

    def add(self, item):
        self.collection.insert_one(item)
        self.db_fetch()

    def delete(self, item, key):
        _query = {key: item[key]}
        self.collection.delete_one(_query)
        self.db_fetch()

    def edit(self, item, pri_key, key, value):
        _query = {pri_key: item[pri_key]}
        _new_value = {'$set': {key: value}}
        self.collection.update_one(_query, _new_value)
        self.db_fetch()
