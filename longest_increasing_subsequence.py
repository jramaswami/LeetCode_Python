"""
LeetCode :: July 2021 Challenge :: Longest Increasing Subsequence
jramaswami
"""


class Solution:
    def lengthOfLIS(self, nums):
        def search(A, x):
            """
            Return index of x or the index of the first value more than x.
            """
            lo = 0
            hi = len(A) - 1
            result_index = len(A)
            while lo <= hi:
                mid = lo + ((hi - lo) // 2)
                if x == A[mid]:
                    return mid
                elif x < A[mid]:
                    # A[mid] > x
                    result_index = min(result_index, mid)
                    hi = mid - 1
                else:
                    lo = mid + 1
            return result_index

        A = []
        soln = 0
        for n in nums:
            i = search(A, n)
            if i >= len(A):
                A.append(n)
            else:
                A[i] = n
            soln = max(soln, len(A))
        return soln


def test_1():
    nums = [10,9,2,5,3,7,101,18]
    expected = 4
    assert Solution().lengthOfLIS(nums) == expected


def test_2():
    nums = [0,1,0,3,2,3]
    expected = 4
    assert Solution().lengthOfLIS(nums) == expected


def test_3():
    nums = [7,7,7,7,7,7,7]
    expected = 1
    assert Solution().lengthOfLIS(nums) == expected
