"""
LeetCode
2071. Maximum Number of Tasks You Can Assign
May 2025 Challenge
jramaswami

Thank You Larry!
"""


from typing import List


class Solution:
    def maxTaskAssign(self, tasks: List[int], workers: List[int], pills: int, strength: int) -> int:
        workers.sort(reverse=True)
        tasks.sort()

        # Binary search the answer
        def check(x: int):
            """Return True if x jobs can be completed
            """
            if len(workers) < x:
                return False
            p = pills
            for w, t in zip(workers[:x], reversed(tasks[:x])):
                if w < t:
                    if p == 0 or w + strength < t:
                        return False
                    p -= 1
            return True

        lo = 0
        hi = len(tasks)
        soln = 0
        while lo <= hi:
            mid = lo + ((hi - lo) // 2)
            if check(mid):
                lo = mid + 1
                soln = max(mid, soln)
            else:
                hi = mid - 1
        return soln


def test_4():
    """WA"""
    tasks = [5,9,8,5,9]
    workers = [1,6,4,2,6]
    pills = 1
    strength = 1
    expected = 3
    assert Solution().maxTaskAssign(tasks, workers, pills, strength) == expected
