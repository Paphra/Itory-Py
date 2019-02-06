"""Accounts model module"""

from .db_connection import Conn


class Accounts:

    def __init__(self):
        self.statistics = Statistics()
        self.expenses = Expenses()
        self.drawings = Drawings()
        self.assets = Assets()
        self.liabilities = Liabilities()
        self.returns = Returns()


class Universal:

    def __init__(self, collection, db_fetch):
        self.collection = collection
        self.db_fetch = db_fetch

    def add(self, item):
        self.collection.insert_one(item)
        self.db_fetch()

    def delete(self, item, key):
        _query = {key: item[key]}
        self.collection.delete_one(_query)
        self.db_fetch()

    def edit(self, item, pri_key, key, value):
        _query = {pri_key: item[pri_key]}
        _new_value = {'$set': {key: value}}
        self.collection.update_one(_query, _new_value)
        self.db_fetch()


class Statistics:

    def __init__(self):
        self.income = self.Income()

    class Income:

        def __init__(self):
            self.all_incomes = []
            db_con = Conn()
            self.collection = db_con.get_collection('col_income')
            self.db_fetch()

            self.work = Universal(self.collection, self.db_fetch)

        def db_fetch(self):
            self.all_incomes = []
            for income in self.collection.find({}).sort('income_date', -1):
                self.all_incomes.append(income)

        def get_all(self):
            return self.all_incomes


class Expenses:

    def __init__(self):
        self.all_expenses = []
        db_con = Conn()
        self.collection = db_con.get_collection('col_expenses')
        self.db_fetch()

        self.work = Universal(self.collection, self.db_fetch)

    def db_fetch(self):
        self.all_expenses = []
        for expense in self.collection.find({}).sort('exp_date', -1):
            self.all_expenses.append(expense)

    def get_all(self):
        return self.all_expenses


class Drawings:

    def __init__(self):
        self.all_drawings = []
        db_con = Conn()
        self.collection = db_con.get_collection('col_drawings')
        self.db_fetch()

        self.work = Universal(self.collection, self.db_fetch)

    def db_fetch(self):
        self.all_drawings = []
        for drawing in self.collection.find({}).sort('draw_date', -1):
            self.all_drawings.append(drawing)

    def get_all(self):
        return self.all_drawings


class Assets:

    def __init__(self):
        self.fixed = self.Fixed()
        self.current = self.Current()

    class Fixed:

        def __init__(self):
            self.all_fixed = []
            db_con = Conn()
            self.collection = db_con.get_collection('col_fixed_assets')
            self.db_fetch()

            self.work = Universal(self.collection, self.db_fetch)

        def db_fetch(self):
            self.all_fixed = []
            for fixed in self.collection.find({}).sort('fixed_assets_date', -1):
                self.all_fixed.append(fixed)

        def get_all(self):
            return self.all_fixed

    class Current:

        def __init__(self):
            self.debtors = self.Debtors()
            self.profits = self.Profits()

        class Debtors:

            def __init__(self):
                self.all_debtors = []
                db_con = Conn()
                self.collection = db_con.get_collection('col_debtors')
                self.db_fetch()

                self.work = Universal(self.collection, self.db_fetch)

            def db_fetch(self):
                self.all_debtors = []
                for debtor in self.collection.find({}).sort('debt_date', -1):
                    self.all_debtors.append(debtor)

            def get_all(self):
                return self.all_debtors

        class Profits:

            def __init__(self):
                self.all_profits = []
                db_con = Conn()
                self.collection = db_con.get_collection('col_profits')
                self.db_fetch()

                self.work = Universal(self.collection, self.db_fetch)

            def db_fetch(self):
                self.all_profits = []
                for profit in self.collection.find({}).sort('profit_date', -1):
                    self.all_profits.append(profit)

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
            db_con = Conn()
            self.collection = db_con.get_collection('col_creditors')
            self.db_fetch()

            self.work = Universal(self.collection, self.db_fetch)

        def db_fetch(self):
            self.all_creditors = []
            for creditor in self.collection.find({}).sort('cred_date', -1):
                self.all_creditors.append(creditor)

        def get_all(self):
            return self.all_creditors

    class Accruals:

        def __init__(self):
            self.all_accruals = []
            db_con = Conn()
            self.collection = db_con.get_collection('col_accruals')
            self.db_fetch()

            self.work = Universal(self.collection, self.db_fetch)

        def db_fetch(self):
            self.all_accruals = []
            for accrual in self.collection.find({}).sort('accr_date', -1):
                self.all_accruals.append(accrual)

        def get_all(self):
            return self.all_accruals


class Returns:

    def __init__(self):
        self.purchases = self.Purchases()
        self.sales = self.Sales()

    class Purchases:

        def __init__(self):
            self.all_pur_returns = []
            db_con = Conn()
            self.collection = db_con.get_collection('col_retout')
            self.db_fetch()

            self.work = Universal(self.collection, self.db_fetch)

        def db_fetch(self):
            self.all_pur_returns = []
            for retout in self.collection.find({}).sort('retout_date', -1):
                self.all_pur_returns.append(retout)

        def get_all(self):
            return self.all_pur_returns

    class Sales:

        def __init__(self):
            self.all_sales_returns = []
            db_con = Conn()
            self.collection = db_con.get_collection('col_retin')
            self.db_fetch()

            self.work = Universal(self.collection, self.db_fetch)

        def db_fetch(self):
            self.all_sales_returns = []
            for retin in self.collection.find({}).sort('retin_date', -1):
                self.all_sales_returns.append(retin)

        def get_all(self):
            return self.all_sales_returns
