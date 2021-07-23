"""
LeetCode :: Array Module :: Merge Sorted Array
jramaswami
"""


class Solution:
    def merge(self, A, m, B, n):
        """
        A different solution.  In place, O(m + n).
        """
        # Go in reverse.
        i = m - 1
        j = n - 1
        k = len(A) - 1
        while i >= 0 and j >= 0:
            if A[i] > B[j]:
                A[k] = A[i]
                i -= 1
                k -= 1
            else:
                A[k] = B[j]
                j -= 1
                k -= 1

        while i >= 0:
            A[k] = A[i]
            i -= 1
            k -= 1

        while j >= 0:
            A[k] = B[j]
            j -= 1
            k -= 1


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
