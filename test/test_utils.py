import unittest
from datetime import datetime

from utils import *


class TestFinanceCalculator(unittest.TestCase):

    def test_calculate(self):
        start_date = datetime(2024, 1, 1)
        periods = 12
        start_amount = 10000
        rate = 5

        expected_output = {'01.02.2024': 10041.67,
                           '01.03.2024': 10083.51,
                           '01.04.2024': 10125.52,
                           '01.05.2024': 10167.71,
                           '01.06.2024': 10210.08,
                           '01.07.2024': 10252.62,
                           '01.08.2024': 10295.34,
                           '01.09.2024': 10338.24,
                           '01.10.2024': 10381.31,
                           '01.11.2024': 10424.57,
                           '01.12.2024': 10468.0,
                           '01.01.2025': 10511.62}

        result = calculate(start_date, periods, start_amount, rate)

        self.assertEqual(result, expected_output)

        start_date = datetime(2024, 1, 1)
        periods = 1
        start_amount = 10000
        rate = 1
        expected_output = {'01.02.2024': 10008.33}
        result = calculate(start_date, periods, start_amount, rate)
        self.assertEqual(result, expected_output)

        start_amount = 3000000
        rate = 8
        expected_output = {'01.02.2024': 3020000.0}
        result = calculate(start_date, periods, start_amount, rate)
        self.assertEqual(result, expected_output)

        periods = 60
        start_amount = 10000
        rate = 5
        result = calculate(start_date, periods, start_amount, rate)
        self.assertTrue(len(result), 60)

    def test_convert_date(self):
        date_str = "2024-09-30"
        expected_date = datetime(2024, 9, 30)

        result = convert_date(date_str)

        self.assertEqual(result, expected_date)

    def test_convert_date_invalid_format(self):
        with self.assertRaises(ValueError):
            convert_date("30-09-2024")

    def test_validate_data(self):
        self.assertEqual(validate_data(12, 10000, 5), "ok")
        self.assertEqual(validate_data(0, 10000, 5), "Invalid period")
        self.assertEqual(validate_data(12, 5000, 5), "Invalid amount")
        self.assertEqual(validate_data(12, 10000, 9), "Invalid rate")

    def test_validate_data_invalid_period(self):
        # Test invalid periods (too low and too high)
        self.assertEqual(validate_data(0, 15000, 5), "Invalid period")
        self.assertEqual(validate_data(61, 15000, 5), "Invalid period")

    def test_validate_data_invalid_amount(self):
        self.assertEqual(validate_data(12, 5000, 5), "Invalid amount")
        self.assertEqual(validate_data(12, 3000001, 5), "Invalid amount")

    def test_validate_data_invalid_rate(self):
        self.assertEqual(validate_data(12, 15000, 0), "Invalid rate")
        self.assertEqual(validate_data(12, 15000, 9), "Invalid rate")


if __name__ == '__main__':
    unittest.main()
