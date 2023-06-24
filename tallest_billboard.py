"""
LeetCode
956. Tallest Billboard
June 2023 Challenge
jramaswami
"""


import functools
from typing import List


class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        soln = 0
        previous_legs = dict()
        previous_legs[0]= [0]
        # The maximum possible leg length is half the sum of all rods.
        maximum_leg_length = sum(rods) // 2
        for rod_index, rod_length in enumerate(rods):
            # Create a new leg for all previous legs by adding the rod.
            previous_leg_lengths = previous_legs.keys()
            new_legs = dict()
            for previous_leg_length, previous_leg_keys in previous_legs.items():
                # Compute the length of the new rod
                new_leg_length = previous_leg_length + rod_length
                # Don't bother if leg is too long
                if new_leg_length > maximum_leg_length:
                    continue
                # Add new_leg_length to previous_legs if it isn't already there
                if new_leg_length not in new_legs:
                    new_legs[new_leg_length] = []
                # We will be comparing our new rods to any existing rods.
                # If there are any existing rods, put them in keys to compare.
                # We should only to this if the new_leg_length is more than
                # our current solution.
                keys_to_compare = []
                if new_leg_length > soln and new_leg_length in previous_legs:
                    keys_to_compare = previous_legs[new_leg_length]
                # Create a new leg by adding the rod to any previous rod.

                for previous_leg_key in previous_leg_keys:
                    # Compute the new key.
                    new_leg_key = previous_leg_key | (1 << rod_index)
                    # See if there are any rods in keys to compare that
                    # do not overlap.  If there are any, then we can
                    # build two distinct rods of the given length.
                    if any(new_leg_key & p == 0 for p in keys_to_compare):
                        soln = max(soln, new_leg_length)
                        # We no longer have to look for rods of this length.
                        # Don't compare them any more.
                        keys_to_compare = []
                    # Add the new leg to previous legs
                    new_legs[new_leg_length].append(new_leg_key)
            # Merge new legs
            for new_leg_length, new_leg_keys in new_legs.items():
                if new_leg_length in previous_legs:
                    previous_legs[new_leg_length].extend(new_leg_keys)
                else:
                    previous_legs[new_leg_length]= list(new_leg_keys)
        return soln
                    

def test_1():
    rods = [1,2,3,6]
    expected = 6
    assert Solution().tallestBillboard(rods) == expected


def test_2():
    rods = [1,2,3,4,5,6]
    expected = 10
    assert Solution().tallestBillboard(rods) == expected


def test_3():
    rods = [1,2]
    expected = 0
    assert Solution().tallestBillboard(rods) == expected


def test_4():
    "TLE"
    rods = [1,2,4,8,16,32,64,128,256,512,50,50,50,150,150,150,100,100,100,123]
    expected = 1023
    assert Solution().tallestBillboard(rods) == expected


def test_5():
    "TLE"
    rods = [102,101,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100]
    expected = 1023
    assert Solution().tallestBillboard(rods) == expected
