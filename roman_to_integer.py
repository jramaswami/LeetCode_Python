"""
LeetCode :: Roman to Integer
jramaswami
"""
class Solution:
    def romanToInt(self, s: str) -> int:
        value_of = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 
                    'C': 100, 'D': 500, 'M': 1000
        }

        soln = 0
        i = 0
        while i < len(s):
            if i + 1 < len(s):
                if value_of[s[i]] < value_of[s[i+1]]:
                    # E.g. IV
                    soln += (value_of[s[i+1]] - value_of[s[i]])
                    i += 2
                else:
                    soln += value_of[s[i]]
                    i += 1
            else:
                soln += value_of[s[i]]
                i += 1
        return soln


def test_1():
    assert Solution().romanToInt("III") == 3

def test_2():
    assert Solution().romanToInt("IV") == 4

def test_3():
    assert Solution().romanToInt("IX") == 9

def test_4():
    assert Solution().romanToInt("LVIII") == 58

def test_5():
    assert Solution().romanToInt("MCMXCIV") == 1994
