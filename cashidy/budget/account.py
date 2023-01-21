from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from cashidy.budget.budget import Budget
from cashidy.budget.fund import Fund
from cashidy.budget.money import Pence


class Account(Fund):
    def __init__(self, id, name, budget: Budget, reconciled: int = 0):
        super().__init__(id, name)
        self._last_reconciled = Pence(reconciled)
        self.budget = budget

    def update_balance(self):
        change = self.budget.register.unreconciled_acct_activity(self.id)
        self._balance = self._last_reconciled + change
        


class RemoteAccount(Account):
    # for accounts that get their data from
    # an authoritative remote source, i.e.
    # import statements directly
    pass

class UserAccount(Account):
    # for account that must be manually
    # updated by the user (e.g. cash)
    pass
