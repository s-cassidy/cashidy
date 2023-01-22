from __future__ import annotations
from typing import Tuple


def pounds_part(amount: int) -> int:
    return amount // 100


def pence_part(amount: int) -> int:
    return amount % 100


def pounds_as_str(amount: int) -> str:
    pounds_str = str(pounds_part(amount))
    L = len(pounds_str)
    # insert comma separators in the correct places
    pounds = ''.join([f",{dgt}" if (i > 0) and (i - L) % 3 == 0 else dgt
                      for i, dgt in enumerate(pounds_str)])
    pence = str(pence_part(amount))
    if len(pence) == 1:
        pence = "0" + pence
    return f"£{pounds}.{pence}"


def money_mul(amount: int, multiplier: int | float) -> int:
    return int(round(amount*multiplier), 0)

def money_div(amount: int, divisor: int | float) -> int:
    return int(round(amount/divisor), 0)


def parse_to_pence(amount: str) -> int:
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
    return value


def extract_digits(string: str) -> str:
    return ''.join(c for c in string if c in "0123456789")
