"""
LeetCode :: March 2022 Challenge :: Validate Stack Sequences
jramaswami
"""


class Solution:
    def validateStackSequences(self, pushed, popped):
        i = 0
        stack = []
        for p in pushed:
            stack.append(p)
            while stack and stack[-1] == popped[i]:
                stack.pop()
                i += 1

        return not stack and i >= len(popped)


def test_1():
    pushed = [1,2,3,4,5]
    popped = [4,5,3,2,1]
    assert Solution().validateStackSequences(pushed, popped) == True


def test_2():
    pushed = [1,2,3,4,5]
    popped = [4,3,5,1,2]
    assert Solution().validateStackSequences(pushed, popped) == False


def test_3():
    pushed = [1,0,2]
    popped = [2,1,0]
    assert Solution().validateStackSequences(pushed, popped) == False
