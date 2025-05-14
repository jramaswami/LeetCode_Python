"""
LeetCode
3337. Total Characters in String After Transformations II
May 2025 Challenge
jramaswami

Thank You Larry!
"""


from typing import List


class Solution:
    def lengthAfterTransformations(self, s: str, t: int, nums: List[int]) -> int:
        MOD = pow(10, 9) + 7
        identity = [[0] * 26 for _ in range(26)]
        for i in range(26):
            identity[i][i] = 1

        def mat_power(matrix, power):
            if power == 0:
                return identity
            if power == 1:
                return matrix

            m = mat_power(matrix, power // 2)
            if power % 2 == 0:
                return mat_mult(m, m)
            return mat_mult(mat_mult(m, m), matrix)


        def mat_mult(a, b):
            aR = len(a)
            aC = len(a[0])
            bC = len(b[0])

            result = [[0 for _ in range(bC)] for _ in range(aR)]

            for i in range(aR):
                for j in range(aC):
                    for k in range(bC):
                        result[i][k] += a[i][j] * b[j][k]
                        result[i][k] %= MOD

            return result

        f = [[0] * 26]
        for c in s:
            f[0][ord(c) - ord('a')] += 1

        trans = [[0] * 26 for _ in range(26)]
        for index, x in enumerate(nums):
            for i in range(x):
                trans[index][(index + i + 1) % 26] += 1

        r = mat_mult(f, mat_power(trans, t))
        return sum(r[0]) % MOD