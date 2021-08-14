"""
LeetCode :: August 2021 Challenge :: Remove Boxes
jramaswami

Thank You Larry!
"""


from functools import lru_cache



class Solution:
    def removeBoxes(self, boxes):
        N = len(boxes)

        @lru_cache(None)
        def solve(left, right, count):
            """Recursive cached solution."""
            if left == right:
                return (count + 1) * (count + 1)
            if left > right:
                return 0

            best = solve(left + 1, right, 0) + ((count + 1) * (count + 1))

            for i in range(left+1, right+1):
                if boxes[i] == boxes[left]:
                    best = max(best, solve(left+1, i-1, 0) + solve(i, right, count+1))

            return best

        return solve(0, N-1, 0)


def test_1():
    boxes = [1,3,2,2,2,3,4,3,1]
    assert Solution().removeBoxes(boxes) == 23
