"""
LeetCode :: December 2021 Challenge :: 1306. Jump Game III
jramaswami
"""


import collections


class Solution:

    def canReach(self, arr, start):
        reachable = [False for _ in arr]
        reachable[start] = True
        queue = collections.deque([start])
        while queue:
            i = queue.popleft()
            if arr[i] == 0:
                return True
            jump_left = i - arr[i]
            jump_right = i + arr[i]
            if jump_left >= 0 and not reachable[jump_left]:
                queue.append(jump_left)
                reachable[jump_left] = True
            if jump_right < len(arr) and not reachable[jump_right]:
                queue.append(jump_right)
                reachable[jump_right] = True
        return False


def test_1():
    arr = [4,2,3,0,3,1,2]
    start = 5
    expected = True
    assert Solution().canReach(arr, start) == expected


def test_2():
    arr = [4,2,3,0,3,1,2]
    start = 0
    expected = True
    assert Solution().canReach(arr, start) == expected


def test_3():
    arr = [3,0,2,1,2]
    start = 2
    expected = False
    assert Solution().canReach(arr, start) == expected
