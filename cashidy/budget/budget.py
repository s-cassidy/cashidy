from cashidy.budget.fund import Fund
from cashidy.budget.account import Account
from cashidy.budget.register import Register



class Budget(Fund):
    # has: categories, category groups, accounts
    # can: make new categories, accounts
    def __init__(self, name: str, register: Register):
        self.register = register
        self.register.budget = self
        self.accounts = {}
        self._balance = 0
        self._needs_update = True

    def category_new(self):
        pass

    def category_del(self):
        pass

    def add_account(self, name: str, id: int = None):
        self.accounts[id]= Account(id=id, name=name, budget=self)

    def update_balance(self):
        balance = 0
        for id, account in self.accounts.items():
            balance += account.balance
        self._balance = balance

    @property
    def balance(self):
        self.update_balance()
        return self._balance


class Category(Fund):
    pass

class Unallocated(Category):
    '''
    Special category containing unallocated money.
    '''
    pass


