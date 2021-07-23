"""
LeetCode :: Arrays Module :: Duplicate Zeros
jramaswami
"""


from collections import deque


class Solution:
    def duplicateZeros(self, A):
        """
        Modify A in place.
        """
        Q = deque()
        for i, n in enumerate(A):
            if n == 0:
                # Duplicate zeros
                Q.append(n)
                Q.append(n)
            else:
                Q.append(n)
            A[i] = Q.popleft()


def test_1():
    A = [1,0,2,3,0,4,5,0]
    Solution().duplicateZeros(A)
    assert A == [1,0,0,2,3,0,0,4]


def test_2():
    A = [1, 2, 3]
    Solution().duplicateZeros(A)
    assert A == [1, 2, 3]


