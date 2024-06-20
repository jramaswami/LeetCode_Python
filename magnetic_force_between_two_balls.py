"""
LeetCode
1552. Magnetic Force Between Two Balls
June 2024 Challenge
jramaswami
"""


class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()

        def check(min_force, ball_count):
            last_ball = position[0]
            balls_used = 1
            for p in position[1:]:
                if p - last_ball >= min_force:
                    balls_used += 1
                    last_ball = p
            return balls_used >= ball_count

        lo = 0
        hi = 1 + position[-1] - position[0]
        soln = 0
        while lo <= hi:
            mid = lo + ((hi - lo) // 2)
            if check(mid, m):
                soln = max(soln, mid)
                lo = mid + 1
            else:
                hi = mid - 1
        return soln
