from test.registertest import add_test_transaction
from test.setuptest import SetupTests


class TestBudgetBalances(SetupTests):
    def test_budget_balance(self):
        self.assertEqual(self.budget.balance, 294000)

    def test_budget_balance_update(self):
        register = self.budget.register
        add_test_transaction(register)
        self.assertEqual(self.budget.balance, 293900)
