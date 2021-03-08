"""
leetcode :: Remove Palindromic Subsequences
jramaswami

There are only 'a' and 'b' in the string.  All subsequences made up entirely of
a single letter are palindromes.  

(1) The string contains 'a' and 'b'.  We could remove the all 'a' first and
    then all the 'b'.  This would be 2 operations.  This is the best that can
    be done, unless the string is already a palindrome.  If so, we can remove
    all letters in a single operation.

(2) The string contains only 'a' or only 'b'.  We can remove all characters
    in a single operation.

(3) The string is empty.  This requires zero operations.
"""
from collections import Counter


class Solution:
    def removePalindromeSub(self, s: str) -> int:
        if s:
            ctr = Counter(s)
            if 'a' in ctr and 'b' in ctr:
                if s == s[::-1]:
                    # Contains a and b but is already a palindrome.
                    return 1
                # Contains a and b and is not already a palindrome.
                return 2
            # Contains only a single letter.
            return 1
        # Empty string.
        return 0


def test_1():
    assert Solution().removePalindromeSub("ababa") == 1

def test_2():
    assert Solution().removePalindromeSub("abb") == 2

def test_3():
    assert Solution().removePalindromeSub("baabb") == 2

def test_4():
    assert Solution().removePalindromeSub("") == 0
