"""
LeetCode :: 368. Largest Divisible Subset
jramaswami
"""


class Solution:

    def largestDivisibleSubset(self, nums):
        nums.sort()

        # Build graph where an edge (u, v) means nums[v] divides nums[u].
        adj = [[] for _ in nums]
        for i, n in enumerate(nums):
            for j, m in enumerate(nums[i+1:], start=i+1):
                if m % n == 0:
                    adj[j].append(i)

        # Top-down dynamic programming.
        cache = [[] for n in nums]
        has_cache = [False for n in nums]

        def solve(u):
            """Return the largest subset ending at nums[u]."""
            if has_cache[u]:
                return cache[u]

            if adj[u]:
                for v in adj[u]:
                    v_path = solve(v)
                    if len(v_path) + 1 > len(cache[u]):
                        cache[u] = list(v_path)
                        cache[u].append(u)
            else:
                cache[u] = [u]

            has_cache[u] = True
            return cache[u]

        soln = []
        for off, n in enumerate(reversed(nums)):
            u = len(nums) - off - 1
            u_path = solve(u)
            if len(soln) <= len(u_path):
                soln = u_path
        return [nums[i] for i in soln]


def test_1():
    nums = [1, 2, 3]
    expected = [1, 2]
    assert Solution().largestDivisibleSubset(nums) == expected


def test_2():
    nums = [1, 2, 4, 8]
    expected = [1, 2, 4, 8]
    assert Solution().largestDivisibleSubset(nums) == expected


def test_3():
    """TLE"""
    nums = [1,2,4,8,16,32,64,128,256,512,1024,2048,4096,8192,16384,32768,65536,131072,262144,524288,1048576,2097152,4194304,8388608,16777216,33554432,67108864,134217728,268435456,536870912,1073741824]
    expected = list(nums)   # nums is powers of two.
    assert Solution().largestDivisibleSubset(nums) == expected
