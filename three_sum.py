"""
LeetCode :: October 2021 Challenge :: 15. 3Sum
jramaswami
"""


import collections


class Solution:
    def threeSum(self, nums):
        solns = []
        ctr = collections.Counter(nums)
        nums0 = list(sorted(ctr))
        for i, a in enumerate(nums0):
            # You can use the same number twice if there is at least two of
            # them.
            offset = 0 if ctr[a] > 1 else 1
            for k, b in enumerate(nums0[i+offset:], start=i+offset):
                c = -(a + b)
                if c < b:
                    continue
                if a == b == c:
                    if ctr[a] >= 3:
                        solns.append([a, b, c])
                elif b == c:
                    if ctr[b] >= 2:
                        solns.append([a, b, c])
                else:
                    if ctr[c] > 0:
                        solns.append([a, b, c])
        return solns







def test_1():
    nums = [-1,0,1,2,-1,-4]
    expected = [[-1,-1,2],[-1,0,1]]
    result = Solution().threeSum(nums)
    assert result == expected


def test_2():
    nums = []
    expected = []
    result = Solution().threeSum(nums)
    assert result == expected


def test_3():
    nums = [0]
    expected = []
    result = Solution().threeSum(nums)
    assert result == expected


def test_4():
    nums = [0] * 3000
    assert Solution().threeSum(nums) == [[0, 0, 0]]
