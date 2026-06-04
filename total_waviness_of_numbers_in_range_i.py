"""
LeetCode
3751. Total Waviness of Numbers in Range I
June 2026 Challenge
jramaswami
"""


class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        def waviness(n):
            digits = [int(x) for x in str(n)]
            if len(digits) < 3:
                return 0
            result = 0
            for i, _ in enumerate(digits[1:-1], start=1):
                a, b, c = digits[i-1:i+2]
                if b > a and b > c:
                    # Peak
                    result += 1
                if b < a and b < c:
                    # Valley
                    result += 1
            return result

        return sum(waviness(n) for n in range(num1, num2+1))