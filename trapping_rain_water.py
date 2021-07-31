"""
LeetCode :: July 2021 Challenge :: Trapping Rain Water
jramaswami
"""


class Solution:
    def trap(self, heights):
        prefix = [0 for _ in heights]
        suffix = [0 for _ in heights]
        curr_height = 0
        for i, h in enumerate(heights):
            prefix[i] = curr_height
            curr_height = max(curr_height, h)

        curr_height = 0
        for off, h in enumerate(reversed(heights), start=1):
            i = len(heights) - off
            suffix[i] = curr_height
            curr_height = max(curr_height, h)

        soln = 0
        for h, left, right in zip(heights, prefix, suffix):
            delta = max(0, min(left, right) - h)
            soln += delta
        return soln



def test_1():
    heights = [0,1,0,2,1,0,1,3,2,1,2,1]
    expected = 6
    assert Solution().trap(heights) == expected


def test_2():
    heights = [4,2,0,3,2,5]
    expected = 9
    assert Solution().trap(heights) == expected
