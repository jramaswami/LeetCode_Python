"""
LeetCode
860. Lemonade Change
August 2024 Challenge
jramaswami
"""


class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        fives = 0
        tens = 0
        for x in bills:
            if x == 5:
                fives += 1
            elif x == 10:
                if fives == 0:
                    return False
                fives -= 1
                tens += 1
            elif x == 20:
                if tens == 0:
                    if fives < 3:
                        return False
                    fives -= 3
                else:
                    if fives == 0:
                        return False
                    tens -= 1
                    fives -= 1
        return True