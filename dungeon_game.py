"""
LeetCode :: October 2021 Challenge :: Dungeon Game
jramaswami
"""


from collections import defaultdict
from math import inf


class Solution:


    def calculateMinimumHP(self, dungeon):
        dp = [[defaultdict(lambda: inf) for _ in row] for row in dungeon]

        for r, row in enumerate(dungeon):
            for c, room in enumerate(row):
                if r == 0 and c == 0:
                    dp[r][c][room] = room
                else:
                    # You can come from above.
                    if r > 0:
                        for prev_hp, path_hp in dp[r-1][c].items():
                            new_hp = prev_hp + room
                            new_path_hp = min(path_hp, new_hp)
                            dp[r][c][new_hp] = min(new_path_hp, dp[r][c][new_hp])
                    # You can com from the left.
                    if c > 0:
                        for prev_hp, path_hp in dp[r][c-1].items():
                            new_hp = prev_hp + room
                            new_path_hp = min(path_hp, new_hp)
                            dp[r][c][new_hp] = min(new_path_hp, dp[r][c][new_hp])

        soln = inf
        for path_hp in dp[-1][-1].values():
            if path_hp <= 0:
                soln = min(soln, (-1 * path_hp) + 1)
            else:
                soln = min(soln, 1)
        return soln


def test_1():
    dungeon = [[-2,-3,3],[-5,-10,1],[10,30,-5]]
    expected = 7
    assert Solution().calculateMinimumHP(dungeon) == expected


def test_2():
    dungeon = [[0]]
    expected = 1
    assert Solution().calculateMinimumHP(dungeon) == expected


def main():
    """Main program."""
    # Timing
    import random
    dungeon = [[random.randint(-100, 10) for _ in range(200)] for _ in range(200)]
    for row in dungeon:
        print(row)
    print('solution', Solution().calculateMinimumHP(dungeon))


if __name__ == '__main__':
    main()

