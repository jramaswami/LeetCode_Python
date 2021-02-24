"""
LeetCode :: Score of Parentheses
jramaswami
"""
def solve0(index, S):
    """Recursive solution."""
    if index >= len(S):
        return 0 

    if S[index] == '(' and S[index + 1] == ')':
        return 1 + solve0(index + 2, S)
    else:
        return 2 * solve0(index + 1, S)


class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        return solve0(0, S)



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
