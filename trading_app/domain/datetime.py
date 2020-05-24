from datetime import datetime, timezone


def json_to_utciso(json_datetime: str) -> str:
    return datetime.strptime(json_datetime, "%Y-%m-%dT%H:%M:%S.%fZ")


def utc_to_iso(utc_datetime: str) -> str:
    return datetime.strptime("{} UTC".format(utc_datetime), "%Y-%m-%d %H:%M:%S %Z").isoformat()


def datetime_to_utciso(in_datetime: datetime) -> str:
    if not in_datetime.tzinfo:
        in_datetime.replace(tzinfo=timezone.utc)
    return '{}Z'.format(in_datetime.isoformat())
