import unittest
from main import Solution


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.sol = Solution()

    def test_normal_convert(self):
        self.assertEqual(self.sol.number_to_roman(1), "I")
        self.assertEqual(self.sol.number_to_roman(2), "II")
        self.assertEqual(self.sol.number_to_roman(256), "CCLVI")
        self.assertEqual(self.sol.number_to_roman(256_000), "|II|(L)(VI)")

    def test_error_case(self):
        self.assertEqual(
            self.sol.number_to_roman(100_000_000), "number can not over then 99,999,999"
        )
        self.assertEqual(
            self.sol.number_to_roman(-2), "number can not less than 0"
        )
        self.assertEqual(
            self.sol.number_to_roman("dummy_data"), "invalid input"
        )


if __name__ == "__main__":
    unittest.main()