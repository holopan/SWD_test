import unittest
from main import Solution


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.sol = Solution()

    def test_normal_list(self):
        self.assertEqual(self.sol.find_max_index([1,2,1,3,5,6,4]), 5)
        self.assertEqual(self.sol.find_max_index([1]), 0)
        self.assertEqual(self.sol.find_max_index([-1,-2,-1,-3,-5,-6,-4]), 0)

    def test_error_case(self):
        self.assertEqual(
            self.sol.find_max_index([]), "list can not blank"
        )
        self.assertEqual(
            self.sol.find_max_index(2), "please only enter list of numbers"
        )
        self.assertEqual(
            self.sol.find_max_index([1,2,1,3,5,6,"T"]), "please only enter list of numbers"
        )


if __name__ == "__main__":
    unittest.main()