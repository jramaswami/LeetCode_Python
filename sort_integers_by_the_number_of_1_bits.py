"""
LeetCode
1356. Sort Integers by The Number of 1 Bits
October 2023 Challenge
jramaswami
"""


from typing import List


class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:

        def popcount(n):
            bits = 0
            while n:
                bits += n & 1
                n >>= 1
            return bits

        arr0 = [(popcount(n), n) for n in arr]
        arr0.sort()
        return [t[1] for t in arr0]



def test_1():
    arr = [0,1,2,3,4,5,6,7,8]
    expected = [0,1,2,4,8,3,5,6,7]
    assert Solution().sortByBits(arr) == expected


def test_2():
    arr = [1024,512,256,128,64,32,16,8,4,2,1]
    expected = [1,2,4,8,16,32,64,128,256,512,1024]
    assert Solution().sortByBits(arr) == expected