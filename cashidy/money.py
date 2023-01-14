from decimal import Decimal
from itertools import product
from typing import Tuple, List
import unittest


class Pence:
    # class to represent money in pounds
    def __init__(self, amount: int) -> None:
        self.amount = amount
        self._pounds = amount // 100
        self._pence = amount % 100

    def __str__(self) -> str:
        pounds_str = str(self._pounds)
        L = len(pounds_str)
        # The following line inserts comma separators in the correct places
        pounds = ''.join([f",{dgt}" if (i > 0) and (i - L) % 3 == 0 else dgt
                          for i, dgt in enumerate(pounds_str)])
        pence = str(self._pence)
        return ''.join(["£", pounds, ".", pence])

    def __add__(self, other: Pence) -> Pence:
        return Pence(self.amount + other.amount)

    def __mul__(self, other: float | int) -> Pence:
        return Pence(int(round(self.amount * other, 0)))

    def __div__(self, other: float | int) -> Pence:
        return Pence(int(round(self.amount / other, 0)))

    def __repr__(self) -> str:
        return f"Pounds: {self.__str__()}"


def parse_to_pounds(amount: str) -> Pence:
    if "." in amount:
        pounds_part, dot, pence_part = amount.partition(".")
        pounds_part = extract_digits(pounds_part)
        pence_part = extract_digits(pence_part)
        if len(pence_part) == 1:
            pence_part = pence_part + "0"
        elif len(pence_part) == 0:
            pence_part = pence_part + "00"
        elif len(pence_part) > 1:
            pence_part = pence_part[:2]
    else:
        pounds_part = extract_digits(amount)
        pence_part = "00"
    value = int(pounds_part + pence_part)
    return Pence(value)


def extract_digits(string: str) -> str:
    return ''.join(c for c in string if c in "0123456789")


class TestPounds(unittest.TestCase):
    def test_parser(self):
        prefix = ["", " ", " £", "£", " £"]
        # First pound amount in each list
        # must be without separators "dddd"
        pounds1234 = ["1234", "1 234", "1,234", "1, 234"]
        pounds1234567 = ["1234567", "1 234 567", "1,234,567", "1, 234, 567",
                         "1, 234,567", "1 234, 567", "1,,234567"]
        # First pence amount in each list must be ".dd"
        pence_none = [".00", "", ".", ".0", ".000"]
        pence_50 = [".50", ".5", ".500"]
        pence_55 = [".55", ".550"]
        pence_05 = [".05", ".050"]
        pounds = (pounds1234, pounds1234567)
        pence = (pence_none, pence_50, pence_55, pence_05)
        amounts = list(product(pounds, pence))
        cases = {int(amount[0][0]+amount[1][0][1:3]):  # eg int('1234' + '00')
                 self.join_parts(prefix, amount[0], amount[1])
                 for amount in amounts}
        for amount in cases:
            print(amount, cases[amount])
            for case in cases[amount]:
                self.assertEqual(parse_to_pounds(case).amount, amount)



    @staticmethod
    def join_parts(*parts: Tuple[List[str]]) -> List[str]:
        return list(''.join(part) for part in product(*parts))


# ((['£', ''], ['1'], ['', ',', ' ', ', '], ['234']), (['', ',', ', '], ['567']), ['', '.0', '.00'])
