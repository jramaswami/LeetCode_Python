"""
LeetCode
1146. Snapshot Array
June 2023 Challenge
jramaswami
"""


class SnapshotArray:

    def __init__(self, length: int):
        self.array = []
        self.array.append([0 for _ in range(length)])

    def set(self, index: int, val: int) -> None:
        self.array[-1][index] = val

    def snap(self) -> int:
        """
        int snap() takes a snapshot of the array and returns the snap_id: the total number of times we called snap() minus 1.
        """
        self.array.append(list(self.array[-1]))
        return len(self.array) - 2

    def get(self, index: int, snap_id: int) -> int:
        return self.array[snap_id][index]


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)


null = None


def test_1():
    methods = ["SnapshotArray","set","snap","set","get"]
    arguments = [[3],[0,5],[],[0,6],[0,0]]
    expected = [null,null,0,null,5]
    sa = SnapshotArray(*arguments[0])
    for (m, a, e) in zip(methods[1:], arguments[1:], expected[1:]):
        result = getattr(sa, m)(*a)
        print(f"sa.{m}({a}) should be {e} result is {result}")
        assert result == e