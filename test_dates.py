import unittest

from dates import is_leap_year, Date, list_year_month, validate_date_range, calculate_date_diff

class TestDatesFunctions(unittest.TestCase):
    def test_is_leap_year(self):
        self.assertTrue(is_leap_year(2000))
        self.assertFalse(is_leap_year(2021))

    def test_validate_date_range(self):
        d1 = Date(31, 12, 2020)
        d2 = Date(1, 5, 2019)
        valid_start, valid_end = validate_date_range(d1, d2)
        self.assertIs(valid_start, d2)
        self.assertIs(valid_end, d1)

    def test_list_year_month(self):
        d1 = Date(6, 6, 2020)
        d2 = Date(27, 6, 2020)
        expected = [(6, 2020)]
        self.assertEqual(list_year_month(d1, d2), expected)

    def test_calculate_date_diff(self):
        cases = [
            (Date(2, 6, 1983), Date(22, 6, 1983), 19),
            (Date(4, 7, 1984), Date(25, 12, 1984), 173),
            (Date(3, 1, 1989), Date(3, 8, 1983), 1979),
        ]
        for case in cases:
            self.assertEqual(calculate_date_diff(case[0], case[1]), case[2])

if __name__ == '__main__':
    unittest.main()
