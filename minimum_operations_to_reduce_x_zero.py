"""
LeetCode :: June 2022 Challenge :: 1658. Minimum Operations to Reduce X to Zero
jramaswami
"""


import collections
import math


class Solution:

    def minOperations(self, nums, x):
        target_sum = sum(nums) - x
        window = collections.deque()
        curr_sum = 0
        soln = math.inf
        for n in nums:
            window.append(n)
            curr_sum += n
            while window and curr_sum > target_sum:
                curr_sum -= window[0]
                window.popleft()
            if curr_sum == target_sum:
                soln = min(soln, len(nums) - len(window))
        return (soln if soln < math.inf else -1)



def test_1():
    nums = [1,1,4,2,3]
    x = 5
    expected = 2
    assert Solution().minOperations(nums, x) == expected


def test_2():
    nums = [5,6,7,8,9]
    x = 4
    expected = -1
    assert Solution().minOperations(nums, x) == expected


def test_3():
    nums = [3,2,20,1,1,3]
    x = 10
    expected = 5
    assert Solution().minOperations(nums, x) == expected
