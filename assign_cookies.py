"""
LeetCode
455. Assign Cookies
January 2024 Challenge
jramaswami
"""


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        greed_factor = list(sorted(g, reverse=True))
        cookie_size = list(sorted(s, reverse=True))

        gi = ci = soln = 0
        while gi < len(greed_factor) and ci < len(cookie_size):
            if cookie_size[ci] >= greed_factor[gi]:
                # Give the kid a cookie because it satisfies their greed factor
                soln += 1
                gi += 1
                ci += 1
            elif cookie_size[ci] < greed_factor[gi]:
                # This kid cannot be satisfied with any of the remaining cookies
                gi += 1
        return soln