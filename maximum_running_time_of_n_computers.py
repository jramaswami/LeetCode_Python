"""
LeetCode
2141. Maximum Running Time of N Computers
July 2023 Challenge
jramaswami
Thank You, Larry!
"""


from typing import List

class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        batteries.sort(reverse=True)

        def check(t):
            "Return True if it is possible to run the computers for t minutes."
            contribution = 0
            for b in batteries:
                contribution += min(t, b)
            return contribution >= (n * t)

        lo = 0
        hi = sum(batteries) // n
        soln = 0
        while lo <= hi:
            mid = lo + ((hi - lo) // 2)
            if check(mid):
                soln = max(soln, mid)
                lo = mid + 1
            else:
                hi = mid - 1
        return soln


def test_1():
    n = 2
    batteries = [3,3,3]
    expected = 4
    assert Solution().maxRunTime(n, batteries) == expected


def test_2():
    n = 2
    batteries = [1, 1, 1, 1]
    expected = 2
    assert Solution().maxRunTime(n, batteries) == expected


def test_3():
    "TLE"
    n = 237
    batteries = [8249,4114,2829,2270,3994,1868,1414,5503,7524,4500,1397,9127,1486,2355,797,4749,3246,7707,8744,9500,9720,2905,5418,4810,8778,5026,6419,3808,9385,6509,4086,2467,9611,1141,7394,8630,5892,3945,271,2896,1552,5524,806,6221,8931,1380,1365,1953,3199,4306,7447,2527,8947,2270,4266,1081,6657,8918,7465,9515,4905,6097,9812,5648,5199,4891,1391,7999,6332,6889,6193,9629,3297,6617,9933,3191,6514,1549,5459,8710,6255,1565,5020,2623,8643,9346,3310,1945,4885,827,330,6309,9968,7105,88,9426,4561,4735,9280,9479,5198,845,5981,1415,8795,751,2893,8027,2603,3280,4090,7472,6530,7786,8716,5443,5017,5226,1704,9487,5891,2312,6352,20,4702,8997,962,7786,4557,7021,4873,734,8646,895,1731,1400,8983,9025,7866,113,478,8837,2311,7823,296,1934,2651,7059,8197,3609,4946,8182,8234,9355,2525,1195,200,6338,9653,4183,4599,933,8839,728,1879,2317,7866,7339,3755,2256,4458,2321,946,4211,5197,4247,100,7616,7066,131,5336,2352,6860,9494,837,167,2754,482,7693,5011,7919,1921,2565,9173,5523,1460,3455,4378,5035,734,8920,8111,9175,1492,328,2843,705,6564,3284,3506,9085,667,8395,6086,5784,4822,7654,5875,8018,5103,1239,7829,491,157,5819,1794,5357,2989,6814,7442,9634,2389,532,207,5769,3204,5447,1324,3600,5610,2702,1112,720,3052,9335,7050,2685,1326,2739,5709,3099,877,8265,9094,8591,9309,9823,2638,8939,5614,7100,4147,9772,6138,3952,2856,1436,9189,4139,1705,7324,1494,3817,6814,3255,5435,9977,17,7299,6706,6849,4451,8491,9125,7809,2516,3864,9562]
    expected = 3131
    assert Solution().maxRunTime(n, batteries) == expected