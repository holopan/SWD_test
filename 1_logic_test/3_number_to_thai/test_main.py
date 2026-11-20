import unittest
from main import Solution


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.sol = Solution()

    def test_normal_convert(self):
        self.assertEqual(self.sol.number_to_thai(1), "หนึ่ง")
        self.assertEqual(self.sol.number_to_thai(10), "สิบ")
        self.assertEqual(self.sol.number_to_thai(21), "ยี่สิบเอ็ด")
        self.assertEqual(self.sol.number_to_thai(1000001), "หนึ่งล้านหนึ่ง")
        self.assertEqual(self.sol.number_to_thai(1000002), "หนึ่งล้านสอง")
        self.assertEqual(self.sol.number_to_thai(1000031), "หนึ่งล้านสามสิบเอ็ด")

    def test_error_case(self):
        self.assertEqual(
            self.sol.number_to_thai(100000000), "number can not more than 10000000"
        )
        self.assertEqual(
            self.sol.number_to_thai(-2), "number can not less than 0"
        )
        self.assertEqual(
            self.sol.number_to_thai("dummy_data"), "invalid input"
        )


if __name__ == "__main__":
    unittest.main()