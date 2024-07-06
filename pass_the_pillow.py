"""
LeetCode
2582. Pass the Pillow
July 2024 Challenge
jramaswami
"""


class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        curr_index = 1
        dirn = 1
        for _ in range(time):
            curr_index += dirn
            if curr_index == n:
                dirn = -1
            elif curr_index == 1:
                dirn = 1
        return curr_index
