"""
LeetCode
1267. Count Servers that Communicate
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
    def countServers(self, grid: List[List[int]]) -> int:
        # How many computers are there?
        N = 0
        computers_by_row = [[] for _ in grid]
        computers_by_col = [[] for _ in grid[0]]

        for r, row in enumerate(grid):
            for c, val in enumerate(row):
                if val == 1:
                    computers_by_row[r].append(N)
                    computers_by_col[c].append(N)
                    N += 1

        uf = UnionFind(N)
        for row in computers_by_row:
            if len(row) > 1:
                x = row[0]
                for y in row[1:]:
                    uf.union(x, y)

        for col in computers_by_col:
            if len(col) > 1:
                x = col[0]
                for y in col[1:]:
                    uf.union(x, y)

        soln = N
        for x in range(N):
            y = uf.get_id(x)
            print(x, y, uf.size[x])
            if y == x and uf.size[y] == 1:
                soln -= 1
        return soln



def test_1():
    grid = [[1,0],[0,1]]
    expected = 0
    assert Solution().countServers(grid) == expected


def test_2():
    grid = [[1,0],[1,1]]
    expected = 3
    assert Solution().countServers(grid) == expected
    

def test_3():
    grid = [[1,1,0,0],[0,0,1,0],[0,0,1,0],[0,0,0,1]]
    expected = 4
    assert Solution().countServers(grid) == expected
