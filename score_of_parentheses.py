"""
LeetCode :: March 2022 Challenge :: Score of Parentheses
jramaswami
"""


class Solution:

    def scoreOfParentheses(self, S):
        # "()" has score 1.
        # AB has score A + B, where A and B are balanced parentheses strings.
        # (A) has score 2 * A, where A is a balanced parentheses string.
        soln = 0
        M = 1
        i = 0
        while i < len(S):
            if S[i] == '(' and S[i+1] == ')':
                soln += (M * 1)
                i += 2
            elif S[i] == '(':
                M *= 2
                i += 1
            elif S[i] == ')':
                M //= 2
                i += 1
        return soln


def test_1():
    assert Solution().scoreOfParentheses("()") == 1


def test_2():
    assert Solution().scoreOfParentheses("(())") == 2


def test_3():
    assert Solution().scoreOfParentheses("()()") == 2


def test_4():
    assert Solution().scoreOfParentheses("(()(()))") == 6


def test_5():
    assert Solution().scoreOfParentheses("(())()") == 3
