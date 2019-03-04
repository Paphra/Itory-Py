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

        self.list_of_commons = ['Purchases', 'Expenses', 'Income',
                                'Sales Returns', 'Purchases Returns',
                                'Fixed Assets', 'Drawings', 'Creditors',
                                'Accruals']

        if self.caller == 'Sales':
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

        elif self.caller in self.list_of_commons:
            _k, _name_k, self.name, _d, _h, _tt = 'exp_date', 'responsible', \
                                                  'Person Responsible', _l, \
                                                  250, 220  # expenses catered for
            _w = 50

            if self.caller == 'Drawings':
                _k, _w = 'draw_date', 52
            elif self.caller == 'Purchases':
                _k, _name_k, self.name, _d, _h, _w = 'purchase_date', 'supplier', \
                                                 'Supplier', _c, 290, 55
            elif self.caller == 'Income':
                _k, _name_k, self.name, _d, _h = 'income_date', 'from', \
                                                 'Source', _c, _tt
            elif self.caller == 'Fixed Assets':
                _k, _name_k, self.name, _d, _h = 'fixed_assets_date', 'name', \
                                                 'Asset', _l, _tt
            elif self.caller == 'Sales Returns':
                _k, _name_k, self.name, _d, _h = 'retin_date', 'customer', \
                                                 'Customer', _l, _tt
            elif self.caller == 'Purchases Returns':
                _k, _name_k, self.name, _d, _h = 'retout_date', 'supplier', \
                                                 'Supplier', _l, _tt
            elif self.caller == 'Creditors':
                _k, _name_k, self.name, _d, _h = 'cred_date', 'creditor', \
                                                 'Creditor', _l, _tt
            elif self.caller == 'Accruals':
                _k, _name_k, self.name, _d, _h = 'accr_date', 'accruer', \
                                                 'Accruer', _l, _tt
            else:
                _w = 52

            self._keys = [_k, _name_k, 'details', 'amount']
            self._use = self._keys[:-1]
            self._date_key = self._keys[0]
            self._amo_key = self._keys[-1]
            self.titles = [_date(), _set(self.name, 27, _l),
                           _set('Details', _w, _d), _set('Amount', 20, _l)]
            self.height = _h
