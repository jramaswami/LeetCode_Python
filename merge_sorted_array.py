"""
LeetCode :: June 2022 Challenge :: Merge Sorted Array
jramaswami
"""


class Solution:
    def merge(self, A, m, B, n):
        m -= 1
        n -= 1
        i = len(A) - 1
        while m >= 0 and n >= 0:
            if A[m] > B[n]:
                A[i] = A[m]
                m -= 1
                i -= 1
            else:
                A[i] = B[n]
                n -= 1
                i -= 1

        while m >= 0:
            A[i] = A[m]
            m -= 1
            i -= 1

        while n >= 0:
            A[i] = B[n]
            n -= 1
            i -= 1

        return A


def test_1():
    nums1 = [1,2,3,0,0,0]
    m = 3
    nums2 = [2,5,6]
    n = 3
    Solution().merge(nums1, m, nums2, n)
    assert nums1 == [1,2,2,3,5,6]


def test_2():
    nums1 = [1]
    m = 1
    nums2 = []
    n = 0
    Solution().merge(nums1, m, nums2, n)
    assert nums1 == [1]


def test_3():
    nums1 = [0]
    m = 0
    nums2 = [1]
    n = 1
    Solution().merge(nums1, m, nums2, n)
    assert nums1 == [1]


def test_4():
    nums1 = [0,0,0,0,0]
    m = 0
    nums2 = [1,2,3,4,5]
    n = 5
    Solution().merge(nums1, m, nums2, n)
    assert nums1 == [1,2,3,4,5]
