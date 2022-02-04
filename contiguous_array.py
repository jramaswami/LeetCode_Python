"""
LeetCode :: February 2022 Challenge :: 525. Contiguous Array
jramaswami
"""


class Solution:

    def findMaxLength(self, nums):
        soln = 0
        curr_sum = 0
        prev_sums = dict()
        prev_sums[0] = 0
        for i, n in enumerate(nums):
            if n:
                curr_sum += 1
            else:
                curr_sum -= 1

            # curr_sum - prev_sum = 0
            # curr_sum = prev_sum
            if curr_sum == 0:
                soln = max(soln, i + 1)
            elif curr_sum in prev_sums:
                soln = max(soln, i - prev_sums[curr_sum])

            if curr_sum not in prev_sums:
                prev_sums[curr_sum] = i

        return soln


def test_1():
    nums = [0,1]
    expected = 2
    assert Solution().findMaxLength(nums) == expected


def test_2():
    nums = [0,1,0]
    expected = 2
    assert Solution().findMaxLength(nums) == expected


def test_3():
    nums = [0, 0, 0, 1, 0, 1, 0, 1, 1, 0]
    expected = 8
    assert Solution().findMaxLength(nums) == expected

