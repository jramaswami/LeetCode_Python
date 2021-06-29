"""
LeetCode :: June 2021 Challenge :: Max Consecutive Ones III
jramaswami
"""


from collections import deque


class Solution:
    def longestOnes(self, nums, k):
        # This is on O(n) solution as we will add each number to the
        # sequence and remove, at most, each number from the sequence.
        # Since we are keeping a separate sequence, we require O(n)
        # extra space.
        soln = 0
        seq = deque()
        zeros_in_seq = 0

        # Scan nums.
        for n in nums:
            # Append n to our current sequence.
            seq.append(n)
            if n == 0:
                zeros_in_seq += 1

            # Remove values from the left of the sequence until there are
            # less than k zeros in the sequence.
            while zeros_in_seq > k:
                removed = seq.popleft()
                if removed == 0:
                    zeros_in_seq -= 1

            # This is the longest sequence ending at this position with
            # less than k zeros.  Keep track of the longest solution as
            # we scan through nums.
            soln = max(soln, len(seq))

        return soln


def test_1():
    nums = [1,1,1,0,0,0,1,1,1,1,0]
    k = 2
    expected = 6
    assert Solution().longestOnes(nums, k) == expected


def test_2():
    nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
    k = 3
    expected = 10
    assert Solution().longestOnes(nums, k) == expected
