import unittest
from roman import to_arabic


class MyTestCase(unittest.TestCase):
    def test_something(self):
        res = to_arabic("CI")
        self.assertEqual(101, res)

        res = to_arabic("XI")
        self.assertEqual(11, res)

        res = to_arabic("MMMIII")
        self.assertEqual(3003, res)

        res = to_arabic("DVI")
        self.assertEqual(506, res)

if __name__ == '__main__':
    unittest.main()
