

test_price_info.py

import unittest
from price_info import total_cost_shopping, cost_of_fruits


class TestPriceInfo(unittest.TestCase):

    def test_total_cost_shopping(self):
        expected_total = 1.20*5 + 1.40*5 + 6.50*1 + 2.70*2 + 0.90*10 + 2.95*1 + 4.95*2
        self.assertAlmostEqual(total_cost_shopping(), expected_total, places=2)

    def test_cost_of_fruits_valid(self):
        self.assertAlmostEqual(cost_of_fruits('apple', 10), 12.00, places=2)
        self.assertAlmostEqual(cost_of_fruits('orange', 3), 4.20, places=2)

    def test_cost_of_fruits_invalid(self):
        self.assertIsNone(cost_of_fruits('banana', 5))


if __name__ == '__main__':
    unittest.main()
