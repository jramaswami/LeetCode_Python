"""
LeetCode :: March 2021 Challenge :: Binary Tree With Factors
jramaswami
"""
from typing import *


MOD = pow(10, 9) + 7


class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        arr.sort()
        trees = dict()
        for p in arr:
            trees[p] = 1
            for a in arr:
                if a * a > p:
                    break
                for b in arr:
                    if a * b > p:
                        break
                    if p == a * b:
                        t = (trees[a] * trees[b]) % MOD
                        if a == b:
                            trees[p] = (trees[p] + t) % MOD
                        else:
                            t = (t * 2) % MOD
                            trees[p] = (trees[p] + t) % MOD

        soln = 0
        for t in trees.values():
            soln = (t + soln) % MOD
        return soln



def test_1():
    arr = [2, 4]
    assert Solution().numFactoredBinaryTrees(arr) == 3


def test_2():
    arr = [2, 4, 5, 10]
    assert Solution().numFactoredBinaryTrees(arr) == 7


def test_3():
    arr = [2,4,5,7,10,20,22,35]
    assert Solution().numFactoredBinaryTrees(arr) == 23


def test_4():
    arr = [2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    assert Solution().numFactoredBinaryTrees(arr) == 77
