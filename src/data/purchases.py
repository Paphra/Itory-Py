from random import randint as rdi
from threading import Thread


class Purchases:

    def __init__(self):
        self.all_purchases = []
        self.db_fetch()
        self.mock_()

    def db_fetch(self):
        self.all_purchases = []

    def mock_(self):
        """
        Mocking the sales
        :return: None
        """
        for i in range(400):
            dt_str = str(20) + str(rdi(17, 19)) + '-' + str(rdi(1, 12)).zfill(2) + \
                     '-' + str(rdi(1, 30)).zfill(2) + '|' + str(rdi(0, 24)).zfill(2) + \
                     ':' + str(rdi(0, 61)).zfill(2) + ':' + str(rdi(0, 61)).zfill(2)

            pur = {
                'item': 'Item No. ' + str(rdi(1, 30)).zfill(2),
                'amount': str(rdi(2, 1000) * 1000),
                'details': [str(rdi(1, 30)) + '-Item No. ' + str(rdi(1, 40)),
                            str(rdi(1, 30)) + '-Item No. ' + str(rdi(1, 40)),
                            str(rdi(1, 30)) + '-Item No. ' + str(rdi(1, 40))],
                'purchase_date': dt_str}
            self.add_purchase(pur)

    def add_purchase(self, pur_):
        self.all_purchases.append(pur_)

    def delete_purchase(self, pur_):
        self.all_purchases.remove(pur_)

    def get_all(self):
        return self.all_purchases
