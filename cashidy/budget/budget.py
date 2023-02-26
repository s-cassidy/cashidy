from cashidy.budget.fund import Fund
from typing import Mapping
from cashidy.budget.account import Account
from cashidy.budget.register import Register


class Budget(Fund):
    # has: categories, category groups, accounts
    # can: make new categories, accounts
    def __init__(self, name: str, register: Register):
        self.register: Register = register
        self.register._budget = self
        self.accounts: Mapping[int, Account] = {}
        self._balance: int = 0
        self.categories: Mapping[int, Category] = {}
        self._needs_update: bool = True

    def add_category(self, name: str, id: int | None = None):
        if not id:
            id = self._find_unique_id(self.categories)
        self.categories[id] = Category(name, id, self)

    def category_del(self):
        pass

    def add_account(self, name: str, id: int | None = None):
        if not id:
            id = self._find_unique_id(self.accounts)
        self.accounts[id] = Account(id=id, name=name, budget=self)

    def update_balance(self):
        balance = 0
        for id, account in self.accounts.items():
            balance += account.balance
        self._balance = balance

    def _find_unique_id(self, fund_dict: Mapping[int, Fund]) -> int:
        for id in fund_dict.keys():
            if id+1 not in fund_dict.keys():
                return id + 1
        return 0

    @property
    def balance(self):
        self.update_balance()
        return self._balance


class Category(Fund):
    def __init__(self, name: str, id: int, budget: Budget) -> None:
        super().__init__(id, name)
        self.budget = budget

    def update_balance(self) -> None:
        pass


class Unallocated(Category):
    """
    Special category containing unallocated money.
    """

    pass
