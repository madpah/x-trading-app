from copy import copy
from decimal import *
from json import dumps

from flask import Response
from sqlalchemy import desc

from ..domain.config import Config
from ..domain.database import DatabaseConnector
from ..domain.datetime import datetime_to_utciso
from ..domain.fixer import FixerIOClient
from ..model.model import Trade

fixer_client = FixerIOClient(access_key=Config().get().get('fixer', 'access_key'))
getcontext().prec = 2


def get_currencies(term: str = None):
    currencies = fixer_client.get_currencies()
    if term and len(term) > 0:
        currencies = list(filter(lambda x: term in x, currencies))
    return _make_json_response(response_object=currencies)


def get_trade_rate(body: dict):
    current_rate = fixer_client.get_latest_rate(
        from_currency=body['sell_currency'],
        to_currency=body['buy_currency']
    )

    response_object = copy(body)
    # response_object['buy_amount'] = float(convert_currency(amount=body['sell_amount'], rate=current_rate))
    response_object['rate'] = current_rate

    return _make_json_response(response_object=response_object)


def get_booked_trades():
    q = DatabaseConnector().get_session().query(Trade).order_by(desc(Trade.date_booked))

    responses = []
    trade: Trade
    for trade in q:
        responses.append(_map_trade_to_dict(trade=trade))

    print("Responses: {}".format(responses))

    return _make_json_response(response_object=responses)


def book_new_trade(body: dict):
    s = DatabaseConnector().get_session()
    try:
        s.add(_map_json_to_trade_v1(json=body))
        s.commit()
    except Exception as e:
        print("Exception: {}".format(e))
        return _make_empty_response(500)

    return _make_empty_response(return_code=201)


def _make_empty_response(return_code=501) -> Response:
    return Response(status=return_code, content_type='application/json')


def _make_json_response(response_object={}, return_code=200):
    return Response(
        content_type='application/json',
        status=return_code,
        response=dumps(response_object)
    )


def _map_json_to_trade_v1(json: dict) -> Trade:
    return Trade(
        sell_currency=json['sell_currency'] if 'sell_currency' in json.keys() else None,
        sell_amount=json['sell_amount'] if 'sell_amount' in json.keys() else None,
        buy_currency=json['buy_currency'] if 'buy_currency' in json.keys() else None,
        buy_amount=json['buy_amount'] if 'buy_amount' in json.keys() else None,
        rate=json['rate'] if 'rate' in json.keys() else None
    )


def _map_trade_to_dict(trade: Trade) -> dict:
    return {
        "sell_currency": trade.sell_currency,
        "sell_amount": float(trade.sell_amount),
        "buy_currency": trade.buy_currency,
        "buy_amount": float(trade.buy_amount),
        "rate": float(trade.rate),
        "date_booked": datetime_to_utciso(trade.date_booked)
    }
