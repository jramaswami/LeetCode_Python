"""
LeetCode
3296. Minimum Number of Seconds to Make Mountain Height Zero
March 2026 Challenge
jramaswami
REF: https://algo.monster/liteproblems/3296 for the check function
"""


class Solution:
    def minNumberOfSeconds(self, mountain_height: int, worker_times: List[int]) -> int:
        def max_rounds(worker_time, time_limit):
            return int(sqrt(2 * time_limit / worker_time + 0.25) - 0.5)

        def check(time_limit):
            return sum(max_rounds(w, time_limit) for w in worker_times) >= mountain_height

        low, high = 0, pow(10, 16)
        soln = -1
        while low <= high:
            mid = low + ((high - low) // 2)
            if check(mid):
                soln = mid
                high = mid - 1
            else:
                low = mid + 1
        return soln