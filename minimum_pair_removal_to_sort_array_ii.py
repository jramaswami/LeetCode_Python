"""
LeetCode
3507. Minimum Pair Removal to Sort Array II
January 2026 Challenge
jramaswami

REF: https://dev.to/om_shree_0709/beginner-friendly-guide-minimum-pair-removal-to-sort-array-ii-leetcode-3510-c-python-57e2
"""


import heapq


class Solution:
    def minimumPairRemoval(self, nums: list[int]) -> int:
        # You do not have to sort an array of less than 2 values
        if len(nums) <= 1:
            return 0

        vals = list(nums)
        nexts = [i + 1 for i, _ in enumerate(nums)]
        prevs = [i - 1 for i, _ in enumerate(nums)]
        nexts[-1] = -1
        removed = [False for _ in vals]

        pq = []
        inversion_count = 0

        # Find the number of inversions
        for i, _ in enumerate(vals[:-1]):
            if vals[i] > vals[i+1]:
                inversion_count += 1
            # Push all pairs on to priority queue
            heapq.heappush(pq, (vals[i] + vals[i+1], i))

        if inversion_count == 0:
            return 0

        soln = 0
        while inversion_count > 0 and pq:
            pair_value, curr_index = heapq.heappop(pq)

            if removed[curr_index]:
                continue

            removal_index = nexts[curr_index]
            if (removal_index == -1 or
                    removed[removal_index] or
                    vals[curr_index] + vals[removal_index] != pair_value):
                continue

            preceding_index = prevs[curr_index]
            following_index = nexts[removal_index]
            soln += 1

            # Decrease count based on old values
            if preceding_index != -1 and vals[preceding_index] > vals[curr_index]:
                inversion_count -= 1
            if vals[curr_index] > vals[removal_index]:
                inversion_count -= 1
            if following_index != -1 and vals[removal_index] > vals[following_index]:
                inversion_count -= 1

            # Merge
            vals[curr_index] = pair_value
            nexts[curr_index] = following_index
            if following_index != -1:
                prevs[following_index] = curr_index
            removed[removal_index] = True

            # Increase count based on new sum
            if preceding_index != -1 and vals[preceding_index] > vals[curr_index]:
                inversion_count += 1
            if following_index != -1 and vals[curr_index] > vals[following_index]:
                inversion_count += 1

            if inversion_count == 0:
                break

            if preceding_index != -1:
                heapq.heappush(
                    pq,
                    (vals[preceding_index] + vals[curr_index], preceding_index)
                )
            if following_index != -1:
                heapq.heappush(
                    pq,
                    (vals[curr_index] + vals[following_index], curr_index)
                )

        return soln


def test_1():
    nums = [5,2,3,1]
    expected = 2
    assert Solution().minimumPairRemoval(nums) == expected