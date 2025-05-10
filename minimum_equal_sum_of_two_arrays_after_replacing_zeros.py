"""
LeetCode
2918. Minimum Equal Sum of Two Arrays After Replacing Zeros
May 2025 Challenge
jramaswami
"""


from typing import List


class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        sum1 = sum(nums1)
        zeros1 = sum(1 if x == 0 else 0 for x in nums1)
        sum2 = sum(nums2)
        zeros2 = sum(1 if x == 0 else 0 for x in nums2)
        minsum1 = sum1 + zeros1
        minsum2 = sum2 + zeros2
        if minsum1 > minsum2:
            if zeros2:
                return minsum1
        elif minsum1 < minsum2:
            if zeros1:
                return minsum2
        else:
            return minsum1
        return -1




def test_1():
    nums1 = [3,2,0,1,0]
    nums2 = [6,5,0]
    expected = 12
    assert Solution().minSum(nums1, nums2) == expected


def test_2():
    nums1 = [2,0,2,0]
    nums2 = [1,4]
    expected = -1
    assert Solution().minSum(nums1, nums2) == expected