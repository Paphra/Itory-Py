class Purchases:

    def __init__(self):
        self.all_purchases = []
        self.fetch_db_purchases()

    def fetch_db_purchases(self):
        pass

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

    def get_purchases(self):
        return self.all_purchases
