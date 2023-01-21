from __future__ import annotations


class Pence:
    # class to represent money in pounds and pence
    def __init__(self, amount: int) -> None:
        self.amount = amount
        self._pounds = amount // 100
        self._pence = amount % 100

    def __str__(self) -> str:
        pounds_str = str(self._pounds)
        L = len(pounds_str)
        # insert comma separators in the correct places
        pounds = ''.join([f",{dgt}" if (i > 0) and (i - L) % 3 == 0 else dgt
                          for i, dgt in enumerate(pounds_str)])
        pence = str(self._pence)
        if len(pence) == 1:
            pence = "0" + pence
        return f"£{pounds}.{pence}"

    def __add__(self, other: 'Pence') -> 'Pence':
        return Pence(self.amount + other.amount)

    def __eq__(self, other: 'Pence') -> bool:
        return self.amount == other.amount

    def __mul__(self, other: float | int) -> 'Pence':
        return Pence(int(round(self.amount * other, 0)))

    def __rmul__(self, other: float | int) -> 'Pence':
        return self * other

    def __floordiv__(self, other: float | int) -> 'Pence':
        return Pence(self.amount // other)

    def __truediv__(self, other: float | int) -> 'Pence':
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


