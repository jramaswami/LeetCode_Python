"""
LeetCode
3394. Check if Grid can be Cut into Sections
March 2025 Challenge
jramaswami
"""


class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        xs = [(min(x1, x2), max(x1, x2)) for x1, _, x2, _ in rectangles]
        ys = [(min(y1, y2), max(y1, y2)) for _, y1, _, y2 in rectangles]
        xs.sort()
        ys.sort()


        def partition(ts):
            tstack = []
            for t1, t2 in ts:
                if not tstack:
                    tstack.append((t1, t2))
                elif t1 < tstack[-1][-1]:
                    _t1, _t2 = tstack.pop()
                    tstack.append((_t1, max(_t2, t2)))
                else:
                    tstack.append((t1, t2))
            return tstack

        xstack = partition(xs)
        ystack = partition(ys)
        return len(xstack) >= 3 or len(ystack) >= 3