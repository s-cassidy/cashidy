from decimal import Decimal



class Pounds(Decimal):
    ## class to represent money in pounds
    def __init__(self, amount):
        pass

    def __str__(self):
        ## string representation of the amount
        return "0"

def parse_to_pounds(amount: str) -> Pounds:
    # turn a string "£13,235.24" into Pounds(13235.24)
    pass
