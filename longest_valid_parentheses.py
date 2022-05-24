"""
LeetCode :: May 2022 Challenge :: Longest Valid Parentheses
jramaswami
"""


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        match = [False for _ in s]
        stack = []
        for i, c in enumerate(s):
            if c == '(':
                stack.append((c, i))
            else:
                if stack:
                    match[stack[-1][1]] = True
                    match[i] = True
                    stack.pop()
                else:
                    # Invalid
                    stack = []

        curr = 0
        soln = 0
        for t in match:
            if t:
                curr += 1
            else:
                soln = max(soln, curr)
                curr = 0
        soln = max(soln, curr)
        return soln


def test_1():
    assert Solution().longestValidParentheses("(()") == 2

def test_2():
    assert Solution().longestValidParentheses(")()())") == 4

def test_3():
    assert Solution().longestValidParentheses("") == 0

def test_4():
    s = "(((()()((()((()()()()(((()()()()()()()()()()((((()()()(()()()()()()"
    print(s)
    print(len(s))
    assert Solution().longestValidParentheses(s) == 20

def test_5():
    """WA"""
    assert Solution().longestValidParentheses("()") == 2
