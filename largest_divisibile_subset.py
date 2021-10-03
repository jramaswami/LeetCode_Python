"""
LeetCode :: 368. Largest Divisible Subset
jramaswami
"""

class Solution:

    def largestDivisibleSubset(self, nums):
        nums.sort()

        # TODO: explore backwards.  The longest path ending at n is
        # n added to the longest path ending at all numbers ending
        # at m such that m divides n.

        # Build graph and find starting nodes
        in_degrees = [0 for _ in nums]
        adj = [[] for _ in nums]
        for i, n in enumerate(nums):
            for j, m in enumerate(nums[i+1:], start=i+1):
                if m % n == 0:
                    adj[i].append(j)
                    in_degrees[j] += 1

        # To find longest path use dfs.
        max_paths = [[] for _ in nums]
        def dfs(node, path, root):
            path.append(node)
            if adj[node]:
                for neighbor in adj[node]:
                    dfs(neighbor, path, root)
            else:
                if len(path) > len(max_paths[root]):
                    max_paths[root] = list(path)
            path.pop()

        print(in_degrees)
        soln = []
        for node, in_degree in enumerate(in_degrees):
            if in_degree == 0:
                dfs(node, [], node)
                if len(max_paths[node]) > len(soln):
                    soln = max_paths[node]
        return [nums[i] for i in soln]


def test_1():
    nums = [1, 2, 3]
    expected = [1, 2]
    assert Solution().largestDivisibleSubset(nums) == expected


def test_2():
    nums = [1, 2, 4, 8]
    expected = [1, 2, 4, 8]
    assert Solution().largestDivisibleSubset(nums) == expected


"""TLE"""
nums = [1,2,4,8,16,32,64,128,256,512,1024,2048,4096,8192,16384,32768,65536,131072,262144,524288,1048576,2097152,4194304,8388608,16777216,33554432,67108864,134217728,268435456,536870912,1073741824]
expected = []
assert Solution().largestDivisibleSubset(nums) == expected
