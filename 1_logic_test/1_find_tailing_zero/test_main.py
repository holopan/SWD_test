import unittest
from main import Solution


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.sol = Solution()

    def test_positive_numbers(self):
        self.assertEqual(self.sol.find_tailing_zeroes(7), 1)
        self.assertEqual(self.sol.find_tailing_zeroes(10), 2)
        self.assertEqual(self.sol.find_tailing_zeroes(3), 0)

    def test_zero(self):
        self.assertEqual(self.sol.find_tailing_zeroes(0), 0)

    def test_negative_number(self):
        self.assertEqual(
            self.sol.find_tailing_zeroes(-10), "number can not be negative"
        )


if __name__ == "__main__":
    unittest.main()