"""
LeetCode
1248. Count Number of Nice Subarrays
June 2024 Challenge
jramaswami
"""


import collections


WindowItem = collections.namedtuple('WindowItem', ['index', 'value'])


class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        window = collections.deque()
        odd_indices = collections.deque()
        soln = odds = 0
        for i, n in enumerate(nums):
            window.append(WindowItem(i, n))
            if n % 2:
                odds += 1
                odd_indices.append(i)
            while odds > k:
                if window[0].value % 2:
                    odds -= 1
                    assert window[0].index == odd_indices[0]
                    odd_indices.popleft()
                window.popleft()
            if odds == k:
                soln += (1 + odd_indices[0] - window[0].index)
        return soln
