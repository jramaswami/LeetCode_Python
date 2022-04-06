"""
LeetCode :: April 2022 Challenge :: 3Sum With Multiplicity
jramaswami
"""


import collections
import bisect


class Solution:
    def threeSumMulti(self, arr, target):
        MOD = pow(10, 9) + 7
        locs = collections.defaultdict(list)
        for i, n in enumerate(arr):
            locs[n].append(i)

        soln = 0
        for i, n in enumerate(arr):
            for j, m in enumerate(arr[i+1:], start=i+1):
                d = target - n - m
                if d in locs:
                    k = len(locs[d]) - bisect.bisect_right(locs[d], j)
                    soln = (soln + k) % MOD
        return soln



def test_1():
    arr = [1,1,2,2,3,3,4,4,5,5]
    target = 8
    assert Solution().threeSumMulti(arr, target) == 20

def test_2():
    arr = [1,1,2,2,2,2]
    target = 5
    assert Solution().threeSumMulti(arr, target) == 12

def test_3():
    arr = [0,0,0]
    target = 0
    assert Solution().threeSumMulti(arr, target) == 1

def test_4():
    arr = [2,1,3]
    target = 6
    assert Solution().threeSumMulti(arr, target) == 1
