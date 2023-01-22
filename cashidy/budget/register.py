import pandas as pd
from typing import Callable, List
from cashidy.budget.money import parse_to_pence
from uuid import uuid4

class Observable:
    def __init__(self):
        self._observers = []

    def attach(self, observer):
        self._observers.append(observer)

    def detach(self, observer):
        self._observers.remove(observer)

    def _notify(self, *observers):
        for implicated in observers:
            if implicated in self._observers:
                implicated.notify()


class DFReaderWriter:
    read_path = 'cashidy/data/register-test.csv'
    write_path = 'cashidy/data/testwrite.csv'

    @classmethod
    def read_from_csv(cls) -> pd.DataFrame:
        with open(cls.read_path, 'r', encoding='utf8') as f:
            df = pd.read_csv(f)
        df = df.set_index(df['id'])
        df['Date'] = pd.to_datetime(df['Date'])
        df = df.drop(['id'], axis=1)
        return df

    @classmethod
    def write(cls, decorated: Callable) -> Callable:
        def call_and_write(*args, **kwargs) -> None:
            decorated(*args, **kwargs)
            register = args[0]
            register._df.to_csv(cls.write_path)
        return call_and_write


class Register(Observable):
    # can: CRUD operations on the register
    # needs: the register
        
    def __init__(self, path):
        super().__init__()
        self._csv_path = path
        self._df = DFReaderWriter.read_from_csv()

    def monthly_category_activity(self, month: str, category: str) -> int:
        pass

    def category_balance(self, category: int, datetime=None) -> int:
        pass

    def unreconciled_acct_activity(self, account_id: int) -> int:
        # TODO make this since the last reconciliation for that account
        acct_activity = self._df[(self._df['Account'] == account_id)]
        net_activity = sum(acct_activity['Inflow']) - sum(acct_activity['Outflow'])
        return net_activity


    def total_balance(self, datetime: pd.Timestamp | str) -> int:
        # total balance at a given datetime
        # None gives most up-to-date total balance
        pass

    @DFReaderWriter.write
    def change_category(self, transactionID: str, new_category: str) -> None:
        old_category = self._df.loc[transactionID]['Category']
        self._df.loc[transactionID]['Category'] = new_category
        self._notify(old_category, new_category)

    @DFReaderWriter.write
    def change_date(self, transaction_ID, datetime):
        pass

    @DFReaderWriter.write
    def add_transaction(self, date, acct, payee=None, category=None,
                        note=None, outflow=0, inflow=0, confirmed=False):

        transaction_dict = {
                'Date': pd.Timestamp(date),
                'Account': acct,
                'Payee': payee,
                'Category': category,
                'Memo': note,
                'Outflow': outflow,
                'Inflow': inflow,
                'status': 'confirmed' if confirmed else 'unconfirmed'}

        transaction_df = pd.DataFrame([transaction_dict],
                                      index=[uuid4()],
                                      columns=self._df.columns)

        self._df = pd.concat([self._df, transaction_df])
        self._df = self._df.sort_values('Date')
        self._notify(category, acct)

    @DFReaderWriter.write
    def delete_transaction(self, transaction_ID):
        pass


class Transaction:
    def __init__(self, uuid: str, details: dict):
        self._id = uuid
        self.details = details

    def change_date(self, datetime: pd.Timestamp | str) -> None:
        pass
