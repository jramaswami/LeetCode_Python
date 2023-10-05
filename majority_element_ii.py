"""
LeetCode
229. Majority Element II
October 2023 Challenge
jramaswami
"""


from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # Misra-Gries Heavy Hitters Algorithm
        heavy_hitter1 = [0, 0]
        heavy_hitter2 = [0, 0]
        for n in nums:
            if n == heavy_hitter1[0] or n == heavy_hitter2[0]:
                # N is in the heavy hitters, increment by 1
                if n == heavy_hitter1[0]:
                    heavy_hitter1[1] += 1
                elif n == heavy_hitter2[0]:
                    heavy_hitter2[1] += 1
            else:
                # Replace if any are zero or less
                if heavy_hitter1[1] <= 0:
                    heavy_hitter1 = [n, 1]
                elif heavy_hitter2[1] <= 0:
                    heavy_hitter2 = [n, 1]
                # Otherwise, decrement current heavy hitters
                else:
                    heavy_hitter1[1] -= 1
                    heavy_hitter2[1] -= 1
            print(heavy_hitter1, heavy_hitter2, n)
        # Check to make sure heavy hitters have frequency greater than
        # len(nums) // 3
        heavy_hitter1[1] = heavy_hitter2[1] = 0
        for n in nums:
            if n == heavy_hitter1[0]:
                heavy_hitter1[1] += 1
            elif n == heavy_hitter2[0]:
                heavy_hitter2[1] += 1

        k = len(nums) // 3
        return [hh[0] for hh in [heavy_hitter1, heavy_hitter2] if hh[1] > k]


def test_1():
    nums = [3,2,3]
    expected = [3]
    assert sorted(Solution().majorityElement(nums)) == sorted(expected)


def test_2():
    nums = [1]
    expected = [1]
    assert sorted(Solution().majorityElement(nums)) == sorted(expected)


def test_3():
    nums = [1,2]
    expected = [1,2]
    assert sorted(Solution().majorityElement(nums)) == sorted(expected)


def test_4():
    nums = [1,2,3,4]
    expected = []
    assert sorted(Solution().majorityElement(nums)) == sorted(expected)


def test_5():
    nums = [1,2,3,1,3,1,2,1]
    expected = [1]
    assert sorted(Solution().majorityElement(nums)) == sorted(expected)