from fund import Fund
from account import Account
from register import Register
from money import Pence

class Budget(Fund):
    # has: categories, category groups, accounts
    # can: make new categories
    def __init__(self, name: str, register: Register):
        self.register = register
        self.accounts = []
        self._balance = Pence(0)
        self._needs_update = True

    def category_new(self):
        pass

    def category_del(self):
        pass

    def add_account(self, name:str, id: int=None):
        self.accounts.append(Account(id=id, name=name, budget=self))

    def update_balance(self):
        balance = Pence(0)
        for account in self.accounts:
            balance += account.balance
        self._balance = balance


class Category(Fund):
    pass

class Unallocated(Category):
    # special category containing unallocated money
    pass


if __name__ == "__main__":
    budget = Budget('The budget', register=Register('data/register-test.csv'))
    budget.add_account(id=0, name='Current account')
    budget.add_account(id=1, name='Cash')
    budget.update_balance()
