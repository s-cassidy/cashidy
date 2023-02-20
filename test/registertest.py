import unittest
from test.setuptest import SetupTests


def add_test_transaction(register) -> None:
    register.add_transaction(date="2023-01-05",
                             acct=0,
                             outflow=100)


class TestNewTransaction(SetupTests):
    def test_add_transaction(self):
        register = self.budget.register
        start_num_transactions = len(register._df)
        expected_transactions = start_num_transactions + 1

        add_test_transaction(register)

        self.assertEqual(len(register._df), expected_transactions)
        self.assertEqual(list(register._df['Date']),
                         sorted(list(register._df['Date'])))
        self.assertEqual(len(set(register._df.axes[0])),
                         expected_transactions)


class TestQuery(SetupTests):        
    def test_query_by_column_equality(self):
        """Filter elements of a column that equal a given value"""
         
