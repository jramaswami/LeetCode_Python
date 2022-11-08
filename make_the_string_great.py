"""
LeetCode :: 1544. Make The String Great
November 2022 Challenge
jramaswami
"""

class Solution:
    def makeGood(self, s: str) -> str:

        def are_same_letter(a, b):
            "Return True if a and be are the same letter ignoring case."
            if a.lower() == b.lower():
                return True
            return False

        def are_different_case(a, b):
            "Return True if a and be are different case."
            return a.islower() != b.islower()

        stack = []
        for c in s:
            if stack:
                if are_same_letter(stack[-1], c) and are_different_case(stack[-1], c):
                    # If the letters are same but opposite case then pop stack
                    # and discard letter.
                    stack.pop()
                else:
                    # If they are different letters or same case, push c onto
                    # the stack.
                    stack.append(c)
            else:
                # If stack is empty, push c.
                stack.append(c)
        return "".join(stack)



def test_1():
    s = "leEeetcode"
    expected = "leetcode"
    assert Solution().makeGood(s) == expected


def test_2():
    s = "abBAcC"
    expected = ""
    assert Solution().makeGood(s) == expected