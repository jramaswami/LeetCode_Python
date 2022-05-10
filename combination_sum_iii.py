"""
LeetCode :: May 2022 Challenge :: 216. Combination Sum III
jramaswami
"""


class Solution:

    def combinationSum3(self, k, n):

        def solve(i, sum_acc, nums_acc, limit, target, soln):
            # Base cases
            if len(nums_acc) == limit:
                if sum_acc == target:
                    soln.append(list(nums_acc))
                return

            if i > 9:
                return

            if sum_acc > 9:
                return

            # With i
            nums_acc.append(i)
            solve(i + 1, sum_acc + i, nums_acc, limit, target, soln)
            nums_acc.pop()
            # Without i
            solve(i + 1, sum_acc, nums_acc, limit, target, soln)

        soln = []
        nums_acc = []
        solve(1, 0, nums_acc, k, n, soln)
        return soln


def test_1():
    k = 3
    n = 7
    expected = [[1,2,4]]
    result = Solution().combinationSum3(k, n)
    assert sorted(result) == sorted(expected)


def test_2():
    k = 3
    n = 9
    expected = [[1,2,6],[1,3,5],[2,3,4]]
    result = Solution().combinationSum3(k, n)
    assert sorted(result) == sorted(expected)


def test_3():
    k = 4
    n = 1
    expected = []
    result = Solution().combinationSum3(k, n)
    assert sorted(result) == sorted(expected)


def test_4():
    "WA"
    k = 9
    n = 45
    expected = [[1,2,3,4,5,6,7,8,9]]
    result = Solution().combinationSum3(k, n)
    assert sorted(result) == sorted(expected)