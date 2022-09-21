"""
LeetCode :: September 2022 Challenge :: 985. Sum of Even Numbers After Queries
jramaswami
"""


from typing import *


class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:

        def is_even(k):
            return k % 2 == 0

        def is_odd(k):
            return k % 2 == 1

        curr_even_sum = sum(n for n in nums if is_even(n))
        soln = []
        for x, i in queries:
            # We are going to add x to nums[i].
            y = nums[i] + x
            if is_even(nums[i]) and is_even(y):
                # Even -> Even: add the difference between nums[i] and y = x.
                curr_even_sum += x
            elif is_even(nums[i]) and is_odd(y):
                # Even -> Odd: subtract nums[i]
                curr_even_sum -= nums[i]
            elif is_odd(nums[i]) and is_even(y):
                # Odd -> Even: add y
                curr_even_sum += y
            else:
                # Odd -> Odd: nothing to do
                pass
            nums[i] = y
            soln.append(curr_even_sum)

        return soln


def test_1():
    nums = [1,2,3,4]
    queries = [[1,0],[-3,1],[-4,0],[2,3]]
    expected = [8,6,2,4]
    assert Solution().sumEvenAfterQueries(nums, queries) == expected


def test_2():
    nums = [1]
    queries = [[4,0]]
    expected = [0]
    assert Solution().sumEvenAfterQueries(nums, queries) == expected