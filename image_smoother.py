"""
LeetCode
661. Image Smoother
December 2023 Challenge
jramaswami
"""


class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        sm = [[0 for _ in row] for row in img]
        for r, row in enumerate(img):
            for c, _ in enumerate(row):
                s = 0
                t = 0
                for r1 in range(max(0, r-1), min(r+2, len(img))):
                    for c1 in range(max(0, c-1), min(c+2, len(img[r1]))):
                        s += img[r1][c1]
                        t += 1
                sm[r][c] = s // t
        return sm