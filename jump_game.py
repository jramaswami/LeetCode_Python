"""
LeetCode
Jump Game
December 2022 Challenge
jramaswami
"""


import heapq


class Solution:

    def canJump(solve, nums):
        visited = [False for _ in nums]
        visited[0] = True
        queue = [0]
        while queue:
            u = -heapq.heappop(queue)
            if u == len(nums) - 1:
                return True
            for x in range(1, nums[u]+1):
                if not visited[u+x]:
                    visited[u+x] = True
                    heapq.heappush(queue, -(u+x))
        return False


def test_1():
    nums = [2,3,1,1,4]
    assert Solution().canJump(nums) == True


def test_2():
    nums = [3,2,1,0,4]
    assert Solution().canJump(nums) == False


def test_3():
    nums = [1,1,2,0,0,0,1]
    assert Solution().canJump(nums) == False


def test_4():
    """WA"""
    nums = [0]
    assert Solution().canJump(nums) == True


def test_5():
    "RTE"
    nums = [2, 0]
    assert Solution().canJump(nums) == True
