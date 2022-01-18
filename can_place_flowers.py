"""
LeetCode :: January 2022 Challenge :: 605. Can Place Flowers
jramaswami
"""


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:

        def get(i):
            if i < 0 or i >= len(flowerbed):
                return 0
            return flowerbed[i]

        i = 0
        while i < len(flowerbed) and n > 0:
            if get(i-1) == 0 and get(i) == 0 and get(i+1) == 0:
                flowerbed[i] = 1
                n -= 1
            i += 1
        return n == 0
