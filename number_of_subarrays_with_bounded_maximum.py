"""
LeetCode :: June 2021 Challenge :: Number of Subarrays with Bounded Maximum
jramaswami
"""


import heapq


class Solution:
    """
    We are given an array nums of positive integers, and two positive integers
    left and right (left <= right).

    Return the number of (contiguous, non-empty) subarrays such that the value
    of the maximum array element in that subarray is at least left and at most
    right.
    """
    def numSubarrayBoundedMax(self, nums, left, right):
        """Solve problem."""
        print(f"numSubarrayBoundedMax({nums=} {left=} {right=})")
        i = 0
        j = 0
        Q = []
        soln = 0
        while i < len(nums):
            # print(f"{i=} {j=}")
            while j < len(nums) and nums[j] <= right:
                heapq.heappush(Q, (-nums[j], j))
                if left <= -Q[0][0] <= right:
                    soln += 1
                    print(f"1 *** {nums[i:j+1]}")
                j += 1
            # j now points points to a number more than right or the end of the
            # array.  Move i right until it runs out of values greater than
            # left.
            k = None if j >= len(nums) else nums[j]
            # print(f"{k=} {i=} {j=} {Q=}")

            # We have already counted all subarrays starting at i, so move
            # forward one place.
            i += 1
            while i <= j:
                # Remove any items that came before i
                while Q and Q[0][1] < i:
                    heapq.heappop(Q)
                # print(f"{i=} {Q=}")
                if Q and -Q[0][0] >= left:
                    soln += 1
                    print(f"2 *** {nums[i:j]}")
                i += 1
            # Move j and i beyond the number that is too big.
            j += 1
            i = j
        return soln


def brute_force(nums, left, right):
    print(nums)
    soln = 0
    for i in range(len(nums)):
        for j in range(i+1, len(nums)+1):
            if left <= max(nums[i:j]) <= right:
                print(i, j, nums[i:j], max(nums[i:j]))
                soln += 1
    print('brute force solution', soln)


def test_1():
    """Sample test 1"""
    nums = [2, 1, 4, 3]
    left = 2
    right = 3
    assert Solution().numSubarrayBoundedMax(nums, left, right) == 3


def test_2():
    nums = [17, 7, 18, 11, 5, 12, 1, 2, 20, 14, 16, 8, 19, 6, 8, 14, 15, 11, 18, 11]
    # nums = [17, 7, 18, 11, 5, 12]
    left = 10
    right = 15
    brute_force(nums, left, right)
    assert Solution().numSubarrayBoundedMax(nums, left, right) == 25
