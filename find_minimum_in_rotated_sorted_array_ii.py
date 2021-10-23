"""
LeetCode :: October 2021 Challenge :: 154. Find Minimum in Rotated Sorted Array II
jramaswami


We are looking for the minimum in the array.

(1) In a rotated array we are looking for a index i, such that
    nums[i-1] > nums[i] <= nums[i+1].  For example:
    4 5 6 1 2 3
          ^

    Be careful to wrap around, for example.
    2 3 4 5 6 1
              ^

(2) In a non-rated array we are looking for an index i, such that
    nums[-1] > nums[0] < nums[1].  For example:
    1 2 3 4 5 6
    ^

(3) What about duplicates?  The corner case would be an array with all
    the same numbers.  For example:
    2 2 2 2 2
    We could simply return -1 from our search function to indicate that
    neither of the first two cases was found, therefore the array is all
    duplicates of the same number, which we can then pick arbitrarily.

Worst case runtime is O(n) when all number are the same.
"""


class Solution:
    def findMin(self, nums):

        def search(lo, hi):
            """
            Return the index of the minimum value for the array if it is
            between nums[lo] and nums[hi].
            Return -1 if that value is not beween nums[lo] and nums[hi].
            """

            # Base case for recursion.
            if lo > hi:
                return -1

            mid = lo + ((hi - lo) // 2)

            # Case 2.
            if mid == 0 and nums[0] < nums[-1] and nums[0] > nums[1]:
                return 0

            # Case 1.
            if nums[mid-1] > nums[mid] and nums[mid] <= nums[(mid + 1) % len(nums)]:
                return mid

            return max(search(lo, mid - 1), search(mid + 1, hi))


        # If the index returned is -1, then we can choose an arbitrary number,
        # in this case the last element in num.  Otherwise we return the value
        # at the returned index.
        return nums[search(0, len(nums)-1)]


def test_1():
    nums = [1, 3, 5]
    assert Solution().findMin(nums) == 1


def test_2():
    nums = [2,2,2,0,1]
    assert Solution().findMin(nums) == 0


def test_3():
    nums = [2,2,2,2,2]
    assert Solution().findMin(nums) == 2


def test_4():
    nums = [2,3,4,5,6,1]
    assert Solution().findMin(nums) == 1


def test_random():
    import random
    import collections
    for _ in range(100):
        nums = collections.deque(sorted(random.randint(-1000, 1000) for _ in range(5000)))
        nums.rotate(random.randint(-1000, 1000))
        assert Solution().findMin(list(nums)) == min(nums)
