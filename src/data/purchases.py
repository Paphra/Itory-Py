from random import randint as rdi


class Purchases:

    def __init__(self):
        self.all_purchases = []
        self.fetch_db_purchases()
        self.mock_()

    def fetch_db_purchases(self):

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
                'details': str(rdi(1, 30)) + '-Item No. ' + str(rdi(1, 40)) +
                           str(rdi(1, 30)) + '-Item No. ' + str(rdi(1, 40)) +
                           str(rdi(1, 30)) + '-Item No. ' + str(rdi(1, 40)),
                'purchase_date': dt_str}
            self.add_pur_given_pur(pur)

    def add_pur_given_pur(self, pur_: dict):
        self.all_purchases.append(pur_)

    def add_pur_given_details(self, date_: str, item: str, details: str,
                              amount: int):
        _pur = {'purchase_date': date_,
                'item': item,
                'details': details,
                'amount': amount}
        self.all_purchases.append(_pur)

    def delete_pur_given_pur(self, pur_: dict):
        self.all_purchases.remove(pur_)

    def delete_pur_given_date(self, date_: str):
        for _pur in self.all_purchases:
            if _pur['purchase_date'] == date_:
                self.all_purchases.remove(_pur)

    def get_all_purchases(self):
        return self.all_purchases
