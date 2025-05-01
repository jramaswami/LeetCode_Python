"""
LeetCode
2071. Maximum Number of Tasks You Can Assign
May 2025 Challenge
jramaswami

Thank You Larry!
"""


from sortedcontainers import SortedList
from typing import List


class Solution:
    def maxTaskAssign(self, tasks: List[int], workers: List[int], pills: int, strength: int) -> int:
        workers.sort()
        tasks.sort(reverse=True)

        # Binary search the answer
        def check(x: int):
            """Return True if x jobs can be completed
            """
            if len(workers) < x:
                return False
            if x == 0:
                return True

            workers0 = SortedList(workers[-x:])
            pills_used = 0
            # Choose the smallest x tasks in reverse order
            for t in tasks[-x:]:
                if t <= workers0[-1]:
                    workers0.pop()
                else:
                    # We need a pill, find the smallest worker
                    # that will allow a pill to work
                    i = workers0.bisect_left(t - strength)
                    if i >= len(workers0):
                        return False
                    workers0.remove(workers0[i])
                    pills_used += 1

                    if pills_used > pills:
                        return False
            return pills_used <= pills

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
    strength = 5
    expected = 3
    assert Solution().maxTaskAssign(tasks, workers, pills, strength) == expected


def test_5():
    """WA"""
    tasks = [74,41,64,20,28,52,30,4,4,63]
    workers = [38]
    pills = 0
    strength = 68
    expected = 1
    assert Solution().maxTaskAssign(tasks, workers, pills, strength) == expected
