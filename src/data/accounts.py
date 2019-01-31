

class Accounts:

    def __init__(self):
        self.statistics = Statistics()
        self.expenses = Expenses()
        self.drawings = Drawings()
        self.assets = Assets()
        self.liabilities = Liabilities()
        self.returns = Returns()


class Universal:

    def __init__(self, list_):
        self._list = list_

    def add(self, item):
        self._list.append(item)

    def delete(self, item):
        self._list.remove(item)

    def edit(self, item, key, value):
        for _l in self._list:
            if _l == item:
                _l[key] = value


class Statistics:

    def __init__(self):
        self.income = self.Income()

    class Income:

        def __init__(self):
            self.all_incomes = []

            self.db_fetch()
            self.mock()

            self.work = Universal(self.all_incomes)

        def db_fetch(self):
            self.all_incomes = []

        def mock(self):
            pass

        def get_all(self):
            return self.all_incomes


class Expenses:

    def __init__(self):
        self.all_expenses = []

        self.db_fetch()
        self.mock()

        self.work = Universal(self.all_expenses)

    def db_fetch(self):
        self.all_expenses = []

    def mock(self):
        pass

    def get_all(self):
        return self.all_expenses


class Drawings:

    def __init__(self):
        self.all_drawings = []

        self.db_fetch()
        self.mock()

        self.work = Universal(self.all_drawings)

    def db_fetch(self):
        self.all_drawings = []

    def mock(self):
        pass

    def get_all(self):
        return self.all_drawings


class Assets:

    def __init__(self):
        self.fixed = self.Fixed()
        self.current = self.Current()

    class Fixed:

        def __init__(self):
            self.all_fixed = []

            self.db_fetch()
            self.mock()

            self.work = Universal(self.all_fixed)

        def db_fetch(self):
            self.all_fixed = []

        def mock(self):
            pass

        def get_all(self):
            return self.all_fixed

    class Current:

        def __init__(self):
            self.debtors = self.Debtors()
            self.profits = self.Profits()

        class Debtors:

            def __init__(self):
                self.all_debtors = []

                self.db_fetch()
                self.mock()

                self.work = Universal(self.all_debtors)

            def db_fetch(self):
                self.all_debtors = []

            def mock(self):
                pass

            def get_all(self):
                return self.all_debtors

        class Profits:

            def __init__(self):
                self.all_profits = []

                self.db_fetch()
                self.mock()

                self.work = Universal(self.all_profits)

            def db_fetch(self):
                self.all_profits = []

            def mock(self):
                pass

            def get_all(self):
                return self.all_profits


class Liabilities:

    def __init__(self):
        self.long_term = self.LongTerm()

        self.creditors = self.Creditors()
        self.accruals = self.Accruals()

    class LongTerm:

        def __init__(self):
            pass

    class Creditors:

        def __init__(self):
            self.all_creditors = []

            self.db_fetch()
            self.mock()

            self.work = Universal(self.all_creditors)

        def db_fetch(self):
            self.all_creditors = []

        def mock(self):
            pass

        def get_all(self):
            return self.all_creditors

    class Accruals:

        def __init__(self):
            self.all_accruals = []

            self.db_fetch()
            self.mock()

            self.work = Universal(self.all_accruals)

        def db_fetch(self):
            self.all_accruals = []

        def mock(self):
            pass

        def get_all(self):
            return self.all_accruals


class Returns:

    def __init__(self):
        self.purchases = self.Purchases()
        self.sales = self.Sales()

    class Purchases:

        def __init__(self):
            self.all_pur_returns = []

            self.db_fetch()
            self.mock()

            self.work = Universal(self.all_pur_returns)

        def db_fetch(self):
            self.all_pur_returns = []

        def mock(self):
            pass

        def get_all(self):
            return self.all_pur_returns

    class Sales:

        def __init__(self):
            self.all_sales_returns = []

            self.db_fetch()
            self.mock()

            self.work = Universal(self.all_sales_returns)

        def db_fetch(self):
            self.all_sales_returns = []

        def mock(self):
            pass

        def get_all(self):
            return self.all_sales_returns
