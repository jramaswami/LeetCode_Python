"""
LeetCode
912. Sort an Array
March 2023 Challenge
jramaswami
"""


from typing import *


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        aux = list(nums)
        nums0 = list(nums)

        def merge(lo, mid, hi):
            i = lo
            j = mid+1
            k = lo
            while i <= mid and j <= hi:
                if nums0[i] <= nums0[j]:
                    aux[k] = nums0[i]
                    i += 1
                    k += 1
                else:
                    aux[k] = nums0[j]
                    j += 1
                    k += 1
            while i <= mid:
                aux[k] = nums0[i]
                i += 1
                k += 1
            while j <= hi:
                aux[k] = nums0[j]
                j += 1
                k += 1
            nums0[lo:hi+1] = aux[lo:hi+1]

        def mergesort(lo, hi):
            if lo == hi:
                return

            mid = lo + ((hi - lo) // 2)
            mergesort(lo, mid)
            mergesort(mid+1, hi)
            merge(lo, mid, hi)

        mergesort(0, len(nums0) - 1)
        return nums0


import random


def test_random():
    limit = 5 * pow(10, 4)
    for _ in range(10):
        nums = [random.randint(-limit, limit) for _ in range(random.randint(1, limit))]
        assert sorted(nums) == Solution().sortArray(nums)