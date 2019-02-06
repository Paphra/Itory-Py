"""Module for Sales records model."""

from datetime import datetime as dt

from .db_connection import Conn


class Sales:
    """Sales model class."""

    def __init__(self):
        """Initialize the list and then fetch records."""
        self.all_sales = []
        db_con = Conn()
        self.collection = db_con.get_collection('col_sales')
        self.db_fetch()

    def db_fetch(self):
        """Fetch db records."""
        self.all_sales = []
        _sales = self.collection.find({}).sort('sale_date', -1)
        for sale in _sales:
            self.all_sales.append(sale)

    def add_sale(self, sale):
        """Add a sale document to the collection and re-fetch"""
        sale['_id'] = dt.now()
        self.collection.insert_one(sale)
        self.db_fetch()

    def delete_sale(self, sale):
        _date = sale['sale_date']
        _query = {'sale_date': _date}
        self.collection.delete_one(_query)
        self.db_fetch()

    def get_all(self):
        return self.all_sales
