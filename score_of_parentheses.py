"""
LeetCode :: Score of Parentheses
jramaswami
"""
class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        score = 0
        mult = 1
        i = 0
        while i < len(S):
            if S[i] == ')':
                mult //= 2
                i += 1
            elif S[i] == '(' and S[i+1] == ')':
                score += (mult * 1)
                i += 2
            elif S[i] == '(':
                mult *= 2
                i += 1

        return score



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
