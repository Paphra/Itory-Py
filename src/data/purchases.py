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

    def db_fetch(self):
        self.all_purchases = []
        for purchase in self.collection.find({}).sort('purchase_date', -1):
            self.all_purchases.append(purchase)

    def add_purchase(self, pur_):
        self.collection.insert_one(pur_)
        self.db_fetch()

    def edit_purchase_amount(self, pur_, new_amount):
        _query = {'purchase_date': pur_['purchase_date']}
        _new_value = {'$set': {'amount': new_amount}}
        self.collection.update_one(_query, _new_value)
        self.db_fetch()

    def delete_purchase(self, pur_):
        _query = {'purchase_date': pur_['purchase_date']}
        self.collection.delete_one(_query)
        self.db_fetch()

    def get_all(self):
        return self.all_purchases
