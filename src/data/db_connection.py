""" Connection module.
    Connecting to the Database for Data Fetching."""

import pymongo


class Conn:

    def __init__(self):
        self.db = None
        self._client = None

    def get_collection(self, col_name):
        """Connect to the database.
        :type: col_name: str collection name
        :returns: collection"""
        self._client = pymongo.MongoClient(host='mongodb://localhost',
                                           port=27017)
        self.db = self._client['db_itory']
        return self.db[col_name]
