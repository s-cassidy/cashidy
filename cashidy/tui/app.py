from textual.app import App, ComposeResult
from textual.widgets import (Header,
                             Footer,
                             DataTable,
                             ListView,
                             ListItem,
                             Label)
from cashidy.budget.budget import Budget
from cashidy.budget.register import Register, Transaction
from typing import List


class AccountTable:
    def __init__(self, transactions: List[Transaction]):
        self.transactions = transactions
        self._private_table = self._make_table()

    def _make_table(self) -> list:
        rows = [None]
        for trns in self.transactions:
            rows[0] = ("trns", *tuple(trns.details.keys()))
            rows.append((trns, *tuple(trns.details.values())))
        return rows

    def get_table(self) -> list:
        table = [row[1:] for row in self._private_table]
        return table


class CashidyUI(App):
    """TUI frontend for the Cashidy budget app."""

    BINDINGS = [("d", "toggle_dark", "Toggle dark mode")]

    def compose(self) -> ComposeResult:
        yield Header()
        yield ListView(*(item for item in self.accounts_list()))
        yield DataTable()
        yield Footer()

    def link_budget(self, budget: Budget) -> None:
        self.budget = budget

    def action_toggle_dark(self) -> None:
        self.dark = not self.dark

    def accounts_list(self) -> ListItem:
        for acct in self.budget.accounts.values():
            yield ListItem(Label(f"{acct.name}:  {acct.balance}"))

    def on_mount(self) -> None:
        table = self.query_one(DataTable)
        self.trns_table = AccountTable(self.budget.register.get_transactions())
        rows = iter(self.trns_table.get_table())
        table.add_columns(*next(rows))
        table.add_rows(rows)





if __name__ == "__main__":
    app = CashidyUI()
    test_register = 'cashidy/data/register-test.csv'
    budget = Budget('The budget', register=Register(test_register))
    budget.add_account(id=0, name='Current account')
    budget.add_account(id=1, name='Cash')
    app.link_budget(budget)
    app.run()
