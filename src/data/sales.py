"""
The Class ..
"""
from random import randint as rdi
from threading import Thread


class Sales:
    """
    This Class ...
    """

    def __init__(self):
        self.all_sales = []
        self.db_fetch()
        self.mock_()

    def db_fetch(self):
        self.all_sales = []

    def mock_(self):
        for i in range(400):
            dt_str = str(20) + str(rdi(17, 19)) + '-' + str(rdi(1, 12)).zfill(2) + \
                     '-' + str(rdi(1, 30)).zfill(2) + '|' + str(rdi(0, 24)).zfill(2) + \
                     ':' + str(rdi(0, 61)).zfill(2) + ':' + str(rdi(0, 61)).zfill(2)

            sale = {
                'customer_name': 'Customer No. ' + str(rdi(1, 30)).zfill(2),
                'customer_contact': str(rdi(1, 1000000000)).zfill(10),
                'amount_paid': str(rdi(2, 1000) * 1000),
                'balance': str(rdi(0, 20) * 500),
                'items': [str(rdi(1, 30)) + '-Item No. ' + str(rdi(1, 40)),
                          str(rdi(1, 30)) + '-Item No. ' + str(rdi(1, 40)),
                          str(rdi(1, 30)) + '-Item No. ' + str(rdi(1, 40))],
                'sale_date': dt_str}
            self.add_sale(sale)

    def add_sale(self, sale):
        self.all_sales.append(sale)

    def delete_sale(self, sale):
        self.all_sales.remove(sale)

    def get_all(self):
        return self.all_sales
