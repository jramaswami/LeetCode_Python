"""
LeetCode
2337. Move Pieces to Obtain a String
December 2024 Challenge
jramaswami
"""


import collections


class Solution:
    def canChange(self, start: str, target: str) -> bool:
        # Character freqs must match
        start_freqs = collections.Counter(start)
        target_freqs = collections.Counter(target)
        if start_freqs != target_freqs:
            return False

        # How many rights to the left of the current index
        start_right = [0 for _ in start]
        curr = 0
        for i, x in enumerate(start):
            if x == 'R':
                curr += 1
            elif x == 'L':
                curr = 0
            start_right[i] = curr

        target_right = [0 for _ in target]
        curr = 0
        for i, x in enumerate(target):
            if x == 'R':
                curr += 1
            elif x == 'L':
                curr = 0
            target_right[i] = curr

        # How many lefts to the right of current index
        start_left = [0 for _ in start]
        curr = 0
        for i in range(len(start) - 1, -1, -1):
            x = start[i]
            if x == 'R':
                curr = 0
            elif x == 'L':
                curr += 1
            start_left[i] = curr

        target_left = [0 for _ in target]
        curr = 0
        for i in range(len(target) - 1, -1, -1):
            x = target[i]
            if x == 'R':
                curr = 0
            elif x == 'L':
                curr += 1
            target_left[i] = curr

        print(start_left)
        print(target_left)
        print(start_right)
        print(target_right)
        # Do this for start and target.  For letter, appropriate freq must be gte target
        for i, x in enumerate(target):
            if x == 'L':
                if start_left[i] < target_left[i]:
                    return False
            elif x == 'R':
                if start_right[i] < target_right[i]:
                    return False
        return True
