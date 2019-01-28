

class Keys:

    def __init__(self):
        self.keys_work()

    def keys_work(self):

        if self.caller == 'Purchases':
            self._use = ['purchase_date', 'item', 'details']
            self._date_key = 'purchase_date'
            self._amo_key = 'amount'

            self._keys = ['purchase_date',
                          'item',
                          'details',
                          'amount']

            self.titles = [{'text': 'Date', 'width': 20, 'type': 'l'},
                           {'text': "Item", 'width': 35, 'type': 'l'},
                           {'text': "Details", 'width': 40, 'type': 'c'},
                           {'text': 'Amount', 'width': 25, 'type': 'l'}]

        elif self.caller == 'Sales':
            self._use = ['sale_date', 'customer_name', 'customer_contact']
            self._date_key = 'sale_date'
            self._amo_key = 'amount_paid'
            self._bal_key = 'balance'

            self._keys = ['sale_date',
                          'customer_name',
                          'customer_contact',
                          'amount_paid',
                          'balance',
                          'items']

            self.titles = [{'text': 'Date', 'width': 20, 'type': 'l'},
                           {'text': "Customer", 'width': 20, 'type': 'l'},
                           {'text': "Contact", 'width': 23, 'type': 'l'},
                           {'text': 'Paid', 'width': 15, 'type': 'l'},
                           {'text': 'Balance', 'width': 15, 'type': 'l'},
                           {'text': 'Items Sold', 'width': 25, 'type': 'c'}]

        elif self.caller == 'Debtors':
            self._use = ['debt_date', 'name', 'tel', 'email']
            self._date_key = 'debt_date'
            self._amo_key = 'balance'
            self._keys = ['debt_date',
                          'name',
                          'tel', 'email', 'details', 'paid', 'balance']
            self.titles = [{'text': 'Date', 'width': 20, 'type': 'l'},
                           {'text': 'Customer', 'width': 20, 'type': 'l'},
                           {'text': 'Tel No.', 'width': 12, 'type': 'l'},
                           {'text': 'Email', 'width': 20, 'type': 'l'},
                           {'text': 'Details', 'width': 20, 'type': 'c'},
                           {'text': 'Paid', 'width': 10, 'type': 'l'},
                           {'text': 'Balance', 'width': 10, 'type': 'l'}]
            self.height = 230
