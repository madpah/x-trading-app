import logging
from decimal import getcontext, Decimal

logger = logging.getLogger('trading_app')


def convert_currency(amount: float, rate: float):
    # Currencies are managed with decimal precision 2, but exchange rates with decimal precision 4
    getcontext().prec = 5
    logger.debug('Converting currency: {} * {}'.format(amount, rate))
    return float(Decimal(amount) * Decimal(rate))
