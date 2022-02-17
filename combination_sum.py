"""
LeetCode :: February 2022 Challenge :: 39. Combination Sum
jramawami
"""


class Solution:
    def combinationSum(self, candidates, target):

        def solve(index, curr_spec, curr_sum, acc):
            if index >= len(candidates):
                if curr_sum == target:
                    elems = []
                    for k, n in zip(curr_spec, candidates):
                        for _ in range(k):
                            elems.append(n)
                    acc.append(elems)
                return

            solve(index + 1, curr_spec, curr_sum, acc)
            n = candidates[index]
            while curr_sum <= target:
                curr_sum += n
                curr_spec[index] += 1
                solve(index + 1, curr_spec, curr_sum, acc)
            curr_spec[index] = 0

        curr_spec = [0 for _ in candidates]
        acc = []
        solve(0, curr_spec, 0, acc)
        return acc


def test_1():
    candidates = [2,3,6,7]
    target = 7
    expected = [[2,2,3],[7]]
    result = Solution().combinationSum(candidates, target)
    assert sorted(result) == sorted(expected)
