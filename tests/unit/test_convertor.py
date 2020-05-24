from unittest import TestCase

from trading_app.domain.convertor import convert_currency


class TestConvertor(TestCase):

    def test_currency_conversion_integers(self):
        self.assertEqual(10, convert_currency(amount=1, rate=10))
        self.assertEqual(10.0, convert_currency(amount=1, rate=10))

    def test_currency_conversion_decimals(self):
        self.assertEqual(109.89, convert_currency(amount=100, rate=1.0989))
        self.assertEqual(109.89000, convert_currency(amount=100, rate=1.0989))
