"""
LeetCode :: June 2021 Challenge :: Max Sum of Rectangle No Larger Than K
jramaswami

Thank You Larry!
"""


from sortedcontainers import SortedList
from itertools import accumulate
from math import inf


class Solution:
    def maxSumSubmatrix(self, matrix, k):
        prefix = [[0 for _ in row] for row in matrix]

        # Compute prefix sums for the matrix.
        # O(N^2)
        for r, row in enumerate(matrix):
            for c, v in enumerate(row):
                prefix[r][c] = v
                if r > 0 and c > 0:
                    prefix[r][c] -= prefix[r-1][c-1]
                if r > 0:
                    prefix[r][c] += prefix[r-1][c]
                if c > 0:
                    prefix[r][c] += prefix[r][c-1]

        # Fix the top row and bottom row.
        soln = -inf
        for top_row in range(len(matrix)):
            for bottom_row in range(top_row, len(matrix)):
                # Keep track of our previous sums
                previous_sums = SortedList()
                # The subarray sum is the sum of no elements: 0.
                previous_sums.add(0)

                # Scan over the columns.
                for col in range(len(matrix[0])):
                    # Get the sum of the rectangle (top_row, 0) to (bottom_row, col).
                    current_sum = prefix[bottom_row][col]
                    if top_row > 0:
                        current_sum -= prefix[top_row-1][col]

                    # We want to find the largest sum in a sub-rectangle
                    # that is at most k.  That means it has to be smaller than
                    # or equal to the current_sum - k.
                    target = current_sum - k

                    # Binary search on our sorted list to find the target.
                    index = previous_sums.bisect_left(target)
                    # If we found a sub-rectangle meeting our conditions,
                    # see if it is the max solution.
                    if 0 <= index < len(previous_sums):
                        soln = max(soln, current_sum - previous_sums[index])

                    previous_sums.add(current_sum)

        return soln


def test_1():
    matrix = [[1,0,1],[0,-2,3]]
    k = 2
    expected = 2
    assert Solution().maxSumSubmatrix(matrix, k) == expected


def test_2():
    matrix = [[2,2,-1]]
    k = 3
    expected = 3
    assert Solution().maxSumSubmatrix(matrix, k) == expected


def test_3():
    matrix = [[37, -60, 85, -41, -57, 30, -96, -50, -97, 75, 59, -27, 49, 97, -55, -51, -8, 94, 43, 22], [30, -20, 50, -54, 75, -61, 5, 55, -69, -24, -50, 44, 93, -97, -90, -53, 18, 78, 3, -85], [23, -50, -20, -98, 26, 79, -12, 6, 57, -82, -4, -20, -47, -34, 76, 47, 0, -97, -77, -73], [-18, -90, -33, 44, -50, -54, -60, -76, 92, 4, 73, 77, 89, -17, 60, 58, -78, -77, -53, -47], [4, -33, 90, -83, -53, -50, -83, 10, -12, 14, -17, 29, 25, -19, -27, 93, 51, -39, 24, -15], [-98, -6, -50, 13, 65, 59, 64, 2, 9, 67, -50, -51, 39, 66, -99, 84, 8, 68, -43, 96], [13, -3, 15, -26, -11, 31, -50, 83, -20, 94, -16, -72, 34, 48, -13, -51, 24, 66, -54, -71], [37, 25, 70, -14, 2, -20, -77, -3, 29, 30, -65, 81, -80, -65, -56, 20, -65, 90, 13, -46], [63, -20, 48, -27, -56, 8, 100, -50, -72, -20, 74, -90, -77, -15, 32, 67, -18, -75, 27, -70], [-45, -5, 55, -26, -16, -87, 92, 7, 74, 26, -23, 13, -69, 57, -76, 11, -99, 76, -86, 11], [23, -46, 63, 67, 25, 78, 13, 7, -43, 91, -70, -84, -30, -74, -34, -74, -32, 43, -32, -84], [-47, 37, 64, -42, -62, -60, 54, 19, -53, -47, 73, 43, -65, -11, 64, -46, 2, 47, -83, 95], [-49, -90, 94, 23, -64, 75, -68, -64, 43, -79, 0, 58, -58, -39, 93, -93, -19, 30, -47, 95], [-84, 91, 58, 42, 99, -31, 74, 62, -18, -48, 53, 53, 8, 84, -43, 0, -55, -63, 52, 97], [-46, 38, 65, -94, -46, -92, -25, -34, -74, -99, -90, 22, -29, -45, -50, -25, -84, 88, 67, -2], [-60, -93, 2, 16, -15, 50, 100, -8, -17, 61, -75, -1, 30, 10, 34, -38, -21, 51, -91, 35], [26, -40, 29, 42, 99, -20, -87, 29, 49, 1, 67, 4, 60, -81, -97, 14, 38, -37, -16, -24], [-42, 63, -20, 81, 43, 73, -79, -40, -31, -75, 32, 51, 48, -54, 28, -21, 93, -31, 79, -29], [-44, -91, 53, 52, 12, -18, -94, -40, 98, 20, 95, -27, 0, -74, 20, 25, 74, -42, -39, 59], [-19, -6, -87, -95, -61, -85, -60, 28, -9, -81, 60, 89, 91, -66, -10, -67, 33, 17, -74, -60]]
    k = 1000
    expected = 796
    assert Solution().maxSumSubmatrix(matrix, k) == expected


def test_4():
    """WA"""
    matrix = [[2,2,-1]]
    k = 0
    expected = -1
    assert Solution().maxSumSubmatrix(matrix, k) == expected


def test_5():
    """TLE"""
    matrix = [[-100,-84,47,-12,-9,74,-45,-67,25,43,-11,-90,-88,32,79,4,-18,-72,18,-97,37,-23,-22,-89,-89,-100,-34,-90,43,62,53,-37,56,4,-40,76,-69,-57,-59,-11,-49,-10,64,65,50,-8,37,80,-65,20,87,-57,-1,49,-96,-100,-61,-78,-75,-1,-64,23,27,54,86,22,-61,-8,-35,11,-60,-30,99,-88,22,7,-80,100,94,100,38,-25,88,-53,-12,-95,-71,43,19,43,-59,-71,-76,-68,4,-26,4,-70,-23,-62],[51,-59,31,-72,14,2,33,33,8,78,36,7,-8,52,-15,81,81,-94,-57,5,11,86,65,95,-95,34,51,46,-16,73,24,-63,-89,-69,-38,-86,-42,-71,21,100,-29,13,68,-18,-21,-34,58,-2,-90,-38,30,91,-7,-93,-54,-84,15,51,59,55,-98,34,-39,12,-21,-4,57,-87,70,3,63,86,-5,48,-89,-1,-34,11,-100,-78,63,51,79,-34,-72,31,-26,-81,98,76,10,21,83,89,-64,-18,28,11,29,-70],[41,91,-6,-4,-3,13,-82,-54,76,81,97,21,-19,3,-78,59,-7,-95,21,59,-64,-46,50,44,-67,-97,-39,11,-9,-92,-59,-9,36,-68,-63,-99,52,90,19,53,75,64,34,-31,-46,-37,-88,-86,37,-8,100,22,93,-54,-66,84,-26,49,93,-4,-90,-20,-82,76,-33,2,-89,86,77,-4,95,31,41,24,24,-75,-81,41,6,-56,7,51,53,-81,-46,-19,46,45,-7,-37,71,17,39,-67,22,-26,77,-27,34,90],[69,64,-62,84,13,-29,-67,40,21,90,-41,-82,-9,66,-57,59,-94,-51,-52,-89,-13,-93,75,-39,57,-53,-85,-8,91,-69,29,-55,56,-79,43,-31,10,12,-38,89,-75,48,-58,-13,-49,-73,57,-20,79,-82,-76,-97,-17,-48,38,-86,81,17,-9,-10,-53,37,87,-97,-87,47,-89,57,13,-18,59,-58,-77,-87,36,-53,29,64,-41,7,-34,-64,36,-28,43,-7,-24,60,8,-60,-67,90,90,29,39,-12,-14,12,-45,38],[-63,-34,-48,-7,-49,-79,-93,72,-54,2,53,99,-81,-37,19,-84,-34,-70,-87,100,7,54,-43,-89,34,-78,64,-93,31,-70,85,-91,42,-10,98,-35,1,-3,-81,40,41,94,17,92,-84,97,89,47,50,-13,86,-86,-15,84,-10,29,-94,6,35,37,-33,-4,-10,-74,-42,-28,50,92,52,66,-73,95,33,32,-1,-71,-87,89,5,75,-31,92,37,-82,37,-71,-89,32,51,-25,-90,6,16,-55,-45,-10,-20,92,-20,87],[-96,-44,-10,-67,-87,61,1,22,6,67,8,-8,-99,19,89,-73,47,24,-38,-9,32,-31,-51,66,40,63,-57,2,55,5,-85,20,-62,48,71,-27,5,-68,-39,-58,-12,-73,57,55,91,-54,-97,31,-47,-73,29,27,36,8,47,52,-60,54,-22,64,65,87,39,73,72,86,70,-64,-96,10,64,81,-21,-69,-68,-62,24,6,18,60,-30,96,83,79,-17,19,-59,-8,-66,-94,50,41,79,-59,53,-64,-100,33,-77,-40],[70,-57,74,-44,71,-22,57,-58,-25,48,46,-2,-80,66,42,-10,-84,91,-12,-6,71,50,-54,-72,-72,-97,90,72,90,-11,-88,17,98,51,86,78,-45,-63,-29,70,-6,-53,27,-38,-65,-13,-72,-22,64,-14,38,28,-15,-65,-85,-43,72,-48,-91,65,-8,4,57,-80,97,23,-14,-95,96,33,-47,-48,31,-80,20,-21,32,0,97,38,-42,23,-55,-21,77,-40,0,81,-3,-42,-47,52,49,-11,-8,-58,-10,-90,3,26],[-53,-20,-59,80,83,-33,24,52,-76,-19,-4,45,-46,-83,72,-23,-2,-90,20,-64,99,-93,55,27,-56,-1,24,61,3,-8,-91,53,-34,72,-81,-62,-30,72,-2,-81,10,-66,-64,-49,60,60,65,44,33,63,95,30,-3,-15,22,-40,40,-43,75,-65,63,-22,-60,-41,35,-20,65,12,-15,-92,1,45,100,23,-23,-58,-52,-77,98,-55,-89,-8,33,77,46,32,0,30,65,-2,81,16,-90,60,30,-26,89,-81,-78,-77],[23,77,86,-23,24,-19,7,2,0,-3,-97,40,-45,-22,-64,-7,-21,67,-59,37,83,-3,-74,-79,-47,15,58,-82,22,-18,63,-19,-81,-27,-82,-70,-49,-20,36,-75,-7,-27,85,85,-70,-50,37,-91,1,46,-9,-13,-3,92,86,20,78,-40,-47,66,-29,-18,-14,37,-68,96,-45,-61,94,-41,-56,30,36,48,-69,99,92,-81,-39,83,1,-19,-52,-54,-37,-75,-34,73,41,-87,94,32,-2,10,-90,40,-26,-11,-70,75],[-89,-74,-64,-4,22,-28,-95,92,-3,14,31,-79,-52,-26,-15,41,-86,-96,17,-44,5,92,-62,-19,7,-44,25,-100,-23,-36,-85,32,-90,-30,89,-41,14,-30,70,-56,-34,-71,-8,89,38,6,38,51,44,-30,50,41,95,-37,-5,-91,-25,29,-23,51,-11,-87,59,72,39,35,49,71,-85,-69,-98,-9,5,71,83,-9,-94,62,64,-40,-14,98,87,-34,47,86,45,-36,9,33,-2,-30,38,-50,-36,-78,29,72,84,52],[79,64,59,8,9,68,88,72,16,29,-39,96,77,74,-79,57,67,-98,16,63,-79,53,60,20,87,69,80,74,60,49,96,-73,28,-51,16,87,-52,52,95,50,-49,-25,-32,79,-8,35,8,34,69,11,-47,-90,93,0,74,-88,89,84,-66,53,38,74,47,4,64,-54,-89,87,4,-44,-68,-54,85,-95,-81,-50,-43,-53,-2,62,-6,18,-19,-24,-68,-19,-17,-39,84,-45,-48,-94,65,87,-74,95,-52,93,0,-72],[-70,-26,57,27,-97,33,49,-72,68,6,42,99,96,29,-25,-75,-96,-64,78,-25,71,18,-35,-66,-29,0,-17,-16,90,-41,-90,-90,-35,-80,-76,59,-95,69,18,-69,-58,-43,78,-77,7,-25,52,-31,30,92,-63,38,100,-51,-45,87,-45,57,-63,36,-11,-45,53,3,-97,79,-25,-71,21,10,68,-20,89,46,59,-19,66,47,-17,-67,0,-46,-40,-22,99,8,52,-71,14,-70,-78,25,-81,-47,92,78,77,82,77,-22],[74,14,88,24,96,4,-86,-19,76,-23,-38,1,-93,23,-46,33,-41,-51,-76,-49,1,-3,-57,-89,44,-17,-33,60,40,43,25,-4,-8,-38,73,59,58,-83,-9,38,32,42,38,-13,99,-70,-11,-10,65,-70,91,-99,59,-37,-79,-50,39,-40,55,50,75,17,-5,57,51,22,-59,-99,-87,-2,-78,-58,-10,-52,-1,-67,38,79,-12,-85,-70,26,22,93,-37,67,-99,71,92,-7,-25,80,-72,-55,60,-17,-63,-15,26,1],[31,77,-98,95,-96,-12,24,57,-19,-70,28,66,-23,56,-79,-89,57,8,98,40,99,-5,39,-29,37,-51,-90,-90,-31,85,34,-49,-18,-4,-3,35,-64,38,9,-2,70,62,-89,-99,-78,89,59,39,-72,88,53,-29,57,6,-73,-38,-42,-87,-17,-51,-54,-8,-70,77,-68,36,-30,-80,-90,-20,-94,-35,96,-80,54,-37,94,72,-18,38,87,80,-64,37,24,-67,29,25,30,80,-7,-19,28,-8,-19,12,53,-9,26,-24],[39,-65,-16,60,-88,-70,21,-23,-58,21,-43,-56,-84,36,-20,79,78,-23,21,-7,-68,-94,77,-74,56,-57,1,-48,76,40,23,-8,83,95,56,64,-49,-97,-88,61,40,-28,-22,59,51,-63,-63,-73,-28,-83,-19,-76,-96,-52,1,40,91,-16,-11,-8,-97,4,-91,-7,9,-37,-14,62,1,-3,-92,84,-44,-64,67,64,56,40,-77,-69,70,-71,-34,-3,-51,54,-19,81,65,37,-71,-51,-86,-31,-3,22,50,23,34,-86],[14,-33,69,69,-64,-83,20,15,17,-54,-81,30,21,-100,64,87,60,-39,89,94,29,-71,-81,-61,-87,12,-15,7,-84,87,-41,-64,43,33,11,-34,68,-21,-64,-87,30,-5,-93,-17,-40,-1,27,10,-37,59,92,-51,-74,71,87,-76,49,-39,-1,2,-74,-66,98,88,-70,-4,-37,70,-43,-73,90,96,-72,-65,31,-91,8,98,-63,10,-98,-37,11,44,12,-2,26,-76,-38,-49,-75,53,-53,48,-47,33,68,-54,20,36],[45,-74,-14,-64,12,-47,5,-11,-57,87,37,17,-17,66,-23,-91,29,76,-37,0,93,33,77,-7,49,95,37,-13,16,-91,95,-12,-27,-54,-52,-28,100,-87,-10,90,-31,51,78,-27,74,-25,-38,-40,46,-12,-15,43,85,59,-11,3,-28,-92,46,-60,-17,-54,34,47,-24,-38,-53,17,74,-45,44,89,-100,-48,49,-46,-97,-64,-43,61,-39,-33,-21,-52,-17,82,-71,35,-10,-80,-22,11,-33,68,-84,97,90,45,94,-45],[11,82,-51,71,72,51,-56,20,-50,19,-77,63,-24,25,-41,-4,92,60,-22,33,60,-48,95,30,-30,96,0,-42,95,-29,-14,75,21,-26,66,-82,-23,54,-80,100,63,25,-12,50,-46,81,65,0,51,28,16,-68,20,61,88,2,12,29,8,-41,35,-83,16,57,-52,98,62,-17,-73,7,4,-66,-98,-71,-75,-78,31,-64,60,-40,-17,38,-31,51,-51,40,-17,-16,-24,39,-30,1,82,42,-1,29,15,78,-28,80],[51,16,64,-71,-42,-41,-63,-39,-6,81,-49,38,-80,-78,52,93,89,-96,-78,-71,-73,-30,61,-6,-90,32,99,-53,-39,-1,62,-15,92,-45,61,46,-70,99,-29,-11,-13,-78,-91,-62,21,-9,-92,-9,-32,15,-4,84,57,-92,68,47,78,17,63,75,2,24,-94,5,-19,-41,43,-89,-24,6,43,77,40,4,-35,-60,-86,-89,-70,-52,87,-18,70,8,52,25,-69,60,-4,-15,-14,-28,5,2,20,30,-46,-18,-70,47],[29,-100,29,18,52,11,-97,45,77,16,50,55,23,-87,-18,-72,-70,-99,40,8,-48,28,-80,-47,82,21,28,-51,48,24,51,20,-84,47,47,77,89,70,47,-9,-48,64,-56,-11,-45,61,-36,17,50,44,49,63,37,-56,-54,-78,-18,-22,-16,88,8,88,-58,38,-90,-22,-34,18,-9,9,-97,89,-81,-33,86,94,98,-11,-26,-74,47,-95,-22,99,36,-83,92,66,-14,4,-47,-13,-76,-39,-23,-80,26,56,-73,-56],[95,57,71,30,-88,-24,20,-76,68,100,-99,13,-24,-58,2,10,-24,38,87,23,17,-40,59,-39,-45,-61,53,38,-55,8,90,-71,-63,91,41,68,85,45,-81,26,-98,-5,55,-44,40,70,-79,-70,-68,-85,26,-58,80,-60,-32,89,0,-33,81,18,-66,4,93,-16,22,95,-84,92,-13,-48,19,29,28,-11,-27,-41,-1,33,50,50,12,3,81,20,86,-29,-46,57,-12,72,-28,12,-30,-27,30,-99,-65,47,-66,-17],[59,23,-6,66,-82,55,-77,67,45,-89,48,86,13,7,-60,-92,-58,82,41,-95,-47,-56,56,87,15,-73,15,-17,-21,-90,-32,-67,-25,57,-47,49,-34,-78,88,-99,-83,63,-4,-52,-4,72,14,-2,-56,15,-57,-6,51,94,-3,60,18,41,28,6,27,99,73,10,-71,-30,66,-10,-91,-15,-24,-8,33,-89,-53,-65,15,0,-85,-18,-6,-29,27,29,63,-78,24,-99,83,-81,15,59,93,-15,85,48,30,39,2,44],[94,-43,-93,-24,92,74,-22,45,-51,88,46,3,17,-78,-44,24,-54,-23,-5,52,-78,-61,7,-63,45,74,44,61,79,-45,-59,38,-90,89,-79,8,36,-22,79,-79,-86,-93,-58,66,90,-28,58,8,-95,-90,26,-59,24,-96,15,69,-2,-28,97,78,-98,63,-14,78,22,3,-86,-89,-78,-7,91,59,31,49,-9,-16,-71,29,18,-59,33,-54,-7,75,-83,-69,95,-82,62,-98,-3,-46,51,81,79,96,82,56,-1,-25],[-28,46,66,-41,34,13,-3,2,-38,-69,57,-76,-95,-18,100,-52,48,83,89,70,63,31,-32,-96,-20,-14,22,37,90,8,85,48,46,3,40,5,-100,-31,-11,-88,30,-17,57,-69,51,20,43,2,-24,-61,-95,-70,93,-58,-61,97,-66,-12,16,-6,22,-9,-6,4,-87,38,-85,64,11,-66,-70,-56,49,-69,-85,-55,12,-22,40,46,-79,22,60,9,78,94,77,26,40,-33,82,52,-91,-18,100,19,98,-55,83,2],[95,83,-48,-12,-68,-30,35,70,19,-80,-3,67,25,0,0,-11,-58,-44,-23,-41,-11,99,-58,21,-48,17,51,-43,40,-68,80,-37,53,-41,-75,-22,32,-59,40,66,48,-6,-1,-7,33,-73,-62,87,42,100,-9,78,55,3,18,79,-77,9,-12,92,37,15,39,22,-9,-30,14,18,56,0,47,-7,9,-94,35,-48,42,-87,26,-9,100,5,75,-50,61,71,96,-18,-3,13,33,34,9,-85,-34,27,89,41,53,-81],[-71,89,-12,-51,86,-16,23,-60,9,-94,89,26,-33,-14,68,93,22,-42,29,45,-48,93,-7,-92,51,68,-84,4,-85,26,-62,-96,-83,-39,22,-96,-13,19,-61,-98,80,-35,67,-80,-18,35,99,4,-75,78,-46,-6,90,30,73,94,3,31,-89,-55,-67,-76,-35,74,93,-21,-28,-43,39,-54,-61,38,97,44,-33,-89,83,93,53,32,-51,-93,-96,10,43,46,37,40,11,40,-53,-23,37,-80,8,-52,8,-89,10,67],[8,-56,21,-91,80,64,-7,57,73,55,2,-75,-72,-62,63,-13,-89,70,78,-54,98,100,98,-6,17,28,-31,50,90,-95,-75,-78,-24,55,-4,-18,-9,39,-2,-13,-69,-49,82,-9,-8,-73,8,-47,77,24,-10,-15,43,-33,34,24,-30,-96,-11,-33,63,91,33,47,36,66,91,2,-10,58,65,69,-44,-100,18,-18,-68,83,-82,-64,-93,-60,-6,-20,-14,48,67,56,-92,84,-63,-46,-67,92,-66,82,24,-5,15,12],[-14,-34,74,-18,-86,-54,-87,58,69,63,45,84,70,87,-28,-11,-39,62,50,-5,-37,82,2,-69,21,76,38,73,100,-75,-39,29,-24,40,15,29,-78,55,-75,24,8,-80,22,17,6,-25,98,-88,-75,28,10,69,71,-19,-40,42,89,71,8,-14,73,12,10,-95,94,79,90,-73,45,28,75,12,-72,-23,-96,-44,-42,-54,-90,-76,-30,-3,20,62,46,-66,65,52,-35,11,33,84,76,-33,58,-51,66,-12,79,22],[89,33,-17,-44,-25,-58,-74,51,85,51,32,23,3,-100,15,-8,85,-60,-54,92,95,-50,18,91,-43,-63,32,-8,48,-55,24,64,-49,29,-73,-83,76,-57,-16,-49,-70,7,54,64,-41,25,-50,-97,60,-61,-82,90,-54,79,9,-21,-13,62,9,-23,-17,-23,95,64,43,-78,-66,15,6,65,-84,-9,-97,-38,-59,-93,46,-53,25,-32,24,-27,-49,-75,-49,-84,-76,69,67,-5,9,17,-60,17,30,34,53,-22,32,-73],[0,-6,100,-32,-5,57,17,22,-60,-73,-67,-28,31,-63,-24,65,86,78,44,-28,100,-6,-91,60,73,-55,24,99,1,4,-90,-15,39,-81,14,92,-68,-44,59,96,-98,26,-66,12,99,25,83,80,22,26,83,-60,56,46,-72,-19,-51,-28,-19,-6,96,32,86,49,25,-51,-62,-78,82,40,-23,50,-19,56,-10,57,14,-99,5,48,42,75,50,-46,-39,-28,28,-44,-98,-90,87,3,90,-80,-65,-92,80,-1,-34,-68],[-30,67,-10,-73,-97,7,73,19,39,88,-85,100,-71,43,74,99,-45,-69,-19,-46,-9,-9,-69,45,-3,-79,-92,-69,42,-92,-74,4,-81,87,98,83,67,-64,-50,68,1,49,2,52,17,85,36,-12,36,-8,19,78,-84,42,26,54,-71,-42,-16,-20,-5,-57,60,-92,100,-89,-76,77,-94,-77,72,-2,70,-11,57,86,-15,-14,70,88,93,-81,30,16,-68,51,-79,47,-44,0,56,-7,11,29,-60,92,67,-27,-40,87],[-27,90,39,26,2,15,80,3,19,61,49,-17,90,46,-74,1,-3,68,-80,-78,63,-34,9,28,24,89,53,35,62,-92,-46,81,-25,-39,36,76,-64,42,-19,-36,-35,13,-86,69,-25,-88,-36,67,-90,77,-51,-51,91,2,97,-34,-96,-75,8,8,-95,74,2,56,-73,-53,41,33,-58,-19,-49,-36,-33,67,-66,-94,-14,0,-4,-24,-24,39,-42,54,-13,16,-69,-3,-18,83,-69,93,-95,-9,22,-24,-19,82,36,27],[-91,-100,-49,-74,-67,-96,59,-25,5,31,82,62,20,-72,-12,-92,-52,-81,70,-68,-14,88,-17,5,91,-41,-22,29,-46,-9,61,41,-56,52,53,82,32,-90,36,-47,4,-68,-94,-49,24,-69,2,8,-15,57,95,-57,90,53,-15,61,-43,-45,-24,-71,73,-48,67,78,83,-36,-96,12,37,50,60,0,82,-23,-83,-6,49,-62,99,21,75,96,11,47,78,27,55,61,-69,-26,3,-99,-89,-99,-77,1,-84,32,76,5],[-58,-14,-88,7,-16,-19,-46,76,-12,88,-26,90,-21,80,65,-2,50,-32,14,40,-83,-71,2,87,96,-44,69,11,-13,-44,-59,75,100,-92,-45,-91,-64,96,2,-62,-11,-4,52,69,-46,-92,-1,-70,-85,8,44,-99,-83,-25,47,-96,8,-52,62,-64,25,-99,-11,11,-100,-73,45,-70,-68,84,5,7,34,69,30,-41,55,-58,-75,-76,93,-14,75,11,29,79,2,78,16,-6,-63,79,55,78,54,-9,-2,27,79,41],[-25,11,21,44,-88,-51,-58,72,55,91,100,-78,-76,67,-16,-11,51,-5,-83,-12,29,-33,15,-31,-95,26,94,54,9,-22,100,-87,55,-20,11,27,-80,35,97,-23,31,40,-80,77,2,92,-45,33,-13,-18,57,88,-57,20,65,32,77,30,-10,86,-81,-94,-8,-75,-44,-16,-92,44,-94,-36,-39,-69,-9,-55,-81,-77,34,92,-93,17,55,33,0,-30,1,-37,77,-99,-91,-99,-42,-31,78,52,61,76,-98,-88,-71,-70],[-48,-42,-87,85,-90,-67,29,36,-92,-13,22,85,19,57,-48,-77,81,91,20,11,84,-15,-26,-18,34,90,74,-33,-84,-92,29,-39,-100,-26,4,-39,-48,-32,27,63,-67,12,62,-11,6,-1,-70,64,45,49,49,38,-100,-46,73,24,-99,-5,-3,-35,83,21,-70,8,-10,0,27,-58,50,-76,-1,33,57,24,-86,82,-37,-44,12,-6,20,-85,-5,-17,-44,-58,15,-87,32,-84,-92,27,15,-97,13,51,-59,100,-65,-73],[94,59,-23,-98,-72,79,-89,14,97,-70,-87,-25,-60,54,60,-75,-82,-48,-12,-53,-42,-18,-2,-39,-22,-34,-8,-74,7,-100,97,-49,96,-4,67,49,-2,18,-4,37,-47,86,-44,13,-67,-26,77,68,-4,-90,-100,-14,94,78,17,48,45,-77,-100,-50,-11,50,-49,59,-52,-22,-28,-38,92,20,0,-61,32,-41,-4,24,82,-58,31,44,-54,-79,17,-45,49,-7,92,-36,-29,-55,68,-66,59,90,25,34,-8,-8,-13,38],[50,12,7,-32,90,-55,67,64,27,36,-98,-83,55,-85,-29,61,-68,-40,-18,14,41,49,-13,91,67,-52,-15,-63,-72,-15,3,-9,88,-31,0,-4,-78,30,79,58,-87,-65,74,89,-24,-90,-39,38,1,88,-23,-82,62,80,-81,-99,-99,-3,-92,79,-32,94,-83,34,-89,-3,-96,96,-71,-79,33,51,-2,10,56,-76,100,-32,16,-88,-58,-74,-32,24,-22,-9,22,-81,-12,54,-36,-22,87,-87,39,-75,-57,63,91,-52],[-55,-97,92,89,67,3,-4,1,-85,54,-11,71,7,-75,-52,-80,-3,88,-43,-17,-71,-50,-16,42,76,-14,-98,16,-60,45,-16,2,-69,-58,-42,-38,11,-78,-67,-81,-59,-69,37,-52,-31,45,-15,69,-53,24,17,-13,-73,-61,-81,33,-43,10,54,31,-4,-48,17,75,37,-26,64,20,31,-69,49,-8,30,80,-99,-64,-69,-89,-52,-32,88,80,-31,-87,67,-90,55,89,51,80,50,-67,-93,16,47,77,-18,72,28,9],[-66,86,85,79,87,-25,-93,31,-21,20,-36,38,-70,100,91,-50,-15,44,92,-98,-72,-7,-75,48,34,79,56,8,-52,-96,-31,-2,-18,-20,26,95,-31,83,-42,-42,24,79,-36,-26,-23,-6,93,9,92,-63,61,-16,-22,-37,-7,82,18,82,-28,46,-66,9,10,39,15,11,-50,98,91,42,-37,74,87,-25,29,79,-53,48,-23,9,-25,67,20,-6,-37,55,-55,70,58,35,-5,-69,-3,-60,-19,-57,-62,-93,-63,-68],[62,-20,35,-17,14,-49,64,45,-68,-75,95,39,29,-22,-46,30,-78,64,50,-95,55,-32,8,-31,-88,-44,23,-86,53,57,-77,39,-43,-73,92,38,78,96,-63,-29,-14,-7,-31,92,-56,-71,53,-84,-44,66,-55,66,98,75,-46,53,-65,-50,78,-50,72,43,-19,4,92,-27,-58,-31,-83,-70,-26,-62,38,83,-99,-21,93,-86,-10,-33,-51,8,96,2,82,64,-72,49,-89,38,13,50,88,-62,-76,-4,81,15,91,48],[34,-2,-13,23,-87,87,-75,78,38,62,22,-61,-76,18,92,100,-90,35,-9,-44,-77,45,-80,86,-93,17,98,-100,77,-1,-8,57,24,-53,-52,-29,25,-40,-11,4,65,-36,76,44,91,18,-76,53,-60,-49,24,-13,1,32,-5,41,0,-4,-3,-85,-15,80,-2,-66,-44,-35,10,43,76,-7,-92,-66,-65,-8,6,53,36,-1,-87,97,60,-77,21,-37,98,67,8,-23,-56,95,85,-59,45,-44,54,40,6,-96,77,37],[67,-88,-2,-84,-51,75,-55,-60,-25,78,-2,50,-23,45,71,6,41,65,24,64,26,29,-13,51,29,-26,-93,-56,36,70,-92,49,-16,77,-3,-44,-28,-65,64,48,-88,-38,79,60,-80,14,3,8,51,53,-48,-80,42,5,77,74,-1,50,13,51,-6,-32,36,-12,76,-56,-18,84,-78,-47,-80,-12,-10,94,-43,-31,-41,12,63,-86,37,81,-80,-34,100,86,60,-14,83,-38,-6,-51,-56,-52,-17,-27,68,-53,33,15],[69,-44,68,-36,51,29,-79,63,-50,-13,6,50,-10,77,2,-30,5,-75,13,-84,-86,-72,-78,-32,23,76,-7,-62,32,24,59,-28,54,70,64,72,14,-88,-94,-28,66,0,100,-89,-71,-30,37,-24,-54,37,-94,40,38,84,-47,29,67,-92,-77,18,98,42,-96,25,96,85,-80,12,-39,4,-24,81,-65,67,-59,70,94,95,66,-13,-17,45,65,-44,-7,-44,86,25,-85,-8,-50,51,89,-43,-20,-11,-33,-37,-100,79],[-34,-81,-80,-2,-64,19,72,-4,-73,-20,100,87,44,35,46,-31,-92,-28,10,-44,31,-4,83,3,72,56,-17,85,-19,-34,-81,-43,-53,-70,82,20,56,-40,-18,-68,-97,-61,-13,57,61,-57,94,-82,-66,68,27,50,-60,39,90,-57,48,-84,73,38,85,-43,57,-64,43,-48,69,-11,36,95,5,-45,7,95,71,21,35,-100,-17,88,19,19,-21,-4,-68,-88,-32,-40,34,-62,-98,-92,40,95,-14,73,53,-55,63,-16],[81,30,15,53,-88,77,-35,89,34,63,89,15,-54,-84,-58,-62,3,68,-10,49,44,-65,22,10,-59,-8,86,100,-12,75,-93,-20,-75,-37,94,-11,-82,61,51,-9,-59,-49,-21,-21,83,-18,-31,-60,-13,-49,50,23,89,-24,-80,42,-26,-31,66,-97,-59,-35,-12,-75,60,23,73,-70,13,93,70,25,18,-61,37,-11,99,32,-26,18,77,64,90,2,-17,-21,-66,-62,-63,-54,-69,-60,-53,-59,36,62,-78,46,17,-35],[-11,-67,-61,-7,12,14,-38,-77,56,-89,68,-53,-46,99,-86,98,-36,42,40,80,-91,55,86,97,83,9,-65,9,0,32,4,17,58,53,-52,-83,-98,-22,-40,-27,-96,-86,86,29,-81,-33,54,1,-83,-4,44,-1,-27,-7,15,-43,-30,38,-31,35,6,17,-59,-79,22,-66,43,-51,5,83,13,-18,9,-70,53,-92,-38,73,7,42,10,10,-6,12,-40,21,-73,27,75,31,-43,43,2,-72,37,53,-43,-36,-86,-97],[-4,76,87,80,-50,-54,72,-31,-48,-72,68,-67,22,62,-54,-47,66,-31,-70,-80,-85,-92,28,54,-52,-97,-80,58,-49,-90,-36,44,14,76,-55,58,-62,27,-67,36,-69,81,82,-58,59,-75,54,35,-25,70,84,37,48,-26,-26,-68,-67,-26,-6,-76,-57,18,81,-49,-22,0,21,96,85,-70,-97,12,89,24,25,8,14,92,-52,50,49,21,-48,-86,32,45,-46,76,16,-55,-40,25,28,-92,7,-72,18,-62,15,-67],[-22,20,86,33,0,-6,-17,-58,38,40,-17,-41,4,50,54,-59,-57,-66,27,73,64,4,13,-17,-97,94,-62,-65,-97,34,78,6,-9,2,64,-98,20,61,39,63,-26,-14,-72,-61,-57,57,-43,83,18,-17,-17,-70,16,-79,-59,-22,41,-67,5,-12,27,31,-15,29,7,5,-43,75,37,-60,30,-63,-12,46,-69,23,-28,15,-10,-22,91,2,-82,13,-64,78,-4,34,-5,20,6,92,80,1,-57,-54,30,10,70,94],[-100,88,-62,-7,6,-89,-44,-66,-100,-62,75,-83,98,22,-96,97,55,1,-98,-55,27,-37,-40,-23,36,-27,-21,-7,94,-45,38,84,-13,-85,-76,1,-3,64,-46,-24,-11,2,80,-40,-53,30,-76,72,39,18,-33,-15,31,48,12,-34,75,63,-48,-93,16,-41,-5,31,-97,56,-10,-67,-22,99,-7,-48,38,-70,43,-52,-80,-87,99,-79,-86,42,-95,-22,25,-22,16,74,-22,-82,3,55,9,-68,71,55,-15,22,-1,-38],[19,-77,20,33,-73,28,-33,74,56,-72,95,-41,-89,71,-99,46,11,-74,82,-26,-58,-99,-98,7,71,39,63,-79,-65,-81,55,-89,-91,-5,-7,-38,31,-100,37,36,17,-18,84,94,-62,-40,25,-55,-71,-27,-74,-44,33,21,-76,23,-53,38,-64,-71,99,22,88,-43,100,30,2,44,44,55,-10,-82,72,59,-4,-59,45,-97,95,32,49,11,-27,5,53,-74,94,0,-92,43,8,-37,56,-52,-60,-44,58,97,15,14],[-31,13,7,28,19,66,82,85,-36,53,71,19,43,56,37,14,99,-64,-88,76,-16,-11,67,-98,-55,38,86,-8,49,10,-54,7,86,-60,-43,43,33,-19,84,87,-12,-60,7,38,52,42,64,-51,-96,-51,30,40,92,97,-87,43,100,43,-14,7,-26,86,-66,34,-46,-26,-78,81,-79,35,-16,-3,82,-43,58,-100,-18,48,70,17,82,81,78,-30,19,9,72,17,47,-23,-92,-87,-82,73,-39,-83,-94,27,41,-94],[-24,-24,52,-35,-18,39,36,-1,99,-20,46,26,-77,-73,-39,-24,-71,49,48,88,43,69,16,-10,-98,37,-16,-79,-37,17,10,-40,-77,-93,57,-77,-17,98,-30,-24,77,-48,33,-3,96,-50,-22,-33,-45,18,-22,11,-90,11,31,-16,98,-6,36,-70,-46,-23,75,-24,-69,-5,73,-50,-99,96,86,34,-33,4,-71,-54,93,54,44,-83,-60,-67,92,-75,26,63,-19,-7,61,53,-77,17,-78,-73,64,-56,-46,-95,-51,9],[-52,38,-47,-77,-100,-24,84,77,0,-80,-25,-14,-12,-16,54,-41,39,67,-10,54,70,-88,98,80,8,-86,64,7,-64,-17,4,-18,-99,-88,-28,59,-17,-86,15,-66,-15,-87,-97,89,-83,80,3,-80,90,57,80,38,-18,-29,68,-30,76,34,-68,28,-27,83,-81,67,13,16,-16,-15,-16,70,61,4,-4,33,-24,-55,-75,72,61,-7,47,71,-86,77,-29,39,42,76,57,-60,7,77,-3,28,-67,43,59,3,-76,-79],[-36,48,-49,27,18,-53,17,-6,-23,-43,-57,-56,38,-58,-15,11,-55,94,-60,-13,-93,-13,53,67,23,-42,38,67,61,-22,-74,56,-5,12,-45,-12,-88,98,34,47,29,16,-6,97,99,-18,-75,-44,-50,99,37,62,-19,-23,-49,-20,-63,-22,11,-92,41,-97,-86,-75,-51,83,-55,99,4,6,52,86,-40,-35,-60,-47,-99,89,-66,-69,99,-60,-54,-95,42,-92,-76,-15,29,-5,4,74,96,-18,-60,61,-59,37,78,32],[13,-54,34,53,72,-46,-35,61,-60,33,60,-28,-93,48,35,42,-28,42,-65,-62,98,-85,19,90,-74,52,-68,42,53,-49,-25,-52,-24,-3,51,80,13,-11,-69,45,-42,-34,79,24,65,-51,-67,28,-2,50,9,-55,-88,-94,44,72,14,-70,42,-56,71,78,40,-8,40,99,-28,-60,-37,96,93,40,-23,68,81,57,33,27,-76,0,64,20,-12,3,-12,99,80,-24,-56,-87,53,24,26,-78,-71,21,35,-90,-17,11],[-45,71,63,73,-60,95,-78,94,90,80,-21,36,-17,-44,34,-42,-48,-13,51,68,-51,89,22,-68,-28,-33,34,40,-7,-43,-29,-4,86,-85,41,-50,17,-22,-4,-6,-68,-93,-7,-12,64,76,3,-72,17,-94,7,-44,19,90,32,-10,-87,62,-46,-33,-38,-37,-27,78,-97,96,52,-7,49,-26,41,48,6,-43,82,-43,-72,-14,86,-6,-64,50,63,-37,56,61,-71,64,8,-94,-17,-24,13,-56,-51,53,-69,81,11,12],[24,-38,50,73,-19,-58,-99,-16,-100,88,57,-48,-3,-83,93,-28,85,-10,-90,-55,-10,-51,-77,55,58,63,-87,80,-28,-34,19,20,17,9,-81,53,-49,-98,-16,100,62,-52,81,-41,79,-40,-13,-35,-96,70,96,41,-74,84,41,-52,48,39,-38,82,-82,-46,-44,5,50,-82,1,7,61,-91,2,54,-26,-89,-40,-9,-82,-38,26,-32,79,-95,-51,98,7,-82,-94,19,-25,1,-22,-100,-49,69,78,51,-82,42,-55,40],[51,-76,26,72,61,21,85,81,9,-43,-80,-20,-80,-96,-89,-36,47,5,8,-65,-30,69,15,-56,-19,40,-78,-58,74,-1,-95,42,-10,99,-86,16,-18,-57,29,-40,-17,93,-63,-43,-96,-77,-72,-25,-11,-60,-15,-24,69,-98,-25,90,28,31,54,-75,-4,-63,79,69,-44,-22,-17,-43,41,-2,-56,-76,23,-60,26,69,37,-26,39,3,-60,94,18,-11,-39,-62,-14,53,87,-78,81,78,-56,-54,-32,59,72,-59,-84,2],[38,70,14,-6,-41,29,-65,79,-47,99,66,-27,-65,-18,37,0,-35,-85,8,13,-71,-27,-68,-65,36,64,40,-73,-89,58,-1,84,-61,-96,-21,24,68,79,88,0,12,-14,-40,13,37,-53,-43,100,-78,-46,-79,61,-38,-25,-92,89,-45,-76,29,1,-56,16,90,89,-100,24,33,48,-57,-67,48,-9,-6,-56,-64,12,89,-46,61,18,-82,89,56,-43,93,-10,-61,85,-48,63,46,-40,57,14,-88,-16,6,-34,46,-66],[40,-43,-22,57,72,-60,58,-72,22,98,-20,32,-53,-31,14,-26,80,-82,-59,84,-35,-26,-72,35,20,15,-81,63,29,86,-66,2,-55,30,19,-74,-87,43,28,100,50,-6,99,30,37,-88,26,0,96,-16,-89,-46,98,57,-8,96,93,-83,17,-97,-17,31,-77,-18,-19,-78,-94,49,94,43,98,89,30,-87,70,-65,-21,-48,-33,-78,-66,36,80,-77,71,37,56,-7,-47,46,-28,34,-27,-73,-36,81,-62,83,67,49],[35,34,-43,-91,-6,-25,-69,-30,91,-68,71,-24,96,-49,-12,97,-80,42,4,-18,-19,41,-31,90,-99,-8,90,-52,-94,-26,-68,-94,-84,-88,-44,43,-75,-28,3,-96,-5,13,-31,70,55,3,-93,-3,29,-71,0,-65,-31,53,-30,-23,-51,-61,49,-11,-72,16,73,56,-65,40,-96,-60,33,19,51,66,47,66,17,-43,-68,-35,-24,70,-58,21,74,90,95,67,-27,-97,-17,24,-56,100,-45,-47,-81,99,80,-79,63,-24],[58,-98,-57,-9,0,94,27,56,-17,-58,26,-21,28,-73,-81,-97,76,27,54,98,14,35,-43,-52,2,-40,-85,43,-54,-69,-93,50,-25,71,-73,39,-18,61,-75,4,-77,-37,-54,79,-4,-49,91,33,-93,-9,-8,-63,22,41,89,-41,40,95,-98,75,-10,-11,59,-97,43,4,30,-1,-35,22,-8,-45,-18,75,-16,-91,-41,-11,-26,42,-83,3,79,21,44,71,23,93,53,-35,45,-90,-63,-44,-15,22,-53,-12,-32,-60],[-35,-59,-31,5,9,-21,28,55,88,-74,-30,-26,94,-69,1,62,-43,-73,-89,-48,-99,-74,31,64,-51,-38,57,58,76,-22,20,-73,78,-70,20,-79,51,-2,-87,-73,9,-21,6,6,-42,-54,71,82,64,14,-54,8,-78,48,84,-75,-59,22,11,32,-69,30,-39,-50,38,49,17,-13,46,-73,9,84,63,-18,83,-62,78,48,18,32,-23,61,-29,99,75,-39,-96,9,-13,-46,51,64,59,80,-58,-2,-67,37,20,-97],[-26,41,-94,-60,44,-23,-32,-57,8,43,-17,36,-42,0,41,2,14,34,-23,100,89,47,-96,73,96,-60,-32,-28,-2,14,-28,-89,-73,-35,99,-33,75,49,89,-29,-23,88,-21,-22,71,1,-64,-69,92,69,-71,-92,-98,-15,-57,76,15,-29,-15,72,5,-59,-51,46,80,-39,-93,-90,-98,65,-61,25,-27,87,-76,-30,27,8,4,-87,-49,-49,94,60,-6,-60,58,-32,41,96,96,-37,1,43,87,-79,-12,-59,34,-45],[-35,-2,18,68,-99,69,86,-72,-52,-1,-65,88,-10,-60,-41,80,-49,-20,-49,67,-49,-84,-58,86,67,100,83,-54,-67,-30,-6,95,-98,2,-16,87,44,-32,62,12,12,-43,68,-31,-66,70,99,44,60,27,-63,-95,-79,25,80,95,29,41,-15,8,48,-46,43,47,21,67,-71,-37,-32,15,79,12,-76,-14,88,56,-88,-19,60,75,88,-95,-100,43,63,-92,26,43,-28,-59,27,-87,-67,-30,-13,-49,12,-54,85,-89],[83,47,1,26,63,37,64,24,58,-4,6,-65,77,79,73,81,-53,76,-67,46,32,-69,29,-99,-63,-15,-55,99,85,9,81,-100,-88,-72,42,-73,-90,20,56,11,-37,-84,-54,24,57,-42,61,30,-53,-12,-71,27,-55,-86,83,9,48,-93,-21,-59,60,-46,65,39,54,-93,61,67,-42,30,45,74,95,-58,-26,70,22,-82,-29,-1,-16,33,-50,-34,100,-86,-42,-43,29,68,-96,-22,-22,-39,41,-34,-50,7,-6,77],[-13,21,-28,-36,-22,11,44,76,-96,-38,-81,5,-17,-16,-20,36,-70,-47,-66,-30,-60,-83,-97,-75,-67,-64,27,92,6,14,-67,-35,-83,85,-9,4,98,18,-8,-66,-9,-41,91,0,-59,42,78,-21,-19,60,-61,5,95,-24,70,8,6,19,85,60,34,-28,30,-77,-3,84,-97,-85,18,53,-57,-22,-29,83,-72,-78,-22,59,-10,-88,-22,-89,0,-30,-85,-13,82,-30,-53,-23,49,-57,-37,21,-7,36,83,91,-89,11],[83,-97,-86,-21,-11,-14,-20,-4,32,-93,39,-92,-87,95,-14,-13,65,36,61,-31,64,-84,-83,4,-67,5,39,-70,-76,-100,-29,-33,40,-98,87,61,55,-90,92,-53,51,21,81,66,-26,-42,90,42,21,52,-79,-52,-26,-99,44,-56,-34,87,-34,43,65,91,-8,89,29,-62,-35,-73,-34,-29,16,96,80,-44,-19,-50,71,87,-44,88,48,62,33,-46,73,-73,-43,50,5,-38,-5,-84,-17,99,34,-20,-62,-26,-73,-73],[-2,-11,-39,-21,-58,-93,44,-95,49,-11,-38,60,32,-38,-34,-6,-41,-29,37,-68,-77,88,30,-15,57,-56,82,-75,-92,-65,84,13,55,-4,18,-81,40,68,-98,-66,-31,-39,74,94,-47,2,-42,73,92,-51,-23,-45,-35,-50,-71,-4,-58,9,-21,-32,-97,-10,-67,-65,44,-48,4,-74,-6,-71,64,-4,61,48,11,51,55,-97,35,-10,90,2,-43,-35,62,-50,-2,-4,-66,11,-90,88,69,-36,-35,-60,-68,0,-98,-15],[-44,-40,29,-11,61,12,46,-91,-66,-70,-99,-52,34,99,60,40,3,20,-34,20,56,-42,85,92,47,22,95,67,-9,-97,11,73,91,-51,-38,-53,-93,0,-1,-33,92,34,-75,-85,12,24,-71,-53,8,-90,44,47,-83,90,-36,99,1,-30,-95,58,-30,-70,63,63,70,-61,-65,-74,-92,68,-88,75,-37,-29,35,-16,-7,48,14,86,83,16,-81,-58,82,-31,38,100,1,-22,-8,0,-75,11,17,-38,22,-24,-5,-61],[39,93,-91,41,3,11,-58,-9,63,40,74,59,12,59,-49,-88,16,-63,-96,71,62,-85,1,5,-64,-37,52,59,21,-98,74,96,-59,26,91,51,44,-25,-70,41,-98,97,59,76,-77,2,-32,-92,80,-91,60,-45,77,-73,32,85,-50,-12,-41,-52,82,96,-21,97,-19,96,-70,-87,42,-32,-92,-11,-79,-73,51,-63,-74,-42,29,89,-89,-23,-72,7,-49,-90,-40,-30,67,65,88,-65,56,55,68,11,-54,-52,18,-77],[-17,74,82,23,-42,52,99,58,0,98,-45,23,-4,-91,-90,23,93,-86,-26,-50,67,-83,-96,7,38,-52,44,-24,53,91,46,82,-6,-64,75,-60,-23,-58,80,-96,-32,-5,73,70,-75,-41,1,-36,45,81,-96,94,100,-52,30,29,93,7,20,22,-53,74,-93,-96,29,22,-10,-2,-20,-47,-83,63,7,54,-72,45,-86,-44,-66,-42,-62,32,47,99,-62,-47,83,64,-14,-87,-61,33,-93,-31,-95,68,-27,-75,-16,33],[18,-48,57,75,-100,-100,5,-93,-27,7,53,-14,15,39,36,-23,78,-42,59,-1,-7,68,11,-45,-77,-26,70,76,-31,-9,16,27,24,94,-74,99,53,66,-14,92,-75,37,18,-24,-24,-74,-11,29,-31,59,-98,24,-87,87,5,-63,85,18,-29,86,22,48,92,-58,-94,40,85,62,64,51,-92,7,5,98,-31,-22,15,-96,-54,69,-31,-10,17,79,30,86,-59,-61,-17,49,-8,-63,46,35,90,41,-90,-33,-63,76],[-97,-2,-96,73,-30,-33,-98,78,28,-42,-31,98,93,6,46,79,-63,53,-45,76,-80,-36,-67,-69,30,-1,-5,100,-7,-36,-49,-42,58,63,49,-28,-69,29,35,30,90,37,-96,-54,78,65,-64,48,-65,-20,1,-76,-81,58,-95,-21,61,-17,22,64,-16,60,-75,48,29,63,94,-42,40,79,7,-77,-73,-82,51,22,83,40,40,-22,31,-26,-15,34,76,50,-39,1,86,-19,71,-38,64,24,-7,-18,-7,-52,90,58],[58,4,-96,98,80,5,-6,-66,-3,57,10,76,-38,-81,25,71,-78,64,-1,11,36,-36,28,15,-75,10,-65,4,40,11,-8,27,-40,-56,13,84,-47,-16,7,-64,31,-99,9,-98,43,74,-2,15,30,95,22,21,57,27,90,-22,-29,81,45,84,-11,48,78,-60,-56,15,-6,81,4,100,40,95,5,7,-83,45,-61,16,-31,5,-99,-98,28,-1,95,-39,81,27,-39,63,29,-80,-74,37,72,-99,-10,-53,13,-54],[-14,56,-13,79,-92,30,92,94,16,-95,-89,48,-54,72,96,-31,99,-75,20,73,81,71,10,6,97,-81,10,-16,-44,39,32,19,76,-44,-100,80,-81,60,23,-49,-69,41,49,-20,-40,-75,78,82,-10,-51,-39,24,-3,24,-25,-79,46,45,37,37,-83,98,-58,-10,38,28,21,29,-14,-26,-53,-73,-65,4,-57,40,12,61,64,10,-8,-68,-76,70,-6,87,26,74,45,-54,59,94,97,70,5,95,92,97,-89,-67],[-4,24,-18,31,81,-16,-16,-26,-82,-66,22,31,-65,13,49,75,66,15,76,93,-79,73,59,76,-43,-97,26,-74,-61,-84,3,99,47,33,-61,52,-41,-43,53,8,54,72,94,26,-16,-4,-60,-54,-100,35,-99,-68,27,47,-30,-9,-1,-61,46,-8,-41,68,45,-12,1,-84,93,67,72,-36,-23,-8,-88,54,37,-64,24,-33,92,-93,-11,-4,-100,-79,-32,-68,-18,-74,-63,60,84,-83,100,-53,6,-23,-84,-6,23,-2],[-48,-65,-21,37,-67,90,71,-30,67,-70,-65,20,0,-7,-8,-8,-70,62,-41,26,1,-68,-87,-64,-27,83,86,-30,-39,-30,-78,-87,20,-12,38,-6,-14,74,-28,82,85,9,-53,-65,-63,40,-79,46,-58,20,-23,78,11,22,35,32,-82,27,88,31,-60,-89,11,78,-75,-14,-63,14,-38,-39,-27,62,-88,78,-45,18,-4,35,1,72,-14,29,-5,-41,-54,-24,-93,-47,-5,45,-70,-21,-38,-66,13,11,78,-26,-62,47],[-91,-19,57,21,86,73,77,3,23,-19,-42,-2,56,-32,1,77,18,-96,-78,19,50,6,-88,-80,-13,62,-33,55,-84,-21,36,63,51,-53,23,-42,-94,-97,-50,1,-16,59,10,22,-25,-41,-5,38,78,-23,52,-100,-87,55,-38,68,-42,78,-88,-84,-45,-35,19,-51,-66,-90,38,7,-22,4,-67,19,-100,-18,-42,46,71,-96,76,-72,56,-77,-57,4,-5,-25,-73,-40,16,78,-84,-32,-1,13,44,16,84,-71,-6,99],[-5,39,-88,58,63,50,18,61,81,-60,-15,-14,-61,2,-39,94,-67,-20,-94,-68,-95,91,100,6,-7,23,40,-79,-48,-72,-34,20,46,-26,79,23,-99,80,72,-53,58,-57,37,80,-21,-71,97,72,-61,-93,-7,-54,43,-28,-89,-23,85,48,74,13,-32,12,1,100,78,-73,9,-59,-81,-1,64,61,63,93,-2,-46,-71,-7,-32,13,36,38,-58,33,13,-16,-3,40,-84,-82,67,63,24,2,41,-67,94,-13,-59,-48],[4,-65,41,53,-47,-26,94,56,70,30,-85,-28,85,56,57,85,-6,-97,16,97,20,-33,-54,27,-78,-99,51,-85,-19,-61,-51,-4,53,21,-48,-75,79,-91,98,-51,98,-64,5,53,-96,-30,-17,85,65,-24,-19,-24,-21,64,99,45,-47,35,37,4,-21,-69,75,-16,-13,-30,-84,88,-98,90,-92,-77,75,-45,43,12,24,-89,-95,-53,-31,-33,-52,11,-87,-13,92,-70,-43,-39,-16,34,-88,-27,74,84,51,-17,35,-27],[-18,-43,-17,100,55,-30,10,-61,2,-29,91,71,-60,7,-28,-50,-23,6,24,-12,-87,-66,-61,27,61,41,65,93,25,89,-62,84,-75,-60,-6,41,-55,-75,-82,99,73,5,-45,69,-31,-44,27,-48,99,-44,-68,-63,-6,30,56,-13,-76,-89,-45,-56,24,-60,84,-29,-93,-28,-7,-27,31,-63,3,-100,36,53,-53,-4,-76,71,32,29,-58,-18,-67,-48,-26,-81,-2,46,23,-45,-21,68,5,-71,83,-82,-38,-90,-16,-85],[19,9,-38,75,2,98,-34,-40,-74,-29,26,-100,96,0,-86,-10,-94,79,-57,96,88,97,-97,17,4,-24,43,-54,36,98,-10,44,-9,53,-81,-51,-93,-59,-91,40,84,76,47,-59,-26,-48,-14,-81,53,14,71,19,-20,-98,-5,-34,-25,52,-24,95,80,-68,-40,82,95,28,93,-21,73,-74,-74,1,-22,10,77,-27,48,21,5,74,54,-70,-27,42,-92,-92,-46,29,-36,57,-84,-55,-99,-23,3,76,45,-43,56,-54],[86,-7,-59,-35,-50,49,19,-23,-53,-61,-2,49,-80,-69,14,13,-3,-23,-33,-84,100,-18,56,30,-82,13,-5,10,-31,77,-75,60,79,-55,-8,0,35,-54,93,69,-42,-80,-2,-16,-1,66,-43,25,10,81,-97,-72,60,-99,33,-78,87,-29,-92,-64,85,81,-67,90,-89,0,53,19,-66,-90,-85,37,-55,-41,-42,64,-26,15,66,13,-24,98,62,-26,92,60,-57,6,-86,-27,40,-16,-80,8,49,-94,45,-61,-77,87],[42,19,-77,-23,25,-79,41,-63,-65,-5,76,-94,-9,94,77,-79,87,-51,-66,-9,5,-43,22,-39,58,-91,-46,-28,94,86,-40,-5,-97,17,-43,-5,53,42,23,-74,33,-82,-46,39,-80,-63,-81,67,43,85,52,-12,47,2,88,-19,17,31,24,-69,-83,-36,-59,-70,-19,60,22,-43,-11,-99,-43,-4,-31,-21,-65,50,64,56,-85,66,-20,-92,11,-7,53,-6,-72,38,47,-70,-73,-7,-19,-53,19,-76,50,-91,46,35],[-37,55,-40,-54,-79,20,65,-19,-84,61,27,-67,-48,29,-24,-78,-27,-88,-45,-25,-3,92,-46,81,31,-55,60,-3,-71,84,-12,98,99,87,16,-17,-65,-89,64,9,-69,76,-71,-79,77,-80,-69,-37,-33,9,-7,-28,42,-71,-11,3,-40,-44,6,-37,-16,-54,-15,-84,59,-79,55,-36,72,-72,-14,76,-78,52,72,-59,18,-40,97,45,-77,-87,81,58,-18,-60,-20,26,67,22,-73,-99,-90,-22,99,11,-35,-7,-69,23],[-66,-85,-80,82,-92,13,-99,-16,-12,-80,49,-38,-97,23,99,-76,-84,-10,36,56,-64,-16,72,-50,80,91,-2,28,-46,71,-89,-13,-95,58,84,-33,-57,-14,-86,13,-12,-44,-100,-40,3,-59,50,-56,25,96,10,5,-36,31,-4,37,-23,-73,97,44,53,-68,-64,-51,-8,-67,8,28,-96,-66,56,-39,73,-98,25,-12,94,65,32,39,-8,20,72,100,-11,5,-100,77,-100,-80,11,91,-63,27,78,14,-23,-78,87,-44],[88,-28,9,12,24,-97,91,98,61,21,39,-11,-65,-100,-66,-52,-84,35,-64,9,13,-15,12,-26,-71,-72,18,45,-52,97,24,44,47,75,-25,15,-45,47,-2,34,-25,5,2,73,38,-82,-91,39,-49,-88,14,-98,-83,-88,-43,-8,90,-47,-43,-45,38,-32,10,-56,14,-67,-17,77,-5,-94,-31,81,93,-61,35,-58,-99,13,-11,37,21,-35,57,27,-34,-1,51,-13,23,-63,-9,25,33,-77,69,17,-79,26,-69,7],[-70,-24,51,-60,18,34,-69,86,42,-12,17,-2,67,65,56,76,-10,-64,-82,-47,6,38,-23,-40,-49,71,-18,98,-50,-8,-91,-6,-2,36,16,-63,39,-24,-10,63,-25,37,-47,-79,-29,89,-52,-68,-93,41,-95,36,-93,-98,65,-73,53,-44,-8,-40,46,98,35,20,46,-39,-53,-67,95,-22,92,33,61,-29,-73,91,28,57,-98,20,69,18,80,43,25,-38,-48,57,55,-20,-50,-53,60,87,13,-42,51,82,-79,73],[-18,79,44,88,-19,22,-89,89,-76,-27,17,-6,-28,9,-8,79,-56,29,93,-43,32,67,83,96,74,39,-26,-3,-32,-80,80,16,-100,-13,29,-41,-53,-28,57,8,-71,40,-26,-89,88,-87,-19,-70,8,-80,-37,4,88,-86,6,-60,7,22,88,58,-23,27,-45,54,35,-41,-97,-76,76,32,3,-70,-56,5,80,64,-75,-74,-98,7,59,-23,-94,-58,10,-85,83,-71,52,-62,-12,95,33,16,41,-2,98,88,82,-87],[25,64,-49,14,-76,-95,56,-52,-70,63,-80,14,94,-54,15,77,44,40,66,0,1,-47,-74,72,-78,-29,-46,88,26,46,-96,-80,-64,-60,-80,-90,57,11,-30,-60,-81,-100,7,-23,31,-99,18,18,-30,-28,95,-1,74,65,89,-23,61,30,52,39,45,-12,74,91,23,-83,90,28,44,-85,-96,0,27,10,52,28,6,97,-1,-53,-3,-55,88,86,-79,-29,-67,80,32,84,31,-60,-78,-100,96,68,-81,84,0,89],[-84,-18,-46,17,-91,18,-45,79,42,-87,63,7,-2,-77,72,-83,-97,75,28,-24,79,-92,-21,-89,-90,-69,-70,-58,-86,34,77,-32,28,-1,-28,31,-19,-82,-40,1,27,-45,-65,-94,-18,52,-37,40,-78,77,14,-63,17,43,-15,52,83,-88,65,94,28,-56,-43,-73,-95,-63,10,-93,-8,93,-86,10,-49,-28,66,65,16,-26,50,21,-30,-30,59,40,87,19,-98,23,-27,52,9,-79,-3,62,-53,-17,4,5,-94,66],[50,-78,68,-74,-15,55,-92,68,50,90,-90,19,-5,-79,41,-39,90,61,-60,-53,12,90,12,-15,-48,49,-93,43,11,71,42,-95,50,89,100,0,-89,79,-63,81,-46,85,-15,52,12,55,-63,60,49,-96,34,-46,-73,38,15,-71,-78,15,-73,41,-73,-42,21,-54,49,-63,-16,2,-41,44,-90,-33,-99,86,12,3,29,35,-94,15,-72,70,-28,26,-73,20,-62,93,-56,-39,41,-89,-85,-52,-2,-88,-22,-44,62,-44],[67,92,-60,-33,-3,2,-73,54,-24,67,9,52,-24,8,-28,-97,-66,-51,48,-50,34,-78,-54,-94,-17,29,85,-43,-42,-99,22,-43,99,37,-67,44,-19,97,60,27,36,79,96,-88,-94,70,-99,83,95,-27,-18,-91,-55,-18,75,-79,-94,6,21,10,-79,-80,-54,83,37,-65,80,-26,37,98,-86,-53,-4,-74,53,-82,-58,-87,-54,5,75,-78,73,41,0,32,-16,-1,-21,-20,97,18,37,91,-59,-51,-35,-46,59,-2],[19,-71,96,-29,-71,7,-64,90,82,-55,-68,80,47,36,81,-31,-65,-14,-21,-15,-31,79,16,-20,22,37,-30,66,77,15,-30,-75,12,-42,53,-100,51,-48,73,-27,80,-11,-40,82,-16,-80,93,-97,-52,11,-9,-84,-93,24,39,-45,67,68,19,-44,41,26,41,76,66,-100,38,-46,9,13,-11,44,38,67,57,58,1,-65,64,39,-78,-35,7,17,97,76,-66,2,25,-74,-57,-1,90,-94,32,12,47,19,-41,84],[57,-10,54,76,-72,-83,11,-7,47,-27,-67,2,91,-40,54,44,98,70,10,-19,-53,-82,12,20,-57,21,-42,15,21,-11,-74,-31,-54,-31,23,-44,24,-98,-85,98,-80,-44,17,-99,22,26,-64,38,-19,9,-44,-24,22,31,-51,-9,100,-17,-79,-37,-79,20,84,-71,55,-73,-42,-74,33,0,5,-52,-25,-28,-64,82,-77,-13,61,-39,86,3,-26,-80,40,87,-35,-86,-40,62,-58,-99,77,58,-94,-22,74,36,-97,90],[-86,-8,82,60,-64,84,54,54,-58,-82,-90,-59,-22,37,-33,77,43,-58,-33,14,14,-29,-12,65,-79,-46,44,34,-49,76,-5,-22,79,15,79,-75,-49,43,-19,14,-100,-31,-45,65,34,23,31,-93,-11,47,14,-82,-95,-58,35,99,74,-61,-24,42,87,81,33,12,-74,38,-88,73,50,31,24,37,-2,-63,-55,-32,9,81,-77,1,-25,-76,14,-71,-90,98,-56,-73,80,-22,-74,-1,-16,-62,42,-93,-47,-44,87,50],[-34,28,80,12,98,40,55,1,19,-71,39,20,-85,90,-100,-74,-29,83,-41,28,-14,-80,97,-43,67,16,85,3,-30,-4,39,97,-42,-43,0,18,78,37,-86,11,81,40,42,-50,32,96,-65,18,49,-86,-2,62,-35,-78,48,58,26,17,76,49,86,75,91,-2,19,18,-27,-2,-70,-93,41,-71,-53,2,-81,-17,-87,80,-97,-68,-5,-91,-82,55,-34,-91,100,-16,-41,4,46,44,36,80,37,87,-22,-86,87,-51],[-27,-28,-43,-41,-77,-54,-80,-23,36,-74,96,-74,41,44,8,36,0,-79,-92,-91,92,-89,-98,58,79,26,-47,-77,59,100,9,33,-3,78,2,-94,10,-79,-31,17,20,57,99,-44,-41,4,28,20,75,80,25,76,-78,39,3,-18,33,-21,-30,28,-100,42,14,54,23,66,-34,42,42,75,-29,-69,21,-82,50,-28,39,-5,55,57,99,75,12,-55,45,75,37,12,-36,43,76,-39,66,-40,47,12,18,-68,-90,-62]]
    k = 4030
    expected = 4030
    assert Solution().maxSumSubmatrix(matrix, k) == expected
