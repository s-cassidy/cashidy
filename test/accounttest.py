from test.setuptest import SetupTests
from test.registertest import add_test_transaction


class TestAccountCreation(SetupTests):
    def test_accounts_in_budget(self):
        self.assertEqual(len(self.budget.accounts), 2)

    def test_accounts_are_observing(self):
        for id, acct in self.budget.accounts.items():
            self.assertIn(acct, self.budget.register._observers)

    def test_accounts_balance(self):
        '''
        Checks balances initialise correctly,
        checks they lazily update balances only
        after being notified of a change
        '''
        self.assertEqual(self.budget.accounts[0].balance, 150000)
        self.assertEqual(self.budget.accounts[1].balance, 144000)
        self.assertEqual(self.budget.accounts[0]._needs_update, False)
        add_test_transaction(self.budget.register)
        self.assertEqual(self.budget.accounts[0]._needs_update, True)
        self.assertEqual(self.budget.accounts[0].balance, 149900)
            

class TestAccountLoad(SetupTests):
    pass
