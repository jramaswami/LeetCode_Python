"""
Leetcode :: 1542. Find Longest Awesome Substring
https://leetcode.com/contest/biweekly-contest-32/problems/find-longest-awesome-substring/
"""
from math import inf

class Solution:
    def longestAwesome(self, s: str) -> int:
        # A substring of 1 is a palindrome.
        soln = 0
        # Minimum index of this bitmask's occurrence
        bitmask_occurred = [inf for _ in range(pow(2, 10))]
        # Zero occurs before the first letter of s.
        bitmask_occurred[0] = -1

        # Bit mask prefix
        mask = 0

        # Find the maximum length substring that can be a palindrome.
        for i, c in enumerate(s):
            # Convert c to a number
            n = ord(c) - ord('0')
            # Update bitmask prefix
            mask ^=  (1 << n)

            # Update bitmask's occurrence
            bitmask_occurred[mask] = min(bitmask_occurred[mask], i)

            # If we have seen this bitmask before, then the substring
            # between this occurrence and the minimum previous occurrence
            # is a palindrome.  This will catch *even* length substrings.
            soln = max(soln, i - bitmask_occurred[mask])

            # For odd length substrings, flip each on bit and see if that
            # bitmask occurred before.
            for b in range(10):
                soln = max(soln, i - bitmask_occurred[mask ^ (1 << b)])

        return soln


#
# Testing
#
import random
from collections import defaultdict


def is_palindromic(frequency):
    """
    A string can be rearranged into palindrome if there is one or no
    character with an odd frequency.
    """
    return sum(v % 2 for v in frequency.values()) <= 1


def longest_awesome(s: str) -> int:
    """TLE solution."""
    # sliding window
    for window_length in range(len(s), 0, -1):

        # count frequencies
        frequency = defaultdict(int)
        for c in s[:window_length]:
            frequency[c] += 1

        # check first window
        if is_palindromic(frequency):
            return window_length

        # slide window ...
        start = 1
        while start + window_length <= len(s):
            # shift window by 1
            frequency[s[start-1]] -= 1
            frequency[s[start+window_length-1]] += 1
            if is_palindromic(frequency):
                print(s[start:start+window_length])
                return window_length
            start += 1

    # This shouldn't happen because any substring of length 1 is palindromic.
    return -1


def test_samples():
    """Sample tests."""
    solver = Solution()
    ss = ["3242415", "12345678", "213123", "00"]
    exs = [5, 1, 6, 2]
    for s, ex in zip(ss, exs):
        assert solver.longestAwesome(s) == ex


def random_string(str_len):
    """Make a random string of digits of the given string length."""
    return "".join(str(random.randint(0, 9)) for _ in range(str_len))


def test_random():
    """Test random strings."""
    solver = Solution()
    str_len = 100
    test_cases = 100
    ss = [random_string(str_len) for _ in range(test_cases)]
    exs = [longest_awesome(s) for s in ss]
    for s, ex in zip(ss, exs):
        rs = solver.longestAwesome(s)
        if rs != ex:
            print('FAIL', s, ex, rs)
        assert  rs == ex