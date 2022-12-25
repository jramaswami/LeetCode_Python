"""
LeetCode
2389. Longest Subsequence With Limited Sum
December 2022 Challenge
jramaswami
"""


import itertools
from typing import *


class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        prefix = list(itertools.accumulate(nums))

        def query(q):
            "Return the right-most index, i,  such that prefix[i] <= q."
            result = -1
            lo = 0
            hi = len(nums)-1
            while lo <= hi:
                mid = lo + ((hi - lo) // 2)
                if prefix[mid] <= q:
                    lo = mid + 1
                    result = max(result, mid)
                else:
                    hi = mid - 1
            return result

        return [1 + query(q) for q in queries]


def test_1():
    nums = [4,5,2,1]
    queries = [3,10,21]
    expected =[2,3,4]
    assert Solution().answerQueries(nums, queries) == expected


def test_2():
    nums = [2,3,4,5]
    queries = [1]
    expected = [0]
    assert Solution().answerQueries(nums, queries) == expected


