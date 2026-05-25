"""
LeetCode
1871. Jump Game VII
May 2026 Challenge
jramaswami
"""


import collections


class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        queue = collections.deque()
        queue.append(0)
        for j, x in enumerate(s[1:], start=1):
            # Remove any indexes that cannot reach j with maxJump
            while queue and j > queue[0] + maxJump:
                queue.popleft()
            # Is leftmost index in the queue farther than the minJump?
            if x == '0' and queue and queue[0] + minJump <= j:
                if j == len(s) - 1:
                    return True
                queue.append(j)
        return False




def test_1():
    s = "011010"
    minJump = 2
    maxJump = 3
    assert Solution().canReach(s, minJump, maxJump)


def test_2():
    s = "01101110"
    minJump = 2
    maxJump = 3
    assert not Solution().canReach(s, minJump, maxJump)


def test_108():
    "TLE"
    s = '0' * pow(10,5)
    minJump = 5
    maxJump = 99998
    assert Solution().canReach(s, minJump, maxJump)
