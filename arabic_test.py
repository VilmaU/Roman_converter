import unittest
from arabic import to_roman

class MyTestCase(unittest.TestCase):
    def test_something(self):
        res = to_roman(3000)
        self.assertEqual("MMM", res)

        # test for 1976
        res = to_roman(1976)
        self.assertEqual("MCMLXXVI", res)

        # test for 101
        res = to_roman(101)
        self.assertEqual("CI", res)


if __name__ == '__main__':
    unittest.main()
