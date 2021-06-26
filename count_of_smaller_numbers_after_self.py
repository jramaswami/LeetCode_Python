"""
LeetCode :: June 2021 Challenge :: ount of Smaller Numbers After Self
jramaswami
"""


class Solution:
    def countSmaller(self, nums):
        """
        Use mergesort to O(n log n)
        """

        nums0 = [(-n, i) for i, n in enumerate(nums)]
        soln = [0 for _ in nums0]
        aux = list(nums0)

        def merge(left, mid, right):
            i = left
            j = mid + 1
            k = left
            new_arr = []
            while i <= mid and j <= right:
                if nums0[i][0] < nums0[j][0]:
                    aux[k] = nums0[i]
                    soln[nums0[i][1]] += (right - j + 1)
                    i += 1
                else:
                    # Inversion
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

            for k in range(left, right+1):
                nums0[k] = aux[k]

        def mergesort(left, right):
            # Base case
            if left >= right:
                return
            mid = (left + right) // 2
            mergesort(left, mid)
            mergesort(mid + 1, right)
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
