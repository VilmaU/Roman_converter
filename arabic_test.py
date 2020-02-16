import unittest
from arabic import to_roman

class MyTestCase(unittest.TestCase):
    def test_something(self):
        res = to_roman(3003)
        self.assertEqual("MMMIII", res)

        # test for 5
        res = to_roman(5)
        self.assertEqual("V", res)

        # test for 100
        res = to_roman(100)
        self.assertEqual("C", res)


if __name__ == '__main__':
    unittest.main()
