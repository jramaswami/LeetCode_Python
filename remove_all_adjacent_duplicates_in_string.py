"""
LeetCode :: June 2021 Challenge :: Remove All Adjacent Duplicates In String
jramaswami
"""

from collections import deque


class Solution:
    def removeDuplicates(self, s):
        left = list(s)
        right = deque()

        # Move the letters from left to right.
        # While doing so, if the back of the left and the front of the right
        # have the same letter, get rid of both of them.  If they don't, then
        # move the letter at the back of the left to the front of the right.
        # This can be done in O(n) time with O(n) space.
        while left:
            if right and left[-1] == right[0]:
                left.pop()
                right.popleft()
            else:
                right.appendleft(left.pop())

        return "".join(right)


def test_1():
    s = "abbaca"
    expected = "ca"
    assert Solution().removeDuplicates(s) == expected


def test_2():
    s = "azxxzy"
    expected = "ay"
    assert Solution().removeDuplicates(s) == expected


def test_3():
    s = "bcdadbdcddbabcdbbdbaddbadcdddbcdadccbabbaadbdcbcad"
    expected = "bcdadbdcbabcbabadcdbcdadbadbdcbcad"
    assert Solution().removeDuplicates(s) == expected
