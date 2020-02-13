import unittest
from roman import to_arabic


class MyTestCase(unittest.TestCase):
    def test_something(self):
        res = to_arabic("C")
        self.assertEqual(100, res)

        res = to_arabic("MM")
        self.assertEqual(2000, res)

        res = to_arabic("X")
        self.assertEqual(10, res)



if __name__ == '__main__':
    unittest.main()
