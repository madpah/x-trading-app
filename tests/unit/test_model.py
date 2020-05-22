import unittest

from trading_app.model.model import _generate_new_trade_id


class TestModel(unittest.TestCase):

    def test_generate_new_trade_id_ouput(self):
        new_id = _generate_new_trade_id()
        self.assertEqual('TR', new_id[0:2])
        self.assertEqual(9, len(new_id))

    def test_generate_new_trade_id_multiple_times(self):
        new_ids = []
        for x in range(0, 10):
            new_id = _generate_new_trade_id()
            self.assertNotIn(new_id, new_ids)
            new_ids.append(new_id)
