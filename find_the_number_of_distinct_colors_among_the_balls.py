"""
LeetCode
3160. Find the Number of Distinct Colors Among the Balls
February 2025 Challenge
jramaswami
"""


import collections


class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        balls_by_color = collections.defaultdict(set)
        colors = collections.defaultdict(lambda: -1)
        distinct_colors = 0
        soln = []
        for ball, curr_ball_color in queries:
            if colors[ball] >= 0:
                prev_ball_color = colors[ball]
                balls_by_color[prev_ball_color].remove(ball)
                if len(balls_by_color[prev_ball_color]) == 0:
                    distinct_colors -= 1
                    del balls_by_color[prev_ball_color]
            if len(balls_by_color[curr_ball_color]) == 0:
                distinct_colors += 1
            colors[ball] = curr_ball_color
            balls_by_color[curr_ball_color].add(ball)
            soln.append(distinct_colors)
        return soln        
