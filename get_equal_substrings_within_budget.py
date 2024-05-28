"""
LeetCode
1208. Get Equal Substrings Within Budget
May 2024 Challenge
jramaswami
"""



class Solution:
    def equalSubstring(self, s: str, t: str, max_cost: int) -> int:
        soln = 0
        left = 0
        right = 0
        curr_cost = 0
        while right < len(s):
            # Add the right index.
            curr_cost += abs(ord(s[right]) - ord(t[right]))
            right += 1

            # Pop left while the cost is too high
            while curr_cost > max_cost:
                curr_cost -= abs(ord(s[left]) - ord(t[left]))
                left += 1

            soln = max(soln, right - left)

        return soln


def test_1():
    s = "abcd"
    t = "bcdf"
    maxCost = 3
    expected = 3
    result = Solution().equalSubstring(s, t, maxCost)
    assert result == expected


def test_2():
    s = "abcd"
    t = "cdef"
    maxCost = 3
    expected = 1
    result = Solution().equalSubstring(s, t, maxCost)
    assert result == expected


def test_3():
    s = "abcd"
    t = "acde"
    maxCost = 0
    expected = 1
    result = Solution().equalSubstring(s, t, maxCost)
    assert result == expected


def test_4():
    "WA"
    s = "krrgw"
    t = "zjxss"
    maxCost = 19
    expected = 2
    result = Solution().equalSubstring(s, t, maxCost)
    assert result == expected
