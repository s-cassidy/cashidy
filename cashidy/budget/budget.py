from cashidy.budget.fund import Fund
from cashidy.budget.account import Account
from cashidy.budget.register import Register
from cashidy.budget.money import Pence



class Budget(Fund):
    # has: categories, category groups, accounts
    # can: make new categories, accounts
    def __init__(self, name: str, register: Register):
        self.register = register
        self.accounts = []  # possibly should be a dictionary
        self._balance = Pence(0)
        self._needs_update = True

    def category_new(self):
        pass

    def category_del(self):
        pass

    def add_account(self, name: str, id: int = None):
        self.accounts.append(Account(id=id, name=name, budget=self))

    def update_balance(self):
        balance = Pence(0)
        for account in self.accounts:
            balance += account.balance
        self._balance = balance

    @property
    def balance(self):
        self.update_balance()
        return self._balance


class Category(Fund):
    pass

class Unallocated(Category):
    # special category containing unallocated money
    pass


