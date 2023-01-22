import unittest
from cashidy.budget.budget import Budget
from cashidy.budget.register import Register


class SetupTests(unittest.TestCase):
    def setUp(self):
        self.test_register = Register('cashidy/data/register-test.csv')
        self.budget = Budget('The budget', register=self.test_register)
        self.budget.add_account(id=0, name='Current account')
        self.budget.add_account(id=1, name='Cash')

    def tearDown(self):
        del self.budget
