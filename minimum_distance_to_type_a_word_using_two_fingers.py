"""
LeetCode
1320. Minimum Distance to Type a Word Using Two Fingers
April 2026 Challenge
jramaswami
"""


import math
import string


class Solution:
    def minimumDistance(self, word: str) -> int:
        word0 = [ord(c) - ord('A') for c in word]

        row, col = 0, 0
        loc = []
        for letter in string.ascii_uppercase:
            loc.append((row, col))
            col += 1
            if col == 6:
                col = 0
                row = row + 1

        def dist(a, b):
            x1, y1 = loc[a]
            x2, y2 = loc[b]
            return abs(x1-x2) + abs(y1-y2)

        # dp[left hand letter][right hand letter]
        prev = [[0 for _ in range(26)] for _ in range(26)]
        curr = [[math.inf for _ in range(26)] for _ in range(26)]
        for target in word0:
            for left_hand in range(26):
                for right_hand in range(26):
                    # Move left hand from it's current position to target
                    curr[target][right_hand] = min(
                        curr[target][right_hand],
                        dist(left_hand, target) + prev[left_hand][right_hand]
                    )
                    # Move right hand from it's current position to target
                    curr[left_hand][target] = min(
                        curr[left_hand][target],
                        dist(right_hand, target) + prev[left_hand][right_hand]
                    )
            prev, curr = curr, [[math.inf for _ in range(26)] for _ in range(26)]

        return min(min(row) for row in prev)


def test_1():
    assert Solution().minimumDistance('CAKE') == 3
