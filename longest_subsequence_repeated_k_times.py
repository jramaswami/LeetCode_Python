"""
LeetCode
2014. Longest Subsequence Repeated k Times
June 2025 Challenge
jramaswami

Thank You Larry!
"""


import collections


class Solution:
    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        letters = list(sorted(set(s)))

        def calculate(current):
            """Count how many times subsequence appears in s
            """
            index = 0
            count = 0
            for i, char in enumerate(s):
                if char == current[index]:
                    index += 1
                if index >= len(current):
                    count += 1
                    index = 0
            return count

        soln = ""
        queue = collections.deque()
        queue.append("")
        while queue:
            current = queue.popleft()
            for next_char in letters:
                current0 = current + next_char
                if calculate(current0) >= k:
                    queue.append(current0)
            soln = current
        return soln


def test_1():
    s = "letsleetcode"
    k = 2
    expected = "let"
    assert Solution().longestSubsequenceRepeatedK(s, k) == expected


def test_2():
    s = "bb"
    k = 2
    expected = "b"
    assert Solution().longestSubsequenceRepeatedK(s, k) == expected


def test_3():
    s = "ab"
    k = 2
    expected = ""
    assert Solution().longestSubsequenceRepeatedK(s, k) == expected