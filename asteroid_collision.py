"""
LeetCode
735. Asteroid Collision
July 2023 Challenge
jramaswami
"""


from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        soln = []
        for n in asteroids:
            if n > 0:
                # Put a positive asteroid in the soln
                soln.append(n)
            elif n < 0:
                # Remove any positive asteroids that are smaller by size than
                # the negative asteroid
                while soln and soln[-1] > 0 and soln[-1] < abs(n):
                    soln.pop()

                if not soln or soln[-1] < 0:
                    # If soln is empty or contains only negative asteroids,
                    # the negative asteroid will keep going
                    soln.append(n)
                elif soln[-1] == abs(n):
                    # If the soln if the last postive asteroid is the same size
                    # as the negative asteroid, remove both
                    soln.pop()
        return soln


def test_1():
    asteroids = [5,10,-5]
    expected = [5,10]
    assert Solution().asteroidCollision(asteroids) == expected


def test_2():
    asteroids = [8,-8]
    expected = []
    assert Solution().asteroidCollision(asteroids) == expected


def test_3():
    asteroids = [10,2,-5]
    expected = [10]
    assert Solution().asteroidCollision(asteroids) == expected
