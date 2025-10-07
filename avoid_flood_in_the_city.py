"""
LeetCode
1488. Avoid Flood in The City
October 2025 Challenge
jramaswami
"""


class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        soln = [-1 for _ in rains]
        full = set()
        for i, lake in enumerate(rains):
            if lake == 0:
                # Empty a lake, but which lake?
                # The next lake that is full
                for lake0 in rains[i+1:]:
                    if lake0 in full:
                        soln[i] = lake0
                        full.remove(lake0)
                        break
                if soln[i] == -1:
                    if full:
                        soln[i] = full.pop()
                    else:
                        soln[i] = 1
            else:
                if lake in full:
                    return []
                full.add(lake)
        return soln