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
        self.fetch_db_sales()
        self.mock_()

    def fetch_db_sales(self):
        """
        Work on fetching the DD records for sales
        :return: None
        """
        self.all_sales = []

    def mock_(self):
        """
        Mocking the sales
        :return: None
        """
        def _w():
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
                self.add_sale_given_sale(sale)
        _w()

    def add_sale_given_sale(self, sale: dict):
        """
        Add A sale when given a full sale with the details
        :param sale: dict with all the details for the sale
        :return: None
        """
        self.all_sales.append(sale)

    def add_sale_given_details(self, cus_name: str, cus_contact: str,
                               amo_pd: int, bal: int, items: list,
                               _date: str):
        """
        Add a sale when given details of that sale
        :param cus_name: string of the name of the customer
        :param cus_contact: string of the contact of the customer: tel and email with , sep
        :param amo_pd: integer of for the amount paid
        :param bal: integer for the balance not paid by the customer
        :param items: list of the items sold
        :param _date: string of the date: year-month-day|hour:minute:seconds
        :return: None
        """
        sale = {
                'customer_name': cus_nm,
                'customer_contact': cus_contact,
                'amount_paid': amo_pd,
                'balance': bal,
                'items': items,
                'sale_date': _date
        }
        self.all_sales.append(sale)

    def delete_sale_given_sale(self, sale: dict):
        """
        Delete a given sale
        :param sale: dictionary of the sale details to be deleted
        :return: None
        """
        self.all_sales.remove(sale)

    def delete_sale_given_date(self, date: str):
        """
        Delete a given sale based on the date given
        :param date: string of the date of the sale to be deleted
        2019-01-09|00:00:00
        :return: None
        """
        for sale in self.all_sales:
            if sale['sale_date'] == date:
                self.all_sales.remove(sale)

    def get_all(self):
        """
        Get all the sales in a list
        :return: list of dictionaries of the sales
        """
        return self.all_sales
