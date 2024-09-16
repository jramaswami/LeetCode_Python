"""
LeetCode
539. Minimum Time Difference
September 2024 Challenge
jramaswami
"""



class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        def to_mins(t):
            """Convert times into the number of minutes from 0
            """
            # Assume time is formatted correctly
            hh = int(t[:2])
            mm = int(t[-2:])
            return (60 * hh) + mm
        
        def delta_t(t1, t2):
            """Return smallest time difference
            
            Smallest time difference will be forward or backward
            """
            t1, t2 = min(t1, t2), max(t1, t2)
            return min(t2 - t1, (t1+(24*60)) - t2)
        
        ts = [to_mins(t) for t in timePoints]
        ts.sort()
        soln = min(delta_t(t1, t2) for t1, t2 in zip(ts[:-1], ts[1:]))
        soln = min(soln, delta_t(ts[0], ts[-1]))
        return soln
