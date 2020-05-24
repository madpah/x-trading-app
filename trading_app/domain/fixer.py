import logging
from typing import List

import requests

DEFAULT_FIXER_API_BASE = 'http://data.fixer.io/api'


class FixerConversionResult:

    @staticmethod
    def from_fixer_response(response_as_json: object):
        print(response_as_json)
        return FixerConversionResult(
            from_currency=response_as_json['query']['from'],
            to_currency=response_as_json['query']['to'],
            rate=response_as_json['info']['rate'],
            amount=response_as_json['result']
        )

    def __init__(self, from_currency: str, to_currency: str, rate: float, amount: float):
        self._from_currency = from_currency
        self._to_currency = to_currency
        self._rate = rate
        self._amount = amount

    def get_amount(self) -> float:
        return self._amount

    def get_rate(self) -> float:
        return self._rate


class FixerIOClient:

    def __init__(self, access_key: str):
        self._access_key = access_key
        self._api_base = DEFAULT_FIXER_API_BASE

    def get_currencies(self) -> List:
        response = requests.get(
            "{}/symbols".format(self._api_base),
            params={
                "access_key": self._access_key
            }
        )

        if response.status_code != 200:
            return None

        response_object = response.json()
        if not response_object['success']:
            return None

        return list(response_object['symbols'].keys())

    def get_latest_rate(self, from_currency: str, to_currency: str) -> float:
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
        print("Raw Fixer Response: {}".format(response_object))
        if not response_object['success']:
            return None

        return response_object['rates'][to_currency]
