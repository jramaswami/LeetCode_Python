"""
LeetCode
1095. Find in Mountain Array
October 2023 Challenge
jramaswami
"""


# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:


class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        N = mountain_arr.length()
        # Make sure there is a left side of the mountain
        a, b = mountain_arr.get(0), mountain_arr.get(1)
        if a < b:
            # Search the left side of the mountain
            lo = 0
            hi = N - 1
            soln = N
            while lo <= hi:
                mid = lo + ((hi - lo) // 2)
                t = mountain_arr.get(mid)
                # Determine which "side" of the mountain we are on.
                if mid == 0 or mountain_arr.get(mid-1) < t:
                    # Left side of mountain
                    if t == target:
                        return mid
                    elif t < target:
                        lo = mid + 1
                    else:
                        hi = mid - 1
                else:
                    # Right side of mountain
                    hi = mid - 1

        # Make sure there is a right side of the mountain
        a, b = mountain_arr.get(N-2), mountain_arr.get(N-1)
        if a > b:
            # Search the right side of the mountain
            lo = 0
            hi = N - 1
            while lo <= hi:
                mid = lo + ((hi - lo) // 2)
                t = mountain_arr.get(mid)
                # Determine which "side" of the mountain we are on.
                if mid == N-1 or t > mountain_arr.get(mid+1):
                    # Right side of mountain
                    if t == target:
                        return mid
                    if t < target:
                        hi = mid - 1
                    else:
                        lo = mid + 1
                else:
                    # Left side of mountain
                    lo = mid + 1

            return -1