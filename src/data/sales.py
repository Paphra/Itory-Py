
import mysql.connector as mysql

"""
The Class ..
"""


class Sales:
    """
    This Class ...
    """

    def __init__(self):
        self.all_sales = []
        self.fetch_db_sales()

    def fetch_db_sales(self):
        pass

    def add_sale_given_sale(self, sale):
        self.all_sales.append(sale)

    def add_sale_given_details(self, cus_nm, cus_contact,
                               amo_pd, bal, items, _date):
        sale = {
            'customer_name': cus_nm,
            'customer_contact': cus_contact,
            'amount_paid': amo_pd,
            'balance': bal,
            'items': items,
            'sale_date': _date
        }
        self.all_sales.append(sale)

    def delete_sale_given_sale(self, sale):
        self.all_sales.delete(sale)

    def delete_sale_given_date(self, date):
        for sale in self.all_sales:
            if sale['sale_date'] == date:
                self.all_sales.delete(sale)

    def get_all_sales(self):
        return self.all_sales
