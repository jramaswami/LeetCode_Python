"""
LeetCode
2028. Find Missing Observations
jramaswami
"""

class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        total_n = len(rolls) + n
        sigma_x = sum(rolls)
        expected_sigma_x = mean * total_n
        # Add a die roll of 1 for each of the missing observations
        sigma_x += n
        new_rolls = [1 for _ in range(n)]
        for i, _ in enumerate(new_rolls):
            # We can add a maximum of up to 5 to each die roll
            # But do not go over the expected value of the sum
            delta = min(5, expected_sigma_x - sigma_x)
            # We cannot have a negative roll
            delta = max(0, delta)
            new_rolls[i] += delta
            sigma_x += delta
        if sigma_x == expected_sigma_x:
            return new_rolls
        return []
