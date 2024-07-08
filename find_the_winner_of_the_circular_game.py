"""
LeetCode
1823. Find the Winner of the Circular Game
July 2024 Challenge
jramaswami
"""


import collections


class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        people = collections.deque(range(1, n+1))
        while len(people) > 1:
            for _ in range(k-1):
                people.rotate(-1)
            people.popleft()
        return people[0]
