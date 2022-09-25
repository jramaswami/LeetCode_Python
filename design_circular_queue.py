"""
LeetCode :: September 2022 Challenge :: Design Circular Queue
jramaswami
"""


class MyCircularQueue:

    def __init__(self, k: int):
        self.capacity = k
        self.size = 0
        self.arr = [None for _ in range(k)]
        self.front = 0
        self.back = k - 1

    def enQueue(self, value: int) -> bool:
        if self.size == self.capacity:
            return False

        self.back = (self.back + 1) % self.capacity
        self.arr[self.back] = value
        self.size += 1
        return True

    def deQueue(self) -> bool:
        if self.size == 0:
            return False
        self.arr[self.front] = None
        self.size -= 1
        self.front = (self.front + 1) % self.capacity
        return True

    def Front(self) -> int:
        val = self.arr[self.front]
        return (val if val is not None else -1)

    def Rear(self) -> int:
        val = self.arr[self.back]
        return (val if val is not None else -1)

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.capacity

    def __repr__(self):
        return f"MyCircularQueue(capacity={self.capacity}, size={self.size}, values={self.arr}, front={self.front}, back={self.back})"


#
# TESTING
#
def test_1():
    methods = ["MyCircularQueue", "enQueue", "enQueue", "enQueue", "enQueue", "Rear", "isFull", "deQueue", "enQueue", "Rear"]
    arguments = [[3], [1], [2], [3], [4], [], [], [], [4], []]
    expected = [None, True, True, True, False, 3, True, True, True, 4]

    Q = MyCircularQueue(*arguments[0])
    for meth, args, exp in zip(methods[1:], arguments[1:], expected[1:]):
        result = getattr(Q, meth)(*args)
        print(meth, args, exp)
        print(Q)
        assert result == exp