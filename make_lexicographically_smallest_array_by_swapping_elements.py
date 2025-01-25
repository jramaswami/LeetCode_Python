"""
LeetCode
2948. Make Lexicographically Smallest Array by Swapping Elements
January 2025 Challenge
jramaswami
"""


from typing import List


class UnionFind:
    def __init__(self, N):
        self.N = N
        self.id = list(range(N))
        self.size = [1 for _ in self.id]

    def get_id(self, u):
        if self.id[u] != u:
            self.id[u] = self.get_id(self.id[u])
        return self.id[u]

    def union(self, a, b):
        a = self.get_id(a)
        b = self.get_id(b)
        if a != b:
            if self.size[a] < self.size[b]:
                a, b = b, a
            self.size[a] += self.size[b]
            self.id[b] = self.id[a]
            self.N -= 1
    
    def __len__(self):
        return self.N


class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        # Find all numbers that can be swapped with each other
        uf = UnionFind(len(nums))
        nums0 = sorted((x, i) for i, x in enumerate(nums))
        print(nums0)
        for i, _ in enumerate(nums0[:-1]):
            x, y = nums0[i][0], nums0[i+1][0]
            if abs(x - y) <= limit:
                # These two numbers can be swapped
                uf.union(nums0[i][1], nums0[i+1][1])
        # Find order for each connected components
        component_values = dict()
        component_indexes = dict()
        for x, i in nums0:
            cid = uf.get_id(i)
            if cid not in component_indexes:
                component_values[cid] = []
                component_indexes[cid] = []
            component_values[cid].append(x)
            component_indexes[cid].append(i)
        soln = [None for _ in nums]
        for cid in component_indexes:
            for x, i in zip(sorted(component_values[cid]), sorted(component_indexes[cid])):
                soln[i] = x
        return soln


def test1():
    nums = [1,5,3,9,8]
    limit = 2
    expected = [1,3,5,8,9]
    assert Solution().lexicographicallySmallestArray(nums, limit) == expected


def test2():
    nums = [1,7,6,18,2,1]
    limit = 3
    expected = [1,6,7,18,1,2]
    assert Solution().lexicographicallySmallestArray(nums, limit) == expected
