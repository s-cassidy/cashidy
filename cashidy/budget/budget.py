from cashidy.budget.fund import Fund
from cashidy.budget.account import Account
from cashidy.budget.register import Register
from typing import Any, Dict, Iterator
from collections import defaultdict


class YearMonth:
    """Representation of a month"""

    def __init__(self, year: int, month: int):
        if month > 12 or month < 1:
            raise ValueError("month must be between 1 and 12")
        self.year = year
        self.month = month

    def __repr__(self) -> str:
        return f"YearMonth({self.year}, {self.month:02})"

    def __str__(self) -> str:
        return f"{self.year}-{self.month:02}"

    def __hash__(self) -> int:
        return hash(repr(self))

    def __eq__(self, comp: Any) -> bool:
        if not isinstance(comp, YearMonth):
            return False
        if self.year == comp.year and self.month == comp.month:
            return True
        else:
            return False

    def __lt__(self, comp: "YearMonth") -> bool:
        if self.year < comp.year:
            return True
        if self.year == comp.year and self.month < comp.month:
            return True
        return False

    def __gt__(self, comp: "YearMonth") -> bool:
        if self.year > comp.year:
            return True
        if self.year == comp.year and self.month > comp.month:
            return True
        return False

    def __le__(self, comp: "YearMonth") -> bool:
        return self < comp or self == comp

    def __ge__(self, comp: "YearMonth") -> bool:
        return self > comp or self == comp

    def generate_next_month(self) -> "YearMonth":
        if self.month == 12:
            return YearMonth(self.year + 1, 1)
        else:
            return YearMonth(self.year, self.month + 1)


class Budget(Fund):
    def __init__(self, name: str, register: Register, start_month: tuple[int, int]):
        self.register: Register = register
        self.register._budget = self
        self.accounts: dict[int, Fund] = {}
        self._balance: int = 0
        self.categories: dict[int, Fund] = {}
        self._needs_update: bool = True
        self.start_month = YearMonth(*start_month)

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

    def _find_unique_id(self, fund_dict: dict[int, Fund]) -> int:
        for id in fund_dict.keys():
            if id + 1 not in fund_dict.keys():
                return id + 1
        return 0

    @property
    def balance(self):
        self.update_balance()
        return self._balance


def generate_months_in_range(start: YearMonth, end: YearMonth) -> Iterator[YearMonth]:
    if not start <= end:
        raise ValueError("Start month must be before end month")
    month = start
    while month <= end:
        yield month
        month = month.generate_next_month()


class Category(Fund):
    def __init__(self, name: str, id: int, budget: Budget) -> None:
        super().__init__(id, name)
        self.budget = budget
        self.assignments: defaultdict[YearMonth, int] = defaultdict(lambda: 0)

    def get_balance_to_date(self, month: YearMonth) -> int:
        register = self.budget.register
        start = self.budget.start_month
        end = month
        assignments = sum(
            self.assignments[m] for m in generate_months_in_range(start, end)
        )
        activity = register.get_category_activity_in_month_range(
            self.id, start, end)
        return assignments + activity

    def update_balance(self) -> None:
        pass

    def assign_funds(self, amount: int, month: YearMonth) -> None:
        self.assignments[month] = amount


class Unallocated(Category):
    """
    Special category containing unallocated money.
    """

    pass
