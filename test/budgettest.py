from test.registertest import add_test_transaction
from test.setuptest import SetupTests
from cashidy.budget.budget import Category


class TestBudgetBalances(SetupTests):
    def test_budget_balance(self):
        self.assertEqual(self.budget.balance, 294000)

    def test_budget_balance_update(self):
        register = self.budget.register
        add_test_transaction(register)
        self.assertEqual(self.budget.balance, 293900)

class TestCategories(SetupTests):
    def test_categories_creation(self):
        budget = self.budget
        budget.add_category("Groceries")
        self.assertIsInstance(budget.categories[0], Category)
