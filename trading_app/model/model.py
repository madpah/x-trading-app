import random
import string

from sqlalchemy import Column, String, UniqueConstraint

from .base import Base


def _generate_new_trade_id() -> str:
    return 'TR{}'.format(''.join(
        random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(7)
    ))


class Trade(Base):
    __tablename__ = 'tblTrade'

    id = Column(String(9), UniqueConstraint(), default=_generate_new_trade_id, nullable=False, primary_key=True)
