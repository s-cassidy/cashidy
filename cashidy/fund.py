from abc import ABC, abstractmethod
from uuid import uuid4
from money import Pounds


class Observer(ABC):
    @abstractmethod
    def __call__(self):
        pass


class Fund(ABC, Observer):
    # Should do lazy update of the balance
    # i.e. should only update when it has been
    # modified in some way (needs a notifier)
    # and when its balance has actually been requested
    def __init__(self, name, balance: Pounds=0):
        self._balance = startbalance
        self.name = name
        self._needs_update = True

    def __call__(self):
        self._needs_update = True

    @abstractmethod
    def update_balance(self):
        pass

    @property
    def balance(self):
        if self._needs_update:
            self.update_balance()
        return _balance
