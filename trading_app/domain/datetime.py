import logging
from datetime import datetime, timezone

logger = logging.getLogger('trading_app')


def datetime_to_utciso(in_datetime: datetime) -> str:
    if not in_datetime.tzinfo:
        logger.debug("Supplied datetimte is not TZ aware - enforcing UTC TZ")
        in_datetime.replace(tzinfo=timezone.utc)
    return '{}Z'.format(in_datetime.isoformat())
