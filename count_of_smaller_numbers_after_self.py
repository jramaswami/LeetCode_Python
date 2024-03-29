"""
LeetCode :: July 2022 Challenge :: ount of Smaller Numbers After Self
jramaswami
"""


import collections


Item = collections.namedtuple('Item', ['value', 'index'])


class Solution:
    def countSmaller(self, nums):
        nums0 = [Item(n, i) for i, n in enumerate(nums)]
        soln = [0 for _ in nums]
        aux = list(nums0)

        def count_inversions(left, mid, right):
            boundary = mid+1
            for item in nums0[left:mid+1]:
                # Move boundary to the first item greater than or equal to
                # item.value.  All the items before the boundary are inversions.
                while boundary <= right and nums0[boundary].value < item.value:
                    boundary += 1
                soln[item.index] += boundary - (mid + 1)

        def merge(left, mid, right):
            count_inversions(left, mid, right)
            i = k = left
            j = mid + 1
            while i <= mid and j <= right:
                if nums0[i].value <= nums0[j].value:
                    aux[k] = nums0[i]
                    i += 1
                else:
                    aux[k] = nums0[j]
                    j += 1
                k += 1

            while i <= mid:
                aux[k] = nums0[i]
                i += 1
                k += 1

            while j <= right:
                aux[k] = nums0[j]
                j += 1
                k += 1

            nums0[left:right+1] = aux[left:right+1]

        def mergesort(left, right):
            if left >= right:
                return
            mid = left + ((right - left) // 2)
            mergesort(left, mid)
            mergesort(mid+1, right)
            merge(left, mid, right)

        mergesort(0, len(nums0)-1)
        return soln



def test_1():
    nums = [5,2,6,1]
    expected = [2,1,1,0]
    assert Solution().countSmaller(nums) == expected


def test_2():
    nums = [-1]
    expected = [0]
    assert Solution().countSmaller(nums) == expected


def test_3():
    nums = [-1, 1]
    expected = [0, 0]
    assert Solution().countSmaller(nums) == expected
