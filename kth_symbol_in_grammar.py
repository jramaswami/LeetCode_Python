"""
LeetCode
779. K-th Symbol in Grammar
October 2023 Challenge
jramaswami
"""


class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n == 1:
            return 0

        # Convert to zero-based index
        k -= 1
        # n -= 1

        curr = 0
        for b in range(n+1):
            if b == n:
                return curr
            if k & (1 << b):
                # Go right
                if curr == 1:
                    curr = 0
                else:
                    curr = 1
            else:
                # Go left
                if curr == 1:
                    curr = 1
                else:
                    curr = 0



def test_1():
    assert Solution().kthGrammar(1, 1) == 0


def test_2():
    assert Solution().kthGrammar(2, 1) == 0


def test_3():
    assert Solution().kthGrammar(2, 2) == 1


def test_4():
    assert Solution().kthGrammar(30, 67548) == 0


def test_5():
    "WA"
    assert Solution().kthGrammar(4, 5) == 1
