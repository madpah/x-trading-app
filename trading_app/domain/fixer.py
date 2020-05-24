import logging
from typing import List
import requests

DEFAULT_FIXER_API_BASE = 'http://data.fixer.io/api'

logger = logging.getLogger('trading_app')


class FixerIOClient:

    def __init__(self, access_key: str):
        self._access_key = access_key
        self._api_base = DEFAULT_FIXER_API_BASE

    def get_currencies(self) -> List:
        logger.debug('Getting currencies from fixer.io')
        response = requests.get(
            "{}/symbols".format(self._api_base),
            params={
                "access_key": self._access_key
            }
        )

        if response.status_code != 200:
            return None

        response_object = response.json()
        logger.debug('Response from fixer.io: {}'.format(response_object))
        if not response_object['success']:
            return None

        return list(response_object['symbols'].keys())

    def get_latest_rate(self, from_currency: str, to_currency: str) -> float:
        logger.debug('Getting latest rate from fixer.io for {} -> {}'.format(from_currency, to_currency))
        response = requests.get(
            "{}/latest".format(self._api_base),
            params={
                "access_key": self._access_key,
                "base": from_currency,
                "symbols": [to_currency]
            }
        )

        if response.status_code != 200:
            return None

        response_object = response.json()
        logger.debug('Response from fixer.io: {}'.format(response_object))
        if not response_object['success']:
            return None

        return response_object['rates'][to_currency]
