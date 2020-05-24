from decimal import *


def convert_currency(amount: float, rate: float):
    # Currencies are managed with decimal precision 2, but exchange rates with decimal precision 4
    getcontext().prec = 5
    return float(Decimal(amount) * Decimal(rate))
