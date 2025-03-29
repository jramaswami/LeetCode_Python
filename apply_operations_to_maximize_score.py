"""
LeetCode
2818. Apply Operations to Maximize Score
March 2025 Challenge
jramaswami

Thank You NeetCode.IO!
"""


from typing import List
import heapq
import math


class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        prime_scores = []
        for n in nums:
            score = 0
            for p in range(2, int(math.sqrt(n)) + 1):
                if n % p == 0:
                    score += 1
                    while n % p == 0:
                        n //= p
            if n >= 2:
                score += 1
            prime_scores.append(score)

        MOD = pow(10, 9) + 7
        left_bound = [-1 for _ in nums]
        right_bound = [len(nums) for _ in nums]
        stack = []
        for i, s in enumerate(prime_scores):
            while stack and prime_scores[stack[-1]] < s:
                index = stack.pop()
                right_bound[index] = i
            if stack:
                left_bound[i] = stack[-1]
            stack.append(i)
        heap = [(-n, i) for i, n in enumerate(nums)]
        heapq.heapify(heap)
        soln = 1
        while k > 0:
            n, index = heapq.heappop(heap)
            n = -n
            score = prime_scores[index]
            left_count = index - left_bound[index]
            right_count = right_bound[index] - index
            count = left_count * right_count
            ops = min(count, k)
            soln = soln * pow(n, ops, MOD)
            soln %= MOD
            k -= ops
        return soln


def test_1():
    nums = [8,3,9,3,8]
    k = 2
    expected = 81
    assert Solution().maximumScore(nums, k) == expected


def test_2():
    nums = [19,12,14,6,10,18]
    k = 3
    expected = 4788
    assert Solution().maximumScore(nums, k) == expected