import unittest
from solution import Solution  # Import the Solution class

class TestCombinationSumII(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_case_1(self):
        candidates = [10, 1, 2, 7, 6, 1, 5]
        target = 8
        expected = [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]
        self.assertCountEqual(self.solution.combinationSum2(candidates, target), expected)

    def test_case_2(self):
        candidates = [2, 5, 2, 1, 2]
        target = 5
        expected = [[1, 2, 2], [5]]
        self.assertCountEqual(self.solution.combinationSum2(candidates, target), expected)

    def test_case_3(self):
        candidates = [3, 1, 3, 5, 1]
        target = 8
        expected = [[1, 1, 3, 3], [3, 5]]
        self.assertCountEqual(self.solution.combinationSum2(candidates, target), expected)

    def test_case_4(self):
        candidates = [4, 3, 2, 7]
        target = 10
        expected = [[3, 7]]
        self.assertCountEqual(self.solution.combinationSum2(candidates, target), expected)

if __name__ == "__main__":
    unittest.main()