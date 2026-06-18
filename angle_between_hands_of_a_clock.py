"""
LeetCode
1344. Angle Between Hands of a Clock
June 2026 Challenge
jramaswami
"""


class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        hour %= 12
        degrees_per_hour = 360 / 12
        degrees_per_minute = 360 / 60
        hour_angle = hour * degrees_per_hour
        minutes_angle = minutes * degrees_per_minute
        # Adjust hour hand
        hour_angle += (degrees_per_hour * minutes / 60)
        a, b = hour_angle, minutes_angle
        if a > b: a, b = b, a
        soln = b - a
        if soln > 180:
            return 360 - soln
        return soln


EPS = pow(10, -5)


def test_79():
    "WA"
    hour, minutes, expected = 1, 57, 76.5
    assert abs(Solution().angleClock(hour, minutes) - expected) < EPS