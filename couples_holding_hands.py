"""
LeetCode :: 765. Couples Holding Hands
jramaswami
"""


class Couples:

    def __init__(self, row):
        self.row = row
        self.loc = [0 for _ in row]
        for i, n in enumerate(row):
            self.loc[n] = i

    def swap(self, left, right):
        left_val = self.row[left]
        right_val = self.row[right]
        # Swap values.
        self.row[left], self.row[right] = self.row[right], self.row[left]
        # Update locations.
        self.loc[left_val] = right
        self.loc[right_val] = left

    def is_pair(self, left):
        min_val = min(self.row[left], self.row[left + 1])
        max_val = max(self.row[left], self.row[left + 1])
        return max_val % 2 and min_val + 1 == max_val

    def find(self, value):
        return self.loc[value]

    def __getitem__(self, key):
        return self.row[key]

    def __len__(self):
        return len(self.row)


class Solution:

    def minSwapsCouples(self, row):
        couples = Couples(row)
        soln = 0
        for i in range(0, len(couples), 2):
            if not couples.is_pair(i):
                spouse = couples[i] - 1 if couples[i] % 2 else couples[i] + 1
                j = couples.find(spouse)
                couples.swap(i + 1, j)
                soln += 1
        return soln


def test_1():
    row = [0,2,1,3]
    expected = 1
    assert Solution().minSwapsCouples(row) == expected


def test_2():
    row = [3,2,0,1]
    expected = 0
    assert Solution().minSwapsCouples(row) == expected


def test_3():
    row = [45, 33, 36, 9, 34, 72, 17, 60, 89, 3, 6, 90, 32, 66, 44, 70, 26, 98, 68, 28, 81, 76, 74, 22, 65, 11, 51, 62, 59, 52, 20, 78, 94, 82, 79, 57, 42, 86, 91, 39, 87, 85, 29, 41, 71, 99, 35, 80, 25, 92, 38, 55, 0, 67, 47, 13, 23, 37, 2, 46, 56, 15, 54, 63, 97, 96, 31, 16, 8, 48, 61, 75, 73, 53, 40, 69, 27, 7, 84, 1, 49, 24, 58, 77, 4, 88, 14, 64, 12, 93, 83, 18, 21, 43, 5, 95, 50, 10, 19, 30]
    expected = 45
    assert Solution().minSwapsCouples(row) == expected
