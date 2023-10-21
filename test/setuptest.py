import unittest
from cashidy.budget.budget import Budget
from cashidy.budget.register import Register
from pathlib import Path
import os

SOURCE_DIR = Path(os.path.dirname(os.path.abspath(__file__)))


class SetupTests(unittest.TestCase):
    def setUp(self):
        self.test_register = Register(SOURCE_DIR / '../cashidy/data/register-test.csv')
        self.budget = Budget(
            'The budget',
            register=self.test_register,
            start_month=(2022, 11)
        )
        self.budget.add_account(id=0, name='Current account')
        self.budget.add_account(id=1, name='Cash')

    def tearDown(self):
        del self.budget
