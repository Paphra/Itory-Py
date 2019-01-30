def _set(txt, w, typ):
    return {'text': txt, 'width': w, 'type': typ}


def _date():
    return _set('Date', 20, 'l')


class Keys:

    def __init__(self):
        self.keys_work()

    def keys_work(self):
        _l = 'l'
        _c = 'c'

        if self.caller == 'Purchases':
            self._use = ['purchase_date', 'item', 'details']
            self._date_key = 'purchase_date'
            self._amo_key = 'amount'

            self._keys = ['purchase_date',
                          'item',
                          'details',
                          'amount']

            self.titles = [_date(), _set("Item", 35, _l),
                           _set("Details", 40, _c), _set('Amount', 25, _l)]

        elif self.caller == 'Sales':
            self._keys = ['sale_date', 'customer_name', 'customer_contact',
                          'amount_paid', 'balance', 'items']
            self._use = self._keys[:3]
            self._date_key = self._keys[0]
            self._amo_key = self._keys[3]
            self._bal_key = self._keys[4]

            self.titles = [_date(), _set("Customer", 20, _l),
                           _set("Contact", 23, _l), _set('Paid', 15, _l),
                           _set('Balance', 15, _l), _set('Items Sold', 25, _c)]

        elif self.caller == 'Debtors':
            self._keys = ['debt_date', 'name', 'tel', 'email', 'details',
                          'paid', 'balance']
            self._use = self._keys[:5]
            self._date_key = self._keys[0]
            self._amo_key = self._keys[-1]

            self.titles = [_date(), _set('Customer', 20, _l),
                           _set('Tel No.', 12, _l), _set('Email', 20, _l),
                           _set('Details', 20, _c), _set('Paid', 10, _l),
                           _set('Balance', 10, _l)]
            self.height = 230

        elif self.caller == 'Expenses':
            self._keys = ['exp_date', 'responsible', 'details', 'amount']
            self._use = self._keys[:3]
            self._date_key = self._keys[0]
            self._amo_key = self._keys[-1]
            self.titles = [_date(), _set('Responsible', 25, _l),
                           _set('Details', 53, _l), _set('Amount', 20, _l)]
            self.height = 250

        elif self.caller == 'Income':
            self._keys = ['income_date', 'from', 'details', 'amount']
            self._use = self._keys[:-1]
            self._amo_key = self._keys[-1]
            self._date_key = self._keys[0]
            self.titles = [_date(), _set('Source', 25, _l),
                           _set('Details', 50, _c), _set('Amount', 20, _l)]
            self.height = 220
