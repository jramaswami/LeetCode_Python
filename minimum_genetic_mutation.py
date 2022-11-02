"""
LeetCode :: 433. Minimum Genetic Mutation
December 2022 Challenge
jramaswami
"""


from typing import *
import collections
import itertools


class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        # Start gene should be assumed as valid (so add it to the bank).
        bank.append(start)
        bank0 = set(bank)

        adj = collections.defaultdict(list)
        for g, h in itertools.combinations(bank0, 2):
            if sum(a != b for a, b in zip(g, h)) == 1:
                adj[g].append(h)
                adj[h].append(g)

        visited = set()
        visited.add(start)
        queue = collections.deque([(start, 0)])
        while queue:
            g, d = queue.popleft()
            if g == end:
                return d
            for h in adj[g]:
                if h not in visited:
                    visited.add(h)
                    queue.append((h, d+1))
        return -1


def test_1():
    start = "AACCGGTT"
    end = "AACCGGTA"
    bank = ["AACCGGTA"]
    expected = 1
    assert Solution().minMutation(start, end, bank) == expected


def test_2():
    start = "AACCGGTT"
    end = "AAACGGTA"
    bank = ["AACCGGTA","AACCGCTA","AAACGGTA"]
    expected = 2
    assert Solution().minMutation(start, end, bank) == expected


def test_3():
    start = "AAAAACCC"
    end = "AACCCCCC"
    bank = ["AAAACCCC","AAACCCCC","AACCCCCC"]
    expected = 3
    assert Solution().minMutation(start, end, bank) == expected


def test_4():
    "WA"
    start = "AACCGGTT"
    end = "AACCGGTA"
    bank = []
    expected = -1
    assert Solution().minMutation(start, end, bank) == expected