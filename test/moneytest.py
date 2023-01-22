import unittest
from itertools import product
from typing import Tuple, List
from cashidy.money import parse_to_pounds


class TestMoney(unittest.TestCase):
    def test_parser(self):
        prefix = ["", " ", " £", "£", " £"]
        pounds = {
                '0':       ["", "0", "000"],
                '1234':    ["1234", "1 234", "1,234", "1, 234"],
                '1234567': ["1234567", "1 234 567", "1,234,567", "1, 234, 567",
                            "1, 234,567", "1 234, 567", "1,,234567"],
                }
        pence = {
                '00': [".00", "", ".", ".0", ".000"],
                '50': [".50", ".5", ".500"],
                '55': [".55", ".550"],
                '05': [".05", ".050"],
                }
        amounts = list(product(pounds, pence))
        cases = {amount[0]+amount[1]:
                 self.combine_parts(prefix, pounds[pd], pence[p])
                 for pd, p in amounts}
        for amount in cases:
            for case in cases[amount]:
                print(f"Testing {case} == {int(amount)}")
                self.assertEqual(parse_to_pounds(case), int(amount))



    @staticmethod
    def combine_parts(*parts: Tuple[List[str]]) -> List[str]:
        return list(''.join(part) for part in product(*parts))
