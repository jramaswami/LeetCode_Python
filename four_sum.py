"""
LeetCode :: July 2021 Challenge :: 4SUM
jramaswami
"""


from collections import defaultdict


class Solution():
    def fourSum(self, nums, target):
        # Dictionary of two-sums
        two_sum = defaultdict(list)
        for i, a in enumerate(nums):
            for j, b in enumerate(nums[i+1:], start=i+1):
                two_sum[a+b].append((i, j))

        soln = set()
        # For each two sum find the corresponding two sum to make the target.
        for m in sorted(two_sum):
            n = target - m
            # To prevent double counting, consider the second two sum only if
            # it is greater than the first two sum.
            if n > m and n in two_sum:
                for mi, mj in two_sum[m]:
                    for ni, nj in two_sum[n]:
                        if len(set([mi, mj, ni, nj])) == 4:
                            soln.add(tuple(sorted([nums[mi], nums[mj], nums[ni], nums[nj]])))
            # Special case where two sum is half the target.
            elif n == m:
                for x, _ in enumerate(two_sum[m]):
                    for y, _ in enumerate(two_sum[m][x+1:], start=x+1):
                        mi, mj = two_sum[m][x]
                        ni, nj = two_sum[m][y]
                        if len(set([mi, mj, ni, nj])) == 4:
                            soln.add(tuple(sorted([nums[mi], nums[mj], nums[ni], nums[nj]])))
        return [list(t) for t in soln]


def test_1():
    nums = [1,0,-1,0,-2,2]
    target = 0
    assert sorted(Solution().fourSum(nums, target)) == sorted([[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]])


def test_2():
    nums = [2,2,2,2,2]
    target = 8
    assert sorted(Solution().fourSum(nums, target)) == sorted([[2,2,2,2]])


def test_3():
    nums = [1, -8, -19, -9, 0, 19, 15, 10, -8, 15, -5, 1, -5, -5, 6, -4, 17, 11, -3, 8]
    target = 0
    expected = [[-19,-9,11,17],[-19,-8,8,19],[-19,-8,10,17],[-19,-4,6,17],[-19,-4,8,15],[-19,0,8,11],[-19,1,1,17],[-19,1,8,10],[-9,-8,0,17],[-9,-8,6,11],[-9,-5,-5,19],[-9,-5,-3,17],[-9,-5,6,8],[-9,-3,1,11],[-9,0,1,8],[-8,-8,-3,19],[-8,-8,1,15],[-8,-8,6,10],[-8,-5,-4,17],[-8,-4,-3,15],[-8,-4,1,11],[-8,-3,0,11],[-8,-3,1,10],[-8,1,1,6],[-5,-5,-5,15],[-5,-5,0,10],[-5,-4,1,8],[-5,-3,0,8],[-4,-3,1,6]]
    expected.sort()
    result = sorted(Solution().fourSum(nums, target))
    print(result)
    print(expected)
    assert result == expected


def test_4():
    nums = [1, -8, -19, -9, 0, 19, 15, 10, -8, 15, -5, 1, -5, -5, 6, -4, 17, 11, -3, 8]
    target = -3
    result = sorted(Solution().fourSum(nums, target))
    expected = [[-19,-9,6,19],[-19,-9,8,17],[-19,-9,10,15],[-19,-5,6,15],[-19,-5,10,11],[-19,-4,1,19],[-19,-3,0,19],[-19,-3,8,11],[-19,0,1,15],[-19,0,6,10],[-9,-8,-5,19],[-9,-8,-3,17],[-9,-8,6,8],[-9,-5,-4,15],[-9,-5,0,11],[-9,-5,1,10],[-9,-4,0,10],[-9,-3,1,8],[-8,-8,-4,17],[-8,-5,-5,15],[-8,-5,0,10],[-8,-4,1,8],[-8,-3,0,8],[-5,-5,-4,11],[-5,-5,-3,10],[-5,-5,1,6],[-5,-4,0,6],[-5,0,1,1]]
    expected.sort()
    print(result)
    print(expected)
    assert result == expected
