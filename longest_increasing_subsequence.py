"""
LeetCode :: August 2022 Challenge :: Longest Increasing Subsequence
jramaswami
"""


class Solution:
    def lengthOfLIS(self, nums):

        def search(A, x):
            "Return the index of the leftmost item A[i] >= x."
            lo = 0
            hi = len(A) - 1
            result = len(A)
            while lo <= hi:
                mid = lo + ((hi - lo) // 2)
                if A[mid] >= x:
                    result = min(result, mid)
                    hi = mid - 1
                else:
                    lo = mid + 1
            return result

        A = [nums[0]]
        for n in nums[1:]:
            i = search(A, n)
            if i == len(A):
                A.append(n)
            else:
                A[i] = n
        return len(A)


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
