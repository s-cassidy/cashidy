from textual.app import App, ComposeResult
from textual.widgets import (Header,
                             Footer,
                             ListView,
                             ListItem,
                             Label)
from cashidy.budget.budget import Budget
from cashidy.budget.register import Register

class CashidyUI(App):
    """TUI frontend for the Cashidy budget app."""

    BINDINGS = [("d", "toggle_dark", "Toggle dark mode")]

    def compose(self) -> ComposeResult:
        yield Header()
        yield ListView(*(item for item in self.accounts_list()))
        yield Footer()

    def link_budget(self, budget: Budget) -> None:
        self.budget = budget

    def action_toggle_dark(self) -> None:
        self.dark = not self.dark

    def accounts_list(self) -> ListItem:
        for acct in self.budget.accounts:
            yield ListItem(Label(f"{acct.name}:  {acct.balance}"))



if __name__ == "__main__":
    app = CashidyUI()
    test_register = 'cashidy/data/register-test.csv'
    budget = Budget('The budget', register=Register(test_register))
    budget.add_account(id=0, name='Current account')
    budget.add_account(id=1, name='Cash')
    app.link_budget(budget)
    app.run()
