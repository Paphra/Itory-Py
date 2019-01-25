

class Accounts:

    def __init__(self):
        self.statistics = Statistics()
        self.expenses = Expenses()
        self.assets = Assets()
        self.liabilities = Liabilities()
        self.returns = Returns()


class Statistics:

    def __init__(self):
        self.income = self.Income()

    class Income:

        def __init__(self):
            pass


class Expenses:

    def __init__(self):
        pass


class Assets:

    def __init__(self):
        self.fixed = self.Fixed()
        self.current = self.Current()

    class Fixed:

        def __init__(self):
            pass

    class Current:

        def __init__(self):
            self.debtors = self.Debtors()

        class Debtors:

            def __init__(self):
                pass


class Liabilities:

    def __init__(self):
        self.current = self.Current()
        self.long_term = self.LongTerm()

    class LongTerm:

        def __init__(self):
            pass

    class Current:

        def __init__(self):
            self.creditors = self.Creditors()
            self.drawings = self.Drawings()

        class Creditors:

            def __init__(self):
                pass

        class Drawings:

            def __init__(self):
                pass


class Returns:

    def __init__(self):
        self.purchases = self.Purchases()
        self.sales = self.Sales()

    class Purchases:

        def __init__(self):
            pass

    class Sales:

        def __init__(self):
            pass
