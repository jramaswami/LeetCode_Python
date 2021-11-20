"""
LeetCode :: November 2021 Challenge :: 540. Single Element in a Sorted Array
jramaswami

Solve in O(log n) time and O(1) extra space.

Key observations:
(1) Any given index will be even or odd.
(2) Assume that the single element is to the right of any given index.  If the
    index is odd, then nums[index-1] will be the same number.  If the index is
    even, then nums[index-1] will be a different number.
(3) If (2) does not hold for the given index, then the single element is the
    element at the given index or is to the left of the given index.
"""


class Solution:

    def singleNonDuplicate(self, nums):

        # Corner case: array of length 1.
        if len(nums) == 1:
            return nums[0]

        def is_single_element(i):
            "Three different cases where nums[i] is the single element."
            if i == 0 and nums[i] < nums[i+1]:
                return True
            elif i == len(nums) - 1 and nums[i-1] < nums[i]:
                return True
            elif nums[i-1] < nums[i] < nums[i+1]:
                return True
            return False

        def single_element_to_right(i):
            "Two cases where single element is too the right."
            if i % 2:
                return nums[i-1] == nums[i]
            else:
                return nums[i] == nums[i+1]

        lo = 0
        hi = len(nums) - 1
        while lo <= hi:
            mid = lo + ((hi - lo) // 2)
            if is_single_element(mid):
                return nums[mid]
            elif single_element_to_right(mid):
                lo = mid + 1
            else:
                hi = mid - 1


def test_1():
    nums = [1,1,2,3,3,4,4,8,8]
    expected = 2
    assert Solution().singleNonDuplicate(nums) == expected


def test_2():
    nums = [3,3,7,7,10,11,11]
    expected = 10
    assert Solution().singleNonDuplicate(nums) == expected


def test_3():
    nums = [1]
    expected = 1
    assert Solution().singleNonDuplicate(nums) == expected


def test_4():
    nums = [1, 2, 2, 3, 3, 4, 4, 5, 5]
    expected = 1
    assert Solution().singleNonDuplicate(nums) == expected


def test_5():
    nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6]
    expected = 6
    assert Solution().singleNonDuplicate(nums) == expected