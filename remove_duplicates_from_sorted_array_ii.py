"""
LeetCode :: February Challenge 2022 :: 80. Remove Duplicates from Sorted Array II
jramaswami
"""


class Solution:
    def removeDuplicates(self, nums):
        # Find any elems that are third, fourth, ...
        # Mark them for removal by changing them to None.
        # O(N)
        curr_count = 1
        curr_value = nums[0]
        removals = 0
        for i, n in enumerate(nums[1:], start=1):
            if n == curr_value:
                curr_count += 1
                if curr_count > 2:
                    nums[i] = None
                    removals += 1
            else:
                curr_value, curr_count = n, 1

        # Swap the removed items to the end.
        # O(N)
        left = 0
        right = 0
        while right < len(nums):
            if nums[right] is None:
                right += 1
            else:
                nums[left] = nums[right]
                left += 1
                right += 1

        return len(nums) - removals


def test_1():
    nums = [1,1,1,2,2,3]
    expected_k = 5
    expected_nums = [1,1,2,2,3,None]
    result = Solution().removeDuplicates(nums)
    assert result == expected_k
    for i in range(expected_k):
        assert nums[i] == expected_nums[i]


def test_2():
    nums = [0,0,1,1,1,1,2,3,3]
    expected_k = 7
    expected_nums = [0,0,1,1,2,3,3,None,None]
    result = Solution().removeDuplicates(nums)
    assert result == expected_k
    for i in range(expected_k):
        assert nums[i] == expected_nums[i]
