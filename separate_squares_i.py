"""
LeetCode
3453. Separate Squares I
January 2026 Challenge
jramaswami
"""


import dataclasses
from typing import List


@dataclasses.dataclass(frozen = True)
class Square:
    x1: int
    y1: int
    x2: int
    y2: int
    area: int
    length: int


class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        EPS = pow(10, -5)
        squares0 = tuple(Square(x, y, x+l, y+l, l*l, l) for x, y, l in squares)
        min_y = min(sq.y1 for sq in squares0)
        max_y = max(sq.y2 for sq in squares0)

        def areas(y):
            above = 0
            below = 0
            for sq in squares0:
                if sq.y2 < y:
                    below += sq.area
                elif sq.y1 > y:
                    above += sq.area
                else:
                    # Line goes through square
                    y_above = sq.y2 - y
                    above += (sq.length * y_above)
                    y_below = y - sq.y1
                    below += (sq.length * y_below)
            return above, below

        # Binary search the answer
        low = min_y
        high = max_y
        # print(f'{low=} {high=} {abs(high-low)} {EPS}')
        soln = pow(10, 20)
        while 1:
            mid = low + ((high - low) / 2)
            above, below = areas(mid)
            delta = abs(above - below)
            # print(f'{mid=} {above=} {below=} {delta=}')
            if delta < EPS:
                soln = min(mid, soln)
                high = mid
                if abs(high - low) < EPS:
                    break
            elif above > below:
                low = mid
            else:
                high = mid
        return soln



def test_1():
    squares = [[0,0,1],[2,2,1]]
    expected = 1.000
    result = Solution().separateSquares(squares)
    print('result', result)
    assert abs(result - expected) < pow(10, -5)


def test_2():
    squares = [[0,0,2],[1,1,1]]
    expected = 1.16667
    result = Solution().separateSquares(squares)
    print('result', result)
    assert abs(result - expected) < pow(10, -5)


def test_3():
    "WA"
    squares = [[522261215,954313664,225462],[628661372,718610752,10667],[619734768,941310679,44788],[352367502,656774918,289036],[860247066,905800565,100123],[817623994,962847576,71460],[691552058,782740602,36271],[911356,152015365,513881],[462847044,859151855,233567],[672324240,954509294,685569]]
    expected = 1.16667
    result = Solution().separateSquares(squares)
    print('result', result)
    assert abs(result - expected) < pow(10, -5)

if __name__ == '__main__':
    squares = squares = [[0,0,2],[1,1,1]]
    expected = 1.16667
    result = Solution().separateSquares(squares)
    print('result', result)