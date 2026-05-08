"""
LeetCode
3629. Minimum Jumps to Reach End via Prime Teleportation
May 2026 Challenge
jramaswami
"""


from typing import List
import collections


MX = pow(10,6) + 10
is_prime = [True for _ in range(MX)]
spf = [0 for _ in range(MX)]
is_prime[0] = is_prime[1] = False
for p in range(2, MX):
    if is_prime[p]:
        spf[p] = p
        for x in range(2*p, MX, p):
            is_prime[x] = False
            if spf[x] == 0:
                spf[x] = p


def get_factors(x):
    res = set()
    while x > 1:
        p = spf[x]
        res.add(p)
        x //= p
    return res


class Solution:
    def minJumps(self, nums: List[int]) -> int:
        groups = collections.defaultdict(list)
        for i, x in enumerate(nums):
            for p in get_factors(x):
                groups[p].append(i)
        queue = collections.deque()
        queue.append((0, 0))
        seen_i = set()
        seen_i.add(0)
        seen_p = set()
        while queue:
            i, jumps = queue.popleft()
            if i == len(nums) - 1:
                return jumps
            if i + 1 < len(nums) and not i+1 in seen_i:
                queue.append((i+1, jumps+1))
                seen_i.add(i+1)
            if i - 1 >= 0 and not i-1 in seen_i:
                queue.append((i-1, jumps+1))
                seen_i.add(i-1)
            if nums[i] in groups and not nums[i] in seen_p:
                seen_p.add(nums[i])
                for j in groups[nums[i]]:
                    if not j in seen_i:
                        seen_i.add(j)
                        queue.append((j, jumps+1))


def test_668():
    nums = [7,5,7]
    assert Solution().minJumps(nums) == 1
