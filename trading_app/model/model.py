import random
import string

from datetime import datetime
from sqlalchemy import Column, String, UniqueConstraint, DateTime, Numeric

from .base import Base


def _generate_new_trade_id() -> str:
    return 'TR{}'.format(''.join(
        random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(7)
    ))


class Trade(Base):
    __tablename__ = 'tblTrade'

    id = Column(String(9), UniqueConstraint(), default=_generate_new_trade_id, nullable=False, primary_key=True)
    sell_currency = Column(String(3), nullable=False)
    sell_amount = Column(Numeric(10, 3), nullable=False)
    buy_currency = Column(String(3), nullable=False)
    buy_amount = Column(Numeric(10, 3), nullable=False)
    rate = Column(Numeric(10, 5), nullable=False)
    date_booked = Column(DateTime, default=datetime.utcnow)
