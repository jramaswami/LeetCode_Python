"""
LeetCode :: September 2021 Challenge :: Intersection of Two Arrays II
jramaswami
"""


from collections import Counter


class Solution:

    def intersect(self, nums1, nums2):
        ctr1 = Counter(nums1)
        ctr2 = Counter(nums2)
        soln = []
        for k, v in (ctr1 & ctr2).items():
            soln.extend([k] * v)
        return soln


def test_1():
    nums1 = [1,2,2,1]
    nums2 = [2,2]
    expected = [2,2]
    assert sorted(Solution().intersect(nums1, nums2)) == sorted(expected)


def test_2():
    nums1 = [4,9,5]
    nums2 = [9,4,9,8,4]
    expected = [4,9]
    assert sorted(Solution().intersect(nums1, nums2)) == sorted(expected)


def test_3():
    nums1 = [28, 50, 95, 27, 99, 54, 7, 17, 58, 74, 32, 24, 35, 48, 45, 81, 36, 30, 52, 11, 34, 83, 24, 86, 20, 55, 50, 54, 45, 2, 13, 1, 21, 15, 34, 61, 76, 18, 65, 38, 30, 94, 85, 22, 12, 10, 80, 75, 55, 85, 16, 81, 88, 88, 66, 7, 14, 16, 95, 87, 48, 98, 87, 98, 52, 33, 47, 22, 90, 60, 76, 14, 88, 10, 55, 37, 80, 29, 22, 43, 92, 60, 9, 62, 27, 63, 8, 20, 46, 15, 52, 46, 89, 70, 86, 83, 54, 10, 86, 14]
    nums2 = [31, 58, 39, 16, 53, 89, 28, 67, 19, 81, 25, 17, 19, 57, 83, 40, 71, 22, 42, 87, 9, 66, 36, 79, 76, 61, 46, 85, 4, 78, 90, 80, 89, 51, 17, 16, 37, 56, 4, 1, 18, 92, 58, 13, 72, 71, 6, 17, 85, 29, 28, 71, 40, 20, 37, 25, 71, 67, 79, 77, 100, 60, 54, 40, 20, 95, 36, 52, 72, 3, 42, 38, 56, 32, 6, 16, 35, 85, 51, 78, 22, 30, 23, 60, 47, 65, 44, 99, 99, 67, 55, 87, 41, 18, 71, 67, 14, 46, 69, 80]
    expected = [58,16,89,28,81,17,83,22,87,9,66,36,76,61,46,85,90,80,16,37,1,18,92,13,85,29,20,60,54,20,95,52,38,32,35,22,30,60,47,65,99,55,87,14,46,80]
    assert sorted(Solution().intersect(nums1, nums2)) == sorted(expected)


def test_4():
    nums1 = [1,2,3]
    nums2 = [4,5,6]
    expected = []
    assert sorted(Solution().intersect(nums1, nums2)) == sorted(expected)
