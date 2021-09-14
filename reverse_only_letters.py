"""
LeetCode :: September 2021 Challenge :: Reverse Only Letters
jramaswami
"""

class Solution:

    def reverseOnlyLetters(self, S):
        # Use a stack to reverse the letters.
        stack = []
        for c in S:
            if c.isalpha():
                stack.append(c)

        soln = []
        for c in S:
            if c.isalpha():
                soln.append(stack.pop())
            else:
                soln.append(c)

        return "".join(soln)


def test_1():
    S = "ab-cd"
    expected = "dc-ba"
    assert Solution().reverseOnlyLetters(S) == expected


def test_2():
    S = "a-bC-dEf-ghIj"
    expected = "j-Ih-gfE-dCba"
    assert Solution().reverseOnlyLetters(S) == expected


def test_3():
    S = "Test1ng-Leet=code-Q!"
    expected = "Qedo1ct-eeLg=ntse-T!"
    assert Solution().reverseOnlyLetters(S) == expected
