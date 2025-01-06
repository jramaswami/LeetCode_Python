"""
LeetCode
1769. Minimum Number of Operations to Move All Balls to Each Box
January 2025 Challenge
jramaswami
"""


class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        # How many left?  How many right?
        # Prefix sum      Suffix sum
        prefix = [0 for _ in boxes]
        curr = 0
        for i, x in enumerate(boxes):
            if i > 0:
                # Every previous box moves one space more than it moved previously
                prefix[i] = prefix[i-1]
                prefix[i] += curr
            # If there is a new box add it to current
            curr += int(x)

        suffix = [0 for _ in boxes]
        curr = 0
        for i in range(len(boxes) - 1, -1, -1):
            x = boxes[i]
            if i < len(boxes) - 1:
                # Every previous box moves one space more than it moved previously
                suffix[i] = suffix[i+1]
                suffix[i] += curr
            # If there is a new box add it to current
            curr += int(x)

        return [p + s for p, s in zip(prefix, suffix)]
