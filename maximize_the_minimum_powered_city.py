"""
LeetCode
2528. Maximize the Minimum Powered City
November 2025 Challenge
jramaswami

Thank NeetCode.IO!
"""


class Solution:
    def maxPower(self, stations: List[int], r: int, k: int) -> int:
        N = len(stations)
        difference = [0 for _ in range(N+1)]
        for i, n in enumerate(stations):
            left = max(0, i - r)
            right = min(N, i + r + 1)
            difference[left] += n
            difference[right] -= n

        def check(target_power):
            curr_power = 0
            extra_stations = k
            difference0 = list(difference)
            for i in range(N):
                curr_power += difference0[i]
                if curr_power < target_power:
                    # Must increase
                    stations_needed = target_power - curr_power
                    if stations_needed > extra_stations:
                        return False
                    extra_stations -= stations_needed
                    curr_power += stations_needed
                    right = min(N, i + (2*r) + 1)
                    difference0[right] -= stations_needed
            return True

        low, high = min(stations), sum(stations) + k
        soln = low
        while low <= high:
            mid = (low + high) // 2
            if check(mid):
                soln = mid
                low = mid + 1
            else:
                high = mid - 1
        return soln