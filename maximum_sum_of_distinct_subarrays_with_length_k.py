"""
LeetCode
2461. Maximum Sum of Distinct Subarrays With Length K
November 2024 Challenge
jramaswami
"""

import collections


class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        # Sliding window with Counter for determining uniqueness
        window = collections.deque()
        freqs = collections.Counter()
        elems_with_dupes = 0
        curr_sum = 0
        soln = 0
        for n in nums:
            window.append(n)
            freqs[n] += 1
            curr_sum += n
            if freqs[n] == 2:
                elems_with_dupes += 1
            
            while len(window) > k:
                x = window.popleft()
                curr_sum -= x
                freqs[x] -= 1
                if freqs[x] == 1:
                    elems_with_dupes -= 1
            if elems_with_dupes == 0 and len(window) == k:
                soln = max(soln, curr_sum)

        return soln
